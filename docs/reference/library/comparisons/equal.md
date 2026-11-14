---
title: Equal
description: "Compares two input values: outputs on if Input[0] == Input[1], else off."
---

# Equal

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Comparisons (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Comparisons.stride#L116" target="_blank" rel="noopener" title="View source on GitHub">[Comparisons.stride:116]</a>

Compares two input values: outputs on if Input[0] == Input[1], else off.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-in">» In</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Two-element list with values to compare: [Left, Right] |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>switch</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Switch indicating if Left == Right |

## Usage

```stride
# Available in global prelude without import:
Signal >> Equal() >> Output;
```
