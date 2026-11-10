---
title: Multiply
description: "Multiplies Input[0] by Input[1]."
---

# Multiply

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L302" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:302]</a>

Multiplies Input[0] by Input[1].

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Two-element input list: [FactorA, FactorB] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | The product of the multiplication |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input[2]` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Output` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Multiply() >> Output;
```
