---
title: OnChange
description: "Detects changes in a signal: outputs on when Input differs from previous tick: Input >> OnChange() >> Trigger."
---

# OnChange

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[Control.stride:4]</a>

Detects changes in a signal: outputs on when Input differs from previous tick: Input >> OnChange() >> Trigger.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Signal or switch being monitored for changes |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Switch that is on when Input changed from its previous tick value |

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
| `Output` | `switch` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Prev` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> OnChange() >> Output;
```
