---
title: Hysteresis
description: "Dual-threshold hysteresis comparator (Schmitt trigger): Input >> Hysteresis(low: 0.2 high: 0.8) >> Output."
---

# Hysteresis

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Hysteresis.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Hysteresis.stride:7]</a>

Dual-threshold hysteresis comparator (Schmitt trigger): Input >> Hysteresis(low: 0.2 high: 0.8) >> Output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Input signal to evaluate |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Binary output state (0.0 or 1.0) |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `low` | `signal` | `0.2` | — | `OutputPort.domain` | Lower switching threshold |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `high` | `signal` | `0.8` | — | `OutputPort.domain` | Upper switching threshold |

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
