---
title: AllOn
description: "Outputs on if all switches in the input array are on: Input >> AllOn() >> Output."
---

# AllOn

<span class="stride-badge">Loop</span> `package Stride` &bull; Group: **Comparisons** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Comparisons.stride#L172" target="_blank" rel="noopener" title="View source on GitHub">[Comparisons.stride:172]</a>

Outputs on if all switches in the input array are on: Input >> AllOn() >> Output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Array of switches to be checked |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Switch that is on only if all input switches are on |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> AllOn() >> Output;
```
