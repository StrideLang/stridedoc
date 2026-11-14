---
title: Exit
description: "When input is true, the current domain terminates without executing any further."
---

# Exit

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Domain (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Domain.stride#L191" target="_blank" rel="noopener" title="View source on GitHub">[Domain.stride:191]</a>

When input is true, the current domain terminates without executing any further.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `MainInputPort` | `switch` | — | — | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Exit() >> Output;
```
