---
title: Sum
description: "Adds all signals in the input array: Input >> Sum() >> Output."
---

# Sum

<span class="stride-badge">Loop</span> `package Stride` &bull; Group: **BasicOperations** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/BasicOperations.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[BasicOperations.stride:4]</a>

Adds all signals in the input array: Input >> Sum() >> Output.

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Sum_Input` | `OutputPort.type` | `OutputPort.rate` / `OutputPort.domain` | Array of signals to be summed |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Sum_Output` | `OutputPort.type` | `OutputPort.rate` / `OutputPort.domain` | The sum of all signals in the array |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Sum() >> Output;
```
