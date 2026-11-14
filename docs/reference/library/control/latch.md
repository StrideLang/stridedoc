---
title: Latch
description: "Sample and hold: samples Input when trigger is on and holds the value when off: Input >> Latch(trigger: Gate) >> Output."
---

# Latch

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Control (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/ControlPrelude.stride#L114" target="_blank" rel="noopener" title="View source on GitHub">[ControlPrelude.stride:114]</a>

Sample and hold: samples Input when trigger is on and holds the value when off: Input >> Latch(trigger: Gate) >> Output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Continuous signal to be sampled and held |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Sampled and held output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `trigger` | `switch` | `off` | `OutputPort.rate` | `OutputPort.domain` | Sample trigger: when on, samples Input; when off, holds previous value |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Latch(trigger: off) >> Output;
```
