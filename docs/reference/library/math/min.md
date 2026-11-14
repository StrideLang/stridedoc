---
title: Min
description: "Returns the minimum of two input values in a list: [A, B] >> Min() >> Out."
---

# Min

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Math (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/MathPrelude.stride#L438" target="_blank" rel="noopener" title="View source on GitHub">[MathPrelude.stride:438]</a>

Returns the minimum of two input values in a list: [A, B] >> Min() >> Out.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Two-element input list to compare: [A, B] |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | The minimum value |

## Usage

```stride
# Available in global prelude without import:
Signal >> Min() >> Output;
```
