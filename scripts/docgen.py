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
    """Tokenizes Stride syntax with line number tracking."""
    
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
        line_no = 1
        last_pos = 0

        for m in cls.TOKEN_REGEX.finditer(text):
            match_start = m.start()
            if match_start > last_pos:
                line_no += text.count('\n', last_pos, match_start)
                last_pos = match_start

            kind = m.lastgroup
            val = m.group(kind)
            if kind in ('WS', 'COMMENT'):
                continue
            if kind == 'STRING':
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1].replace('\\"', '"').replace('\\\\', '\\')
                elif val.startswith("'") and val.endswith("'"):
                    val = val[1:-1].replace("\\'", "'").replace('\\\\', '\\')
            tokens.append((kind, val, line_no))
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
        return (None, None, 0)

    def advance(self):
        tok = self.peek()
        self.idx += 1
        return tok

    def parse_property_value(self) -> str:
        """Collects tokens until end of statement/property boundary."""
        val_parts = []
        bracket_depth = 0
        while self.idx < self.length:
            k, v, _ = self.peek()
            if bracket_depth == 0:
                if k in ('BRACE_CLOSE', 'SEMICOLON', 'COMMA'):
                    break
                if k == 'BRACKET_CLOSE':
                    break
                # If next is an IDENT followed by a COLON, that is the start of the next property
                if k == 'IDENT' and self.peek(1)[0] == 'COLON':
                    break

            if k == 'BRACKET_OPEN':
                bracket_depth += 1
            elif k == 'BRACKET_CLOSE':
                bracket_depth -= 1

            val_parts.append(str(v))
            self.advance()

        result = " ".join(val_parts).replace(" . ", ".").strip()
        return result

    def parse_file(self) -> Dict[str, Any]:
        results = {
            'package': None,
            'declarations': []
        }

        while self.idx < self.length:
            kind, val, line = self.peek()

            # package Foo::Bar
            if kind == 'IDENT' and val == 'package':
                self.advance()
                pkg_parts = []
                while self.idx < self.length:
                    k, v, _ = self.peek()
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
                decl_line = line
                self.advance()
                name_kind, name_val, _ = self.advance()
                decl_name = name_val if name_kind in ('IDENT', 'NUMBER') else "Anonymous"

                b_kind, b_val, _ = self.peek()
                if b_kind == 'BRACE_OPEN':
                    self.advance()
                    decl_body = self.parse_block()
                    decl_body['kind'] = decl_type
                    decl_body['name'] = decl_name
                    decl_body['line'] = decl_line
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
            kind, val, _ = self.peek()

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
            if kind == 'IDENT' and self.peek(1)[0] == 'COLON' and val == 'meta':
                self.advance() # 'meta'
                self.advance() # ':'
                s_kind, s_val, _ = self.peek()
                if s_kind == 'STRING':
                    block_data['meta'] = s_val
                    self.advance()
                else:
                    block_data['meta'] = self.parse_property_value().strip('"\'')
                continue

            # value: ...
            if kind == 'IDENT' and self.peek(1)[0] == 'COLON' and val == 'value':
                self.advance()
                self.advance()
                block_data['value'] = self.parse_property_value()
                continue

            # ports: [ ... ]
            if kind == 'IDENT' and self.peek(1)[0] == 'COLON' and val == 'ports':
                self.advance()
                self.advance()
                if self.peek()[0] == 'BRACKET_OPEN':
                    self.advance()
                    block_data['ports'] = self.parse_ports_list()
                continue

            # entities: [ ... ]
            if kind == 'IDENT' and self.peek(1)[0] == 'COLON' and val == 'entities':
                self.advance()
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
            kind, val, _ = self.peek()

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
                id_kind, id_val, _ = self.advance()
                port_id = id_val if id_kind == 'IDENT' else ""

                port_meta = ""
                port_name = port_id
                port_entity = ""
                port_default = ""

                if self.peek()[0] == 'BRACE_OPEN':
                    self.advance()
                    port_brace_depth = 1
                    while self.idx < self.length and port_brace_depth > 0:
                        p_kind, p_val, _ = self.peek()
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

                        if p_kind == 'IDENT' and self.peek(1)[0] == 'COLON':
                            prop_name = p_val
                            self.advance() # prop_name
                            self.advance() # ':'
                            prop_val = self.parse_property_value()
                            if prop_name == 'name':
                                port_name = prop_val.strip('"\'')
                            elif prop_name == 'entity':
                                port_entity = prop_val
                            elif prop_name == 'meta':
                                port_meta = prop_val.strip('"\'')
                            elif prop_name == 'default':
                                port_default = prop_val
                            continue

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
            kind, val, _ = self.peek()

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
                id_kind, id_val, _ = self.advance()
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
                ent_explicit_type = ""

                if self.peek()[0] == 'BRACE_OPEN':
                    self.advance()
                    ent_brace_depth = 1
                    while self.idx < self.length and ent_brace_depth > 0:
                        e_kind, e_val, _ = self.peek()
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

                        if e_kind == 'IDENT' and self.peek(1)[0] == 'COLON':
                            eprop_name = e_val
                            self.advance()
                            self.advance()
                            eprop_val = self.parse_property_value()
                            if eprop_name == 'default':
                                ent_default = eprop_val
                            elif eprop_name == 'rate':
                                ent_rate = eprop_val
                            elif eprop_name == 'domain':
                                ent_domain = eprop_val
                            elif eprop_name == 'type':
                                ent_explicit_type = eprop_val
                            elif eprop_name == 'meta':
                                ent_meta = eprop_val.strip('"\'')
                            continue

                        self.advance()

                entities.append({
                    'id': ent_id,
                    'kind': ent_type,
                    'type': ent_explicit_type if ent_explicit_type else ent_type,
                    'default': ent_default,
                    'rate': ent_rate,
                    'domain': ent_domain,
                    'meta': ent_meta
                })
                continue

            self.advance()

        return entities


