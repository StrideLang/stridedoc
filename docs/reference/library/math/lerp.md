---
title: Lerp
description: "Linearly interpolates from Input to Target based on factor: Input >> Lerp(target: Target factor: 0.5) >> Output."
---

# Lerp

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L653" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:653]</a>

Linearly interpolates from Input to Target based on factor: Input >> Lerp(target: Target factor: 0.5) >> Output.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Base input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Interpolated output signal |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `target` | `Target` | — | Target signal to blend towards |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `factor` | `Factor` | — | Blend factor from 0.0 (Input) to 1.0 (Target) |

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
| `Target` | `signal` | `0.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Factor` | `signal` | `0.5` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Lerp(target: ..., factor: ...) >> Output;
```
