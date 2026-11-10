---
title: OnChange
description: "Detects changes in a signal: outputs on when Input differs from previous tick: Input >> OnChange() >> Trigger."
---

# OnChange

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Control** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[Control.stride:4]</a>

Detects changes in a signal: outputs on when Input differs from previous tick: Input >> OnChange() >> Trigger.

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `InputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Signal or switch being monitored for changes |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Switch that is on when Input changed from its previous tick value |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> OnChange() >> Output;
```
