---
title: Sum
description: "Adds all signals in the input array: Input >> Sum() >> Output."
---

# Sum

<span class="stride-badge">Loop</span> Global Prelude &bull; Group: **BasicOperations (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/BasicOperations.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[BasicOperations.stride:4]</a>

Adds all signals in the input array: Input >> Sum() >> Output.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Array of signals to be summed |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | The sum of all signals in the array |

## Usage

```stride
# Available in global prelude without import:
Signal >> Sum() >> Output;
```
