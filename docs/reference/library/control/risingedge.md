---
title: RisingEdge
description: "Detects rising edge (off -> on): Input >> RisingEdge() >> Trigger."
---

# RisingEdge

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control.stride#L38" target="_blank" rel="noopener" title="View source on GitHub">[Control.stride:38]</a>

Detects rising edge (off -> on): Input >> RisingEdge() >> Trigger.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Monitored switch signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Switch that is on for one tick when Input transitions from off to on |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `switch` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Output` | `switch` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Prev` | `switch` | `off` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `NotPrev` | `switch` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> RisingEdge() >> Output;
```
