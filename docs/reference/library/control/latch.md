---
title: Latch
description: "Sample and hold: samples Input when trigger is on and holds the value when off: Input >> Latch(trigger: Gate) >> Output."
---

# Latch

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control.stride#L114" target="_blank" rel="noopener" title="View source on GitHub">[Control.stride:114]</a>

Sample and hold: samples Input when trigger is on and holds the value when off: Input >> Latch(trigger: Gate) >> Output.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Continuous signal to be sampled and held |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Sampled and held output signal |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `trigger` | `Trigger` | — | Sample trigger: when on, samples Input; when off, holds previous value |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Output` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Trigger` | `switch` | `off` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Held` | `signal` | `0.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Latch(trigger: ...) >> Output;
```
