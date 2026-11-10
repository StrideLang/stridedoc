---
title: Clamp
description: "Constrains input signal between minimum and maximum bounds: Input >> Clamp(min: 0.0 max: 1.0) >> Output."
---

# Clamp

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L486" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:486]</a>

Constrains input signal between minimum and maximum bounds: Input >> Clamp(min: 0.0 max: 1.0) >> Output.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Input signal to constrain |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Clamped output signal |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `min` | `MinVal` | — | Minimum lower bound |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `max` | `MaxVal` | — | Maximum upper bound |

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
| `MinVal` | `signal` | `0.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `MaxVal` | `signal` | `1.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Temp` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Clamp(min: ..., max: ...) >> Output;
```
