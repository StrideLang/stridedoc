---
title: Wrap
description: "Periodically wraps input signal within [min, max): Input >> Wrap(min: 0.0 max: 1.0) >> Output."
---

# Wrap

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L572" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:572]</a>

Periodically wraps input signal within [min, max): Input >> Wrap(min: 0.0 max: 1.0) >> Output.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Input signal to wrap |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Wrapped output signal |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `min` | `MinVal` | — | Range lower bound |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `max` | `MaxVal` | — | Range upper bound |

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
| `Range` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Offset` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `ModVal` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Quo` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Fl` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Wrap(min: ..., max: ...) >> Output;
```
