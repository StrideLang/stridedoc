---
title: Floor
description: "Returns input value rounded down to the nearest integer."
---

# Floor

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Math** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L543" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:543]</a>

Returns input value rounded down to the nearest integer.

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Floating point number input |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Largest integer value less than or equal to input |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Floor() >> Output;
```
