---
title: Hysteresis
description: "Dual-threshold hysteresis comparator (Schmitt trigger) with a switch output: Input >> Hysteresis(low: 0.2 high: 0.8) >> Output. The output k"
---

# Hysteresis

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Hysteresis.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Hysteresis.stride:7]</a>

Dual-threshold hysteresis comparator (Schmitt trigger) with a switch output: Input >> Hysteresis(low: 0.2 high: 0.8) >> Output. The output keeps its state while the input is between the two thresholds.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `InputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal to evaluate |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Switch: turns on when the input reaches the high threshold and off when it falls to the low threshold |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `low` | `InputPort.type` | `0.2` | — | `OutputPort.domain` | Lower switching threshold (default 0.2) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `high` | `InputPort.type` | `0.8` | — | `OutputPort.domain` | Upper switching threshold (default 0.8) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Control;

Signal >> Hysteresis(low: 0.2, high: 0.8) >> Output;
```
