---
title: Clip
description: "Limits signal within minimum and maximum values: Input >> Clip(minimum: 0.0 maximum: 1.0) >> Output."
---

# Clip

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/BasicOperations.stride#L85" target="_blank" rel="noopener" title="View source on GitHub">[BasicOperations.stride:85]</a>

Limits signal within minimum and maximum values: Input >> Clip(minimum: 0.0 maximum: 1.0) >> Output.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Input signal to constrain |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Clipped output signal |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `minimum` | `MinVal` | — | Lower bound |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `maximum` | `MaxVal` | — | Upper bound |

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

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Clip(minimum: ..., maximum: ...) >> Output;
```
