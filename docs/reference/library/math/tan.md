---
title: Tan
description: "Tangent function of angle in radians."
---

# Tan

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Math** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L226" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:226]</a>

Tangent function of angle in radians.

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `OutputPort.type` | `OutputPort.rate` / `OutputPort.domain` | Input angle in radians |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `OutputPort.type` | `OutputPort.rate` / `OutputPort.domain` | Tangent of the input angle |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Tan() >> Output;
```
