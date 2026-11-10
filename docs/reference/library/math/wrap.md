---
title: Wrap
description: "Periodically wraps input signal within [min, max): Input >> Wrap(min: 0.0 max: 1.0) >> Output."
---

# Wrap

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Math (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L557" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:557]</a>

Periodically wraps input signal within [min, max): Input >> Wrap(min: 0.0 max: 1.0) >> Output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal to wrap |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Wrapped output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `min` | `OutputPort.type` | `0.0` | `OutputPort.rate` | `OutputPort.domain` | Range lower bound |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `max` | `OutputPort.type` | `1.0` | `OutputPort.rate` | `OutputPort.domain` | Range upper bound |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Wrap(min: 0.0, max: 1.0) >> Output;
```
