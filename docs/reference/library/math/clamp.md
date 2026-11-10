---
title: Clamp
description: "Constrains input signal between minimum and maximum bounds: Input >> Clamp(min: 0.0 max: 1.0) >> Output."
---

# Clamp

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Math** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L486" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:486]</a>

Constrains input signal between minimum and maximum bounds: Input >> Clamp(min: 0.0 max: 1.0) >> Output.

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal to constrain |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Clamped output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `min` | `OutputPort.type` | `0.0` | `OutputPort.rate` | `OutputPort.domain` | Minimum lower bound |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `max` | `OutputPort.type` | `1.0` | `OutputPort.rate` | `OutputPort.domain` | Maximum upper bound |

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
Signal >> Clamp(min: 0.0, max: 1.0) >> Output;
```
