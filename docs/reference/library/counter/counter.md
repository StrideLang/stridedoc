---
title: Counter
description: "A discrete step counter that increments per tick and rolls over to startValue upon exceeding stopValue."
---

# Counter

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Counter** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Counter.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[Counter.stride:4]</a>

A discrete step counter that increments per tick and rolls over to startValue upon exceeding stopValue.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | `OutputPort.domain` | Counter output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `startValue` | `signal` | `0` | — | `OutputPort.domain` | The starting value of the counter, which is also the first output value. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `stopValue` | `signal` | `100` | — | `OutputPort.domain` | The roll value of the counter. The maximum value before resetting to startValue. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `increment` | `signal` | `1` | — | `OutputPort.domain` | The step value added per tick. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `reset` | `trigger` | — | — | `OutputPort.domain` | The counter is reset to startValue when a trigger arrives at the reset port. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Counter(startValue: 0, stopValue: 100, increment: 1) >> Output;
```