def render_port_icon(kind: str) -> str:
    """Returns a sober, compact badge for the port/property kind."""
    if kind in ('mainInputPort', 'inputPort'):
        return '<span class="port-icon stream-in" title="Stream Input">»</span>'
    elif kind in ('mainOutputPort', 'outputPort'):
        return '<span class="port-icon stream-out" title="Stream Output">»</span>'
    elif kind == 'propertyInputPort':
        return '<span class="port-icon prop-in" title="Property Input">↓</span>'
    elif kind == 'propertyOutputPort':
        return '<span class="port-icon prop-out" title="Property Output">↑</span>'
    return '<span class="port-icon stream-in" title="Port">»</span>'


def format_rate_domain(rate: str, domain: str) -> str:
    """Combines rate and domain into a clean, compact representation."""
    parts = []
    if rate and rate != 'none':
        parts.append(f"`{rate}`")
    if domain:
        parts.append(f"`{domain}`")
    return " / ".join(parts) if parts else "—"


def generate_markdown_for_declaration(
    decl: Dict[str, Any],
    package_name: str,
    group_name: str,
    file_rel_path: str,
    file_basename: str,
    github_url: str,
    is_root_library: bool
) -> str:
    name = decl.get('name', 'Anonymous')
    kind = decl.get('kind', 'module').capitalize()
    meta = decl.get('meta', '').strip()
    ports = decl.get('ports', [])
    entities = decl.get('entities', [])
    value = decl.get('value', None)
    line_no = decl.get('line', 1)

    # Build entity lookup map
    entity_map = {}
    for e in entities:
        base_id = e['id'].split('[')[0].strip()
        entity_map[base_id] = e
        entity_map[e['id'].strip()] = e

    md = []
    # Frontmatter
    clean_desc = meta.replace('\n', ' ').replace('"', "'")[:140] if meta else f"{name} {kind.lower()} definition."
    md.append("---")
    md.append(f"title: {name}")
    md.append(f"description: \"{clean_desc}\"")
    md.append("---\n")

    # Header with Scope Note and GitHub Link
    source_label = f"{file_basename}:{line_no}"
    source_anchor = f'<a class="stride-source-link" href="{github_url}" target="_blank" rel="noopener" title="View source on GitHub">[{source_label}]</a>'
    
    md.append(f"# {name}\n")
    if is_root_library:
        md.append(f'<span class="stride-badge">{kind}</span> `package Stride` &bull; Group: **{group_name}** {source_anchor}\n')
    else:
        cat = package_name.replace("Stride::", "")
        md.append(f'<span class="stride-badge">{kind}</span> `package {package_name}` &bull; Namespace: **`{package_name}`** {source_anchor}\n')

    # Compact Overview Description
    if meta:
        md.append(f"{meta}\n")

    # If it's a constant
    if value is not None:
        md.append("## Value\n")
        md.append("```stride")
        md.append(f"constant {name} = {value}")
        md.append("```\n")

    # Partition ports into stream ports and properties
    stream_ports = [p for p in ports if 'property' not in p['kind'].lower()]
    properties = [p for p in ports if 'property' in p['kind'].lower()]

    # 1. Streams Table (if any stream ports)
    if stream_ports:
        md.append("## Streams\n")
        md.append("| | Stream | Type | Rate / Domain | Description |")
        md.append("| :-: | :--- | :--- | :--- | :--- |")
        for p in stream_ports:
            icon = render_port_icon(p['kind'])
            # Stream name
            s_name = p['name'] if (p['name'] and p['name'] != p['id']) else (p['entity'] if p['entity'] else p['id'])
            # Resolve from entity
            ent = entity_map.get(p['entity'], {})
            s_type = ent.get('type') or ent.get('kind') or 'signal'
            rate_domain = format_rate_domain(ent.get('rate', ''), ent.get('domain', ''))
            desc = p['meta'].replace('\n', ' ') if p['meta'] else (ent.get('meta', '').replace('\n', ' ') if ent.get('meta') else "—")
            md.append(f"| {icon} | `{s_name}` | `{s_type}` | {rate_domain} | {desc} |")
        md.append("")

    # 2. Properties Table (if any properties)
    if properties:
        md.append("## Properties\n")
        md.append("| | Property | Type | Default | Rate / Domain | Description |")
        md.append("| :-: | :--- | :--- | :--- | :--- | :--- |")
        for p in properties:
            icon = render_port_icon(p['kind'])
            p_name = p['name'] if p['name'] else p['id']
            # Resolve from entity
            ent = entity_map.get(p['entity'], {})
            p_def = p['default'] if p['default'] else ent.get('default', '')
            p_def_str = f"`{p_def}`" if p_def else "—"
            p_type = ent.get('type') or ent.get('kind') or 'signal'
            rate_domain = format_rate_domain(ent.get('rate', ''), ent.get('domain', ''))
            desc = p['meta'].replace('\n', ' ') if p['meta'] else (ent.get('meta', '').replace('\n', ' ') if ent.get('meta') else "—")
            md.append(f"| {icon} | `{p_name}` | `{p_type}` | {p_def_str} | {rate_domain} | {desc} |")
        md.append("")

    # Compact Legend if ports/properties present
    if stream_ports or properties:
        md.append('<div class="port-legend">')
        if stream_ports:
            md.append('  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>')
            md.append('  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>')
        if properties:
            md.append('  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>')
            md.append('  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>')
        md.append('</div>\n')

    # Usage Example
    md.append("## Usage\n")
    md.append("```stride")
    md.append("import Stride;\n")
    prop_args = []
    for p in properties:
        if p['name'] and not p['name'].startswith('_'):
            ent = entity_map.get(p['entity'], {})
            val = p['default'] if p['default'] else ent.get('default', '')
            val_str = val if val else "..."
            prop_args.append(f"{p['name']}: {val_str}")
    args_str = f"({', '.join(prop_args[:3])})" if prop_args else "()"

    if is_root_library:
        md.append(f"# Available in root namespace:")
        md.append(f"Signal >> {name}{args_str} >> Output;")
    else:
        cat = package_name.replace("Stride::", "")
        md.append(f"# Access via {cat} category:")
        md.append(f"Signal >> {cat}::{name}{args_str} >> Output;")
    md.append("```\n")

    return "\n".join(md)


