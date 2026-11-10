---
title: Sign
description: "Returns 1.0 if input > 0, -1.0 if input < 0, and 0.0 if input == 0."
---

# Sign

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Math** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L51" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:51]</a>

Returns 1.0 if input > 0, -1.0 if input < 0, and 0.0 if input == 0.

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input value |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Sign of the input (-1.0, 0.0, or 1.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Sign() >> Output;
```
