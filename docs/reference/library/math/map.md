---
title: Map
description: "Linearly maps Input from [inMin, inMax] to [outMin, outMax]: Input >> Map(inMin: 0.0 inMax: 1.0 outMin: 100.0 outMax: 1000.0) >> Output."
---

# Map

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L704" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:704]</a>

Linearly maps Input from [inMin, inMax] to [outMin, outMax]: Input >> Map(inMin: 0.0 inMax: 1.0 outMin: 100.0 outMax: 1000.0) >> Output.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Input value to rescale |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Rescaled output value |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `inMin` | `InMin` | — | Source range minimum |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `inMax` | `InMax` | — | Source range maximum |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `outMin` | `OutMin` | — | Target range minimum |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `outMax` | `OutMax` | — | Target range maximum |

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
| `InMin` | `signal` | `0.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `InMax` | `signal` | `1.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `OutMin` | `signal` | `0.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `OutMax` | `signal` | `1.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Norm` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Map(inMin: ..., inMax: ..., outMin: ...) >> Output;
```
