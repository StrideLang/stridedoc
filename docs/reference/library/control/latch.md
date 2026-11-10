---
title: Latch
description: "Sample and hold: samples Input when trigger is on and holds the value when off: Input >> Latch(trigger: Gate) >> Output."
---

# Latch

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Control** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control.stride#L114" target="_blank" rel="noopener" title="View source on GitHub">[Control.stride:114]</a>

Sample and hold: samples Input when trigger is on and holds the value when off: Input >> Latch(trigger: Gate) >> Output.

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `OutputPort.type` | `OutputPort.rate` / `OutputPort.domain` | Continuous signal to be sampled and held |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `OutputPort.type` | `OutputPort.rate` / `OutputPort.domain` | Sampled and held output signal |

## Properties

| | Property | Type | Default | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `trigger` | `switch` | `off` | `OutputPort.rate` / `OutputPort.domain` | Sample trigger: when on, samples Input; when off, holds previous value |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Latch(trigger: off) >> Output;
```
