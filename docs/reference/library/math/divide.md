---
title: Divide
description: "Divides Input[0] by Input[1]."
---

# Divide

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L271" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:271]</a>

Divides Input[0] by Input[1].

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Two-element input list: [Numerator, Denominator] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | The quotient of the division |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input[2]` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | Input values |
| `Output` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | Result of the division |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Divide() >> Output;
```
