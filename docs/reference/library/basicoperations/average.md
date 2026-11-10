---
title: Average
description: "Computes the arithmetic mean of all signals in the input array: Input >> Average() >> Output."
---

# Average

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **BasicOperations** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/BasicOperations.stride#L50" target="_blank" rel="noopener" title="View source on GitHub">[BasicOperations.stride:50]</a>

Computes the arithmetic mean of all signals in the input array: Input >> Average() >> Output.

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Array of signals to be averaged |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Arithmetic mean of all signals in the array |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Average() >> Output;
```