def process_strideroot(strideroot_path: Path, output_docs_dir: Path, git_ref: str = "main") -> List[Dict[str, Any]]:
    """Scans strideroot/library, extracts docs, and writes markdown files with clear Core/Package sidebar distinction."""
    library_dir = strideroot_path / "library" / "1.0"
    if not library_dir.exists():
        print(f"Error: Could not find library directory at {library_dir}")
        return []

    ref_dir = output_docs_dir / "reference" / "library"
    ref_dir.mkdir(parents=True, exist_ok=True)

    core_groups = {}
    core_order = []

    package_groups = {}
    package_order = []

    IGNORED_DIRS = {'doc', '.strdcache', 'tests', 'local'}
    GITHUB_REPO_URL = "https://github.com/StrideLang/strideroot"

    for root, dirs, files in os.walk(library_dir):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS and not d.startswith('.')]

        root_path = Path(root)
        rel_to_lib = root_path.relative_to(library_dir)
        stride_files = sorted([f for f in files if f.endswith(".stride")])

        is_root = (rel_to_lib == Path('.'))

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

            # Filter out declarations starting with '_'
            valid_decls = [
                d for d in parsed['declarations']
                if not d.get('name', '').startswith('_') and d.get('name', '') != 'Anonymous'
            ]

            if not valid_decls:
                continue

            if is_root:
                group_name = file_path.stem
                cat_slug = group_name.lower()
                pkg_name = "Stride"
                if group_name not in core_order:
                    core_order.append(group_name)
                target_dict = core_groups
                group_key = group_name
            else:
                cat_name = rel_to_lib.parts[0]
                group_name = cat_name
                cat_slug = cat_name.lower()
                pkg_name = f"Stride::{cat_name}"
                if cat_name not in package_order:
                    package_order.append(cat_name)
                target_dict = package_groups
                group_key = cat_name

            cat_dir = ref_dir / cat_slug
            cat_dir.mkdir(parents=True, exist_ok=True)

            if group_key not in target_dict:
                target_dict[group_key] = {
                    'slug': cat_slug,
                    'package': pkg_name,
                    'items': []
                }

            rel_unix = str(file_path.relative_to(strideroot_path)).replace("\\", "/")

            for decl in valid_decls:
                decl_name = decl.get('name', '')
                decl_line = decl.get('line', 1)

                github_url = f"{GITHUB_REPO_URL}/blob/{git_ref}/{rel_unix}#L{decl_line}"

                md_content = generate_markdown_for_declaration(
                    decl=decl,
                    package_name=pkg_name,
                    group_name=group_name,
                    file_rel_path=rel_unix,
                    file_basename=file_path.name,
                    github_url=github_url,
                    is_root_library=is_root
                )

                file_slug = decl_name.lower().replace(" ", "-")
                md_filename = f"{file_slug}.md"
                out_file = cat_dir / md_filename
                out_file.write_text(md_content, encoding='utf-8')

                target_dict[group_key]['items'].append({
                    'text': decl_name,
                    'link': f"/reference/library/{cat_slug}/{file_slug}"
                })

    # Build Core Section items
    core_items = []
    for g_key in core_order:
        g_data = core_groups[g_key]
        seen = set()
        deduped = []
        for it in sorted(g_data['items'], key=lambda x: x['text']):
            if it['text'] not in seen:
                seen.add(it['text'])
                deduped.append(it)
        if deduped:
            core_items.append({
                'text': f"{g_key} (Group)",
                'collapsed': False if g_key == 'Math' else True,
                'items': deduped
            })

    # Build Packages Section items
    package_items = []
    for p_key in package_order:
        p_data = package_groups[p_key]
        seen = set()
        deduped = []
        for it in sorted(p_data['items'], key=lambda x: x['text']):
            if it['text'] not in seen:
                seen.add(it['text'])
                deduped.append(it)
        if deduped:
            package_items.append({
                'text': f"Stride::{p_key}",
                'collapsed': False if p_key in ('Generators', 'Filters') else True,
                'items': deduped
            })

    # Structured 2-Tier Sidebar distinguishing Core Groups from Sub-packages
    sidebar_config = [
        {
          'text': "Core Library (Direct Scope)",
          'collapsed': False,
          'items': core_items
        },
        {
          'text': "Packages (Namespaces)",
          'collapsed': False,
          'items': package_items
        }
    ]

    # Generate an Index Page for the Library Reference
    index_md = [
        "---",
        "title: Standard Library Reference",
        "description: Specification of modules, stream processors, filters, generators, and arithmetic operations in the Stride standard library.",
        "---\n",
        "# Standard Library Reference\n",
        "The Stride standard library provides verified primitives for signal flow, multi-rate digital signal processing (DSP), mathematical operations, and state machine transitions.\n",
        "## Source Repository & Versioning\n",
        f"- **Upstream Repository**: [`StrideLang/strideroot`]({GITHUB_REPO_URL})\n",
        f"- **Active Ref**: `{git_ref}` (unambiguous source line links are embedded in each definition)\n",
        "## Namespace Architecture\n",
        "Stride establishes a clear distinction between **Core Library Groups** (which share the root `Stride` namespace) and **Sub-packages** (which form dedicated hierarchical namespaces):\n",
        "### 1. Core Library (Root `Stride` Namespace)\n",
        "Modules defined in root library files reside directly in `package Stride`. They are imported automatically or via `import Stride;` and are called directly in global scope (e.g. `Sin()`, `Sum()`, `Equal()`). In the documentation and navigation sidebar, they are organized into file-based groups for clarity:\n"
    ]

    for g_entry in core_items:
        g_name = g_entry['text']
        items = g_entry['items']
        index_md.append(f"- **{g_name}** ({len(items)} definitions): " + ", ".join(f"[`{it['text']}`]({it['link']})" for it in items[:6]) + ("..." if len(items) > 6 else ""))

    index_md.append("\n### 2. Sub-Packages (Dedicated Namespaces)\n")
    index_md.append("Components residing in library subdirectories form explicit language namespaces (`Stride::<Package>`). When imported via `import Stride;`, they are accessed via category qualification (e.g. `Generators::Oscillator`, `Filters::BiQuad`), or imported directly via `import Stride::Generators;`:\n")

    for p_entry in package_items:
        p_name = p_entry['text']
        items = p_entry['items']
        index_md.append(f"- **`{p_name}`** ({len(items)} definitions): " + ", ".join(f"[`{it['text']}`]({it['link']})" for it in items[:6]) + ("..." if len(items) > 6 else ""))

    index_md.append("\n")
    (ref_dir / "index.md").write_text("\n".join(index_md), encoding='utf-8')

    return sidebar_config


