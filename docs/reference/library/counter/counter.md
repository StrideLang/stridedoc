---
title: Counter
description: "A discrete step counter that increments per tick and rolls over to startValue upon exceeding stopValue."
---

# Counter

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Counter.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[Counter.stride:4]</a>

A discrete step counter that increments per tick and rolls over to startValue upon exceeding stopValue.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Counter output signal |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `startValue` | `StartValue` | — | The starting value of the counter, which is also the first output value. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `stopValue` | `StopValue` | — | The roll value of the counter. The maximum value before resetting to startValue. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `increment` | `Increment` | — | The step value added per tick. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `reset` | `Reset` | — | The counter is reset to startValue when a trigger arrives at the reset port. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `StartValue` | `signal` | `0` | Domain: OutputPort.domain | — |
| `StopValue` | `signal` | `100` | Domain: OutputPort.domain | — |
| `Increment` | `signal` | `1` | Domain: OutputPort.domain | — |
| `Output` | `signal` | `0` | Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Counter(startValue: ..., stopValue: ..., increment: ...) >> Output;
```
