#!/usr/bin/env python3
"""
Stride Documentation Extractor (stride-docgen)

Extracts API documentation, metadata, ports, and signals from .stride source files
and generates structured Markdown reference pages and VitePress navigation configurations.
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional

class StrideLexer:
    """Tokenizes Stride syntax while handling comments and multi-line strings."""
    
    TOKEN_REGEX = re.compile(
        r'(?P<COMMENT>#[^\r\n]*)'
        r'|(?P<STRING>"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')'
        r'|(?P<BRACE_OPEN>\{)'
        r'|(?P<BRACE_CLOSE>\})'
        r'|(?P<BRACKET_OPEN>\[)'
        r'|(?P<BRACKET_CLOSE>\])'
        r'|(?P<NAMESPACE_OP>::)'
        r'|(?P<STREAM_OP>>>|->)'
        r'|(?P<COLON>:)'
        r'|(?P<COMMA>,)'
        r'|(?P<SEMICOLON>;)'
        r'|(?P<NUMBER>-?[0-9]+(?:\.[0-9]+)?)'
        r'|(?P<IDENT>[A-Za-z_][A-Za-z0-9_]*)'
        r'|(?P<WS>\s+)'
        r'|(?P<OTHER>[^\sA-Za-z0-9_:"\'{}[\];,]+)'
    )

    @classmethod
    def tokenize(cls, text: str):
        tokens = []
        for m in cls.TOKEN_REGEX.finditer(text):
            kind = m.lastgroup
            val = m.group(kind)
            if kind in ('WS', 'COMMENT'):
                continue
            if kind == 'STRING':
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1].replace('\\"', '"').replace('\\\\', '\\')
                elif val.startswith("'") and val.endswith("'"):
                    val = val[1:-1].replace("\\'", "'").replace('\\\\', '\\')
            tokens.append((kind, val))
        return tokens


class StrideDocParser:
    """Parses token streams into structured metadata for modules, loops, constants, and types."""

    DECLARATION_KEYWORDS = {
        'module', 'loop', 'block', 'object', 'constant', 'platform', 'framework', 'system', 'type'
    }

    PORT_TYPES = {
        'mainInputPort', 'mainOutputPort', 'propertyInputPort', 'propertyOutputPort',
        'inputPort', 'outputPort', 'port'
    }

    ENTITY_TYPES = {
        'signal', 'switch', 'trigger', 'stream', 'list', 'buffer'
    }

    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.length = len(tokens)

    def peek(self, offset=0):
        target = self.idx + offset
        if target < self.length:
            return self.tokens[target]
        return (None, None)

    def advance(self):
        tok = self.peek()
        self.idx += 1
        return tok

    def parse_file(self) -> Dict[str, Any]:
        results = {
            'package': None,
            'declarations': []
        }

        while self.idx < self.length:
            kind, val = self.peek()

            # package Foo::Bar
            if kind == 'IDENT' and val == 'package':
                self.advance()
                pkg_parts = []
                while self.idx < self.length:
                    k, v = self.peek()
                    if k == 'IDENT':
                        pkg_parts.append(v)
                        self.advance()
                        if self.peek()[0] == 'NAMESPACE_OP':
                            self.advance()
                        else:
                            break
                    else:
                        break
                if pkg_parts:
                    results['package'] = "::".join(pkg_parts)
                continue

            # Declarations: module Foo { ... }
            if kind == 'IDENT' and val in self.DECLARATION_KEYWORDS:
                decl_type = val
                self.advance()
                name_kind, name_val = self.advance()
                decl_name = name_val if name_kind in ('IDENT', 'NUMBER') else "Anonymous"

                b_kind, b_val = self.peek()
                if b_kind == 'BRACE_OPEN':
                    self.advance()
                    decl_body = self.parse_block()
                    decl_body['kind'] = decl_type
                    decl_body['name'] = decl_name
                    results['declarations'].append(decl_body)
                continue

            self.advance()

        return results

    def parse_block(self) -> Dict[str, Any]:
        block_data = {
            'meta': '',
            'value': None,
            'ports': [],
            'entities': [],
            'properties': {}
        }

        brace_depth = 1

        while self.idx < self.length and brace_depth > 0:
            kind, val = self.peek()

            if kind == 'BRACE_OPEN':
                brace_depth += 1
                self.advance()
                continue

            if kind == 'BRACE_CLOSE':
                brace_depth -= 1
                self.advance()
                if brace_depth == 0:
                    break
                continue

            # meta: "..."
            if kind == 'IDENT' and val == 'meta':
                self.advance()
                if self.peek()[0] == 'COLON':
                    self.advance()
                s_kind, s_val = self.peek()
                if s_kind == 'STRING':
                    block_data['meta'] = s_val
                    self.advance()
                continue

            # value: ...
            if kind == 'IDENT' and val == 'value':
                self.advance()
                if self.peek()[0] == 'COLON':
                    self.advance()
                v_kind, v_val = self.advance()
                block_data['value'] = v_val
                continue

            # ports: [ ... ]
            if kind == 'IDENT' and val == 'ports':
                self.advance()
                if self.peek()[0] == 'COLON':
                    self.advance()
                if self.peek()[0] == 'BRACKET_OPEN':
                    self.advance()
                    block_data['ports'] = self.parse_ports_list()
                continue

            # entities: [ ... ]
            if kind == 'IDENT' and val == 'entities':
                self.advance()
                if self.peek()[0] == 'COLON':
                    self.advance()
                if self.peek()[0] == 'BRACKET_OPEN':
                    self.advance()
                    block_data['entities'] = self.parse_entities_list()
                continue

            self.advance()

        return block_data

    def parse_ports_list(self) -> List[Dict[str, Any]]:
        ports = []
        bracket_depth = 1

        while self.idx < self.length and bracket_depth > 0:
            kind, val = self.peek()

            if kind == 'BRACKET_OPEN':
                bracket_depth += 1
                self.advance()
                continue

            if kind == 'BRACKET_CLOSE':
                bracket_depth -= 1
                self.advance()
                if bracket_depth == 0:
                    break
                continue

            if kind == 'COMMA':
                self.advance()
                continue

            if kind == 'IDENT' and val in self.PORT_TYPES:
                port_kind = val
                self.advance()
                id_kind, id_val = self.advance()
                port_id = id_val if id_kind == 'IDENT' else ""

                port_meta = ""
                port_name = port_id
                port_entity = ""
                port_default = ""

                if self.peek()[0] == 'BRACE_OPEN':
                    self.advance()
                    port_brace_depth = 1
                    while self.idx < self.length and port_brace_depth > 0:
                        p_kind, p_val = self.peek()
                        if p_kind == 'BRACE_OPEN':
                            port_brace_depth += 1
                            self.advance()
                            continue
                        if p_kind == 'BRACE_CLOSE':
                            port_brace_depth -= 1
                            self.advance()
                            if port_brace_depth == 0:
                                break
                            continue

                        if p_kind == 'IDENT' and p_val == 'name':
                            self.advance()
                            if self.peek()[0] == 'COLON': self.advance()
                            port_name = str(self.advance()[1])
                        elif p_kind == 'IDENT' and p_val == 'entity':
                            self.advance()
                            if self.peek()[0] == 'COLON': self.advance()
                            port_entity = str(self.advance()[1])
                        elif p_kind == 'IDENT' and p_val == 'meta':
                            self.advance()
                            if self.peek()[0] == 'COLON': self.advance()
                            port_meta = str(self.advance()[1])
                        elif p_kind == 'IDENT' and p_val == 'default':
                            self.advance()
                            if self.peek()[0] == 'COLON': self.advance()
                            port_default = str(self.advance()[1])
                        else:
                            self.advance()

                ports.append({
                    'id': port_id,
                    'name': port_name,
                    'kind': port_kind,
                    'entity': port_entity,
                    'default': port_default,
                    'meta': port_meta
                })
                continue

            self.advance()

        return ports

    def parse_entities_list(self) -> List[Dict[str, Any]]:
        entities = []
        bracket_depth = 1

        while self.idx < self.length and bracket_depth > 0:
            kind, val = self.peek()

            if kind == 'BRACKET_OPEN':
                bracket_depth += 1
                self.advance()
                continue

            if kind == 'BRACKET_CLOSE':
                bracket_depth -= 1
                self.advance()
                if bracket_depth == 0:
                    break
                continue

            if kind == 'COMMA':
                self.advance()
                continue

            if kind == 'IDENT' and val in self.ENTITY_TYPES:
                ent_type = val
                self.advance()
                id_kind, id_val = self.advance()
                ent_id = id_val if id_kind == 'IDENT' else ""

                if self.peek()[0] == 'BRACKET_OPEN':
                    self.advance()
                    idx_val = ""
                    while self.idx < self.length and self.peek()[0] != 'BRACKET_CLOSE':
                        idx_val += str(self.advance()[1])
                    if self.peek()[0] == 'BRACKET_CLOSE': self.advance()
                    ent_id = f"{ent_id}[{idx_val}]"

                ent_default = ""
                ent_rate = ""
                ent_domain = ""
                ent_meta = ""

                if self.peek()[0] == 'BRACE_OPEN':
                    self.advance()
                    ent_brace_depth = 1
                    while self.idx < self.length and ent_brace_depth > 0:
                        e_kind, e_val = self.peek()
                        if e_kind == 'BRACE_OPEN':
                            ent_brace_depth += 1
                            self.advance()
                            continue
                        if e_kind == 'BRACE_CLOSE':
                            ent_brace_depth -= 1
                            self.advance()
                            if ent_brace_depth == 0:
                                break
                            continue

                        if e_kind == 'IDENT' and e_val == 'default':
                            self.advance()
                            if self.peek()[0] == 'COLON': self.advance()
                            ent_default = str(self.advance()[1])
                        elif e_kind == 'IDENT' and e_val == 'rate':
                            self.advance()
                            if self.peek()[0] == 'COLON': self.advance()
                            ent_rate = str(self.advance()[1])
                        elif e_kind == 'IDENT' and e_val == 'domain':
                            self.advance()
                            if self.peek()[0] == 'COLON': self.advance()
                            ent_domain = str(self.advance()[1])
                        elif e_kind == 'IDENT' and e_val == 'meta':
                            self.advance()
                            if self.peek()[0] == 'COLON': self.advance()
                            ent_meta = str(self.advance()[1])
                        else:
                            self.advance()

                entities.append({
                    'id': ent_id,
                    'type': ent_type,
                    'default': ent_default,
                    'rate': ent_rate,
                    'domain': ent_domain,
                    'meta': ent_meta
                })
                continue

            self.advance()

        return entities


def friendly_port_kind(kind: str) -> str:
    mapping = {
        'mainInputPort': 'Input Stream',
        'mainOutputPort': 'Output Stream',
        'propertyInputPort': 'Property In',
        'propertyOutputPort': 'Property Out',
        'inputPort': 'Input',
        'outputPort': 'Output',
        'port': 'Port'
    }
    return mapping.get(kind, kind)


def generate_markdown_for_declaration(decl: Dict[str, Any], package_name: str, file_rel_path: str, is_root_library: bool) -> str:
    name = decl.get('name', 'Anonymous')
    kind = decl.get('kind', 'module').capitalize()
    meta = decl.get('meta', '').strip()
    ports = decl.get('ports', [])
    entities = decl.get('entities', [])
    value = decl.get('value', None)

    md = []
    # Frontmatter
    clean_desc = meta.replace('\n', ' ').replace('"', "'")[:140] if meta else f"{name} {kind.lower()} definition."
    md.append("---")
    md.append(f"title: {name}")
    md.append(f"description: \"{clean_desc}\"")
    md.append("---\n")

    # Title & Badge
    md.append(f"# {name}\n")
    md.append(f'<span class="stride-badge">{kind}</span> `package {package_name}`\n')

    # Description
    if meta:
        md.append(f"{meta}\n")
    else:
        md.append(f"*{kind} declared in `{file_rel_path}`.*\n")

    # If it's a constant
    if value is not None:
        md.append("## Value\n")
        md.append("```stride")
        md.append(f"constant {name} = {value}")
        md.append("```\n")

    # Ports Table
    if ports:
        md.append("## Ports & Properties\n")
        md.append("| Name | Type | Target Signal | Default | Description |")
        md.append("| :--- | :--- | :--- | :--- | :--- |")
        for p in ports:
            p_name = f"`{p['name']}`" if p['name'] else "—"
            p_kind = friendly_port_kind(p['kind'])
            p_entity = f"`{p['entity']}`" if p['entity'] else "—"
            p_def = f"`{p['default']}`" if p['default'] else "—"
            p_desc = p['meta'].replace('\n', ' ') if p['meta'] else "—"
            md.append(f"| {p_name} | {p_kind} | {p_entity} | {p_def} | {p_desc} |")
        md.append("")

    # Internal Signals & Entities Table
    notable_entities = [e for e in entities if e['default'] or e['meta'] or e['rate']]
    if notable_entities:
        md.append("## Signals & Attributes\n")
        md.append("| Signal | Type | Default | Rate / Domain | Description |")
        md.append("| :--- | :--- | :--- | :--- | :--- |")
        for e in notable_entities:
            e_id = f"`{e['id']}`"
            e_type = f"`{e['type']}`"
            e_def = f"`{e['default']}`" if e['default'] else "—"
            rate_domain = []
            if e['rate']: rate_domain.append(f"Rate: {e['rate']}")
            if e['domain']: rate_domain.append(f"Domain: {e['domain']}")
            e_rd = ", ".join(rate_domain) if rate_domain else "—"
            e_desc = e['meta'].replace('\n', ' ') if e['meta'] else "—"
            md.append(f"| {e_id} | {e_type} | {e_def} | {e_rd} | {e_desc} |")
        md.append("")

    # Usage Example
    md.append("## Usage\n")
    md.append("```stride")
    md.append("import Stride;\n")
    prop_args = []
    for p in ports:
        if 'property' in p['kind'].lower() and p['name']:
            val = p['default'] if p['default'] else "..."
            prop_args.append(f"{p['name']}: {val}")
    args_str = f"({', '.join(prop_args[:3])})" if prop_args else "()"

    if is_root_library:
        # Directly available in Stride root namespace
        md.append(f"# Available in root namespace:")
        md.append(f"Signal >> {name}{args_str} >> Output;")
    else:
        cat = package_name.replace("Stride::", "")
        md.append(f"# Access via {cat} category:")
        md.append(f"Signal >> {cat}::{name}{args_str} >> Output;")
    md.append("```\n")

    return "\n".join(md)


def process_strideroot(strideroot_path: Path, output_docs_dir: Path) -> Dict[str, Any]:
    """Scans strideroot/library, extracts docs, and writes markdown files."""
    library_dir = strideroot_path / "library" / "1.0"
    if not library_dir.exists():
        print(f"Error: Could not find library directory at {library_dir}")
        return {}

    ref_dir = output_docs_dir / "reference" / "library"
    ref_dir.mkdir(parents=True, exist_ok=True)

    # Categories:
    # 1. "Stride (Core Library)" for all root files
    # 2. "Stride::<Subdir>" for subdirectories (Generators, Filters, etc.)
    sidebar_groups = {}
    sidebar_order = ["Stride (Core Library)"]

    IGNORED_DIRS = {'doc', '.strdcache', 'tests', 'local'}

    for root, dirs, files in os.walk(library_dir):
        # Prune ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS and not d.startswith('.')]

        root_path = Path(root)
        rel_to_lib = root_path.relative_to(library_dir)
        stride_files = [f for f in files if f.endswith(".stride")]

        # Determine category and package
        is_root = (rel_to_lib == Path('.'))

        if is_root:
            group_key = "Stride (Core Library)"
            pkg_name = "Stride"
            cat_slug = "core"
        else:
            cat_name = rel_to_lib.parts[0]
            group_key = f"Stride::{cat_name}"
            pkg_name = f"Stride::{cat_name}"
            cat_slug = cat_name.lower()
            if group_key not in sidebar_order:
                sidebar_order.append(group_key)

        cat_dir = ref_dir / cat_slug
        cat_dir.mkdir(parents=True, exist_ok=True)

        if group_key not in sidebar_groups:
            sidebar_groups[group_key] = {
                'slug': cat_slug,
                'package': pkg_name,
                'items': []
            }

        for sf in stride_files:
            file_path = root_path / sf
            try:
                content = file_path.read_text(encoding='utf-8')
            except Exception as e:
                print(f"Failed to read {file_path}: {e}")
                continue

            tokens = StrideLexer.tokenize(content)
            parser = StrideDocParser(tokens)
            parsed = parser.parse_file()

            effective_pkg = parsed['package'] if parsed['package'] else pkg_name

            for decl in parsed['declarations']:
                decl_name = decl.get('name', '')
                # Skip internal declarations starting with double underscore
                if decl_name.startswith('__') or decl_name == "Anonymous":
                    continue

                md_content = generate_markdown_for_declaration(
                    decl, effective_pkg, str(file_path.relative_to(strideroot_path)), is_root
                )

                file_slug = decl_name.lower().replace(" ", "-")
                md_filename = f"{file_slug}.md"
                out_file = cat_dir / md_filename
                out_file.write_text(md_content, encoding='utf-8')

                sidebar_groups[group_key]['items'].append({
                    'text': decl_name,
                    'link': f"/reference/library/{cat_slug}/{file_slug}"
                })

    # Build sorted sidebar items
    sidebar_config = []
    for g_key in sidebar_order:
        if g_key not in sidebar_groups:
            continue
        g_data = sidebar_groups[g_key]
        # Deduplicate items by text
        seen = set()
        deduped = []
        for it in sorted(g_data['items'], key=lambda x: x['text']):
            if it['text'] not in seen:
                seen.add(it['text'])
                deduped.append(it)

        if deduped:
            sidebar_config.append({
                'text': g_key,
                'collapsed': g_key != "Stride (Core Library)",
                'items': deduped
            })

    # Generate an Index Page for the Library Reference
    index_md = [
        "---",
        "title: Standard Library Reference",
        "description: Specification of modules, stream processors, filters, generators, and arithmetic operations in the Stride standard library.",
        "---\n",
        "# Standard Library Reference\n",
        "The Stride standard library provides the foundational primitives for signal routing, multi-rate audio digital signal processing (DSP), mathematical operations, and state machine transitions.\n",
        "## Namespace Organization\n",
        "- **`package Stride` (Core Library)**: Primitives located in the root of the standard library (`Math`, `Logic`, `BasicOperations`, `Comparisons`, etc.) belong to the root `Stride` package. They are imported automatically or via `import Stride`, and are available directly in global scope (e.g. `Sin()`, `Sum()`, `Abs()`).",
        "- **Sub-packages (`Stride::<Category>`)**: Components residing in subdirectories (`Generators`, `Filters`, `Serial`, `Osc`) form categorized sub-packages. When using `import Stride`, they are referenced via category qualification (e.g. `Generators::Oscillator`, `Filters::BiQuad`), or directly via category import (`import Stride::Generators`).\n",
        "## Package Modules\n"
    ]

    for entry in sidebar_config:
        title = entry['text']
        items = entry['items']
        count = len(items)
        index_md.append(f"### {title} ({count} definitions)\n")
        sample_items = items[:8]
        links = [f"[`{item['text']}`]({item['link']})" for item in sample_items]
        index_md.append(", ".join(links) + ("..." if count > 8 else ""))
        index_md.append("\n")

    (ref_dir / "index.md").write_text("\n".join(index_md), encoding='utf-8')

    return sidebar_config


def main():
    parser = argparse.ArgumentParser(description="Stride Documentation Extractor (stride-docgen)")
    parser.add_argument("--strideroot", default=None, help="Path to strideroot repository")
    parser.add_argument("--output", default="docs", help="Target output documentation directory")
    args = parser.parse_args()

    strideroot_candidates = [
        args.strideroot,
        os.environ.get("STRIDEROOT"),
        Path("../Stride/strideroot"),
        Path("../../Stride/strideroot"),
        Path("c:/Users/Andres/source/repos/Stride/strideroot")
    ]

    strideroot_path = None
    for c in strideroot_candidates:
        if c and Path(c).exists() and (Path(c) / "library").exists():
            strideroot_path = Path(c).resolve()
            break

    if not strideroot_path:
        print("Error: Could not locate a valid strideroot directory.")
        sys.exit(1)

    output_dir = Path(args.output).resolve()
    print(f"[*] Extracting docs from: {strideroot_path}")
    print(f"[*] Output directory:     {output_dir}")

    sidebar = process_strideroot(strideroot_path, output_dir)

    sidebar_file = output_dir / ".vitepress" / "sidebar-reference.json"
    sidebar_file.parent.mkdir(parents=True, exist_ok=True)
    sidebar_file.write_text(json.dumps(sidebar, indent=2), encoding='utf-8')

    total_modules = sum(len(g['items']) for g in sidebar)
    print(f"[+] Successfully extracted {total_modules} definitions across {len(sidebar)} packages!")
    print(f"[+] Sidebar config saved to: {sidebar_file}")


if __name__ == "__main__":
    main()