def main():
    parser = argparse.ArgumentParser(description="Stride Documentation Extractor (stride-docgen)")
    parser.add_argument("--strideroot", default=None, help="Path to strideroot repository")
    parser.add_argument("--output", default="docs", help="Target output documentation directory")
    parser.add_argument("--ref", default=os.environ.get("STRIDE_DOCS_GIT_REF", "main"), help="Git ref (branch or tag) for GitHub source links")
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
    print(f"[*] Target branch/ref:    {args.ref}")
    print(f"[*] Output directory:     {output_dir}")

    sidebar = process_strideroot(strideroot_path, output_dir, git_ref=args.ref)

    sidebar_file = output_dir / ".vitepress" / "sidebar-reference.json"
    sidebar_file.parent.mkdir(parents=True, exist_ok=True)
    sidebar_file.write_text(json.dumps(sidebar, indent=2), encoding='utf-8')

    total_core = sum(len(g['items']) for g in sidebar[0]['items'])
    total_pkgs = sum(len(g['items']) for g in sidebar[1]['items'])
    print(f"[+] Successfully extracted {total_core + total_pkgs} definitions!")
    print(f"    - Core Library: {total_core} definitions across {len(sidebar[0]['items'])} groups")
    print(f"    - Sub-packages: {total_pkgs} definitions across {len(sidebar[1]['items'])} namespaces")
    print(f"[+] Sidebar config saved to: {sidebar_file}")


if __name__ == "__main__":
    main()
