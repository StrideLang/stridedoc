---
title: Greater
description: "Compares two input values: outputs on if Input[0] > Input[1], else off."
---

# Greater

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Comparisons.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[Comparisons.stride:4]</a>

Compares two input values: outputs on if Input[0] > Input[1], else off.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Two-element list with values to compare: [Left, Right] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Switch indicating if Left > Right |

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
| `Output` | `switch` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Greater() >> Output;
```
