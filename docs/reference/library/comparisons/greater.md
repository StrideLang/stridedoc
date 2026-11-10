---
title: Greater
description: "Compares two input values: outputs on if Input[0] > Input[1], else off."
---

# Greater

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Comparisons (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Comparisons.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[Comparisons.stride:4]</a>

Compares two input values: outputs on if Input[0] > Input[1], else off.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `InputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Two-element list with values to compare: [Left, Right] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Switch indicating if Left > Right |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Greater() >> Output;
```
