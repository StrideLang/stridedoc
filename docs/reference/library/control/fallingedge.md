---
title: FallingEdge
description: "Detects falling edge (on -> off): Input >> FallingEdge() >> Trigger."
---

# FallingEdge

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Control** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control.stride#L76" target="_blank" rel="noopener" title="View source on GitHub">[Control.stride:76]</a>

Detects falling edge (on -> off): Input >> FallingEdge() >> Trigger.

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `switch` | `OutputPort.rate` / `OutputPort.domain` | Monitored switch signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `switch` | `OutputPort.rate` / `OutputPort.domain` | Switch that is on for one tick when Input transitions from on to off |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> FallingEdge() >> Output;
```
