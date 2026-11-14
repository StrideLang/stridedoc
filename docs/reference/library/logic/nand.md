---
title: Nand
description: "Logical NAND operation on switch inputs: [A, B] >> Nand() >> Out."
---

# Nand

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Logic (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L127" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:127]</a>

Logical NAND operation on switch inputs: [A, B] >> Nand() >> Out.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>switch</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Two-element switch list: [A, B] |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>switch</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Switch output of A NAND B |

## Usage

```stride
# Available in global prelude without import:
Signal >> Nand() >> Output;
```
