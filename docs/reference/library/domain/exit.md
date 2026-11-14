---
title: Exit
description: "When input is true, the current domain terminates without executing any further."
---

# Exit

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Domain (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Domain.stride#L191" target="_blank" rel="noopener" title="View source on GitHub">[Domain.stride:191]</a>

When input is true, the current domain terminates without executing any further.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» MainInputPort</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>switch</code></span></div> | — |

## Usage

```stride
# Available in global prelude without import:
Signal >> Exit() >> Output;
```
