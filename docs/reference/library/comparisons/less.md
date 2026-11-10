---
title: Less
description: "Compares two input values: outputs on if Input[0] < Input[1], else off."
---

# Less

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Comparisons** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Comparisons.stride#L60" target="_blank" rel="noopener" title="View source on GitHub">[Comparisons.stride:60]</a>

Compares two input values: outputs on if Input[0] < Input[1], else off.

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `InputPort.type` | `OutputPort.rate` / `OutputPort.domain` | Two-element list with values to compare: [Left, Right] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `switch` | `OutputPort.rate` / `OutputPort.domain` | Switch indicating if Left < Right |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Less() >> Output;
```
