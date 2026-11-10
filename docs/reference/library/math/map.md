---
title: Map
description: "Linearly maps Input from [inMin, inMax] to [outMin, outMax]: Input >> Map(inMin: 0.0 inMax: 1.0 outMin: 100.0 outMax: 1000.0) >> Output."
---

# Map

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Math** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L704" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:704]</a>

Linearly maps Input from [inMin, inMax] to [outMin, outMax]: Input >> Map(inMin: 0.0 inMax: 1.0 outMin: 100.0 outMax: 1000.0) >> Output.

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `OutputPort.type` | `OutputPort.rate` / `OutputPort.domain` | Input value to rescale |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `OutputPort.type` | `OutputPort.rate` / `OutputPort.domain` | Rescaled output value |

## Properties

| | Property | Type | Default | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `inMin` | `OutputPort.type` | `0.0` | `OutputPort.rate` / `OutputPort.domain` | Source range minimum |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `inMax` | `OutputPort.type` | `1.0` | `OutputPort.rate` / `OutputPort.domain` | Source range maximum |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `outMin` | `OutputPort.type` | `0.0` | `OutputPort.rate` / `OutputPort.domain` | Target range minimum |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `outMax` | `OutputPort.type` | `1.0` | `OutputPort.rate` / `OutputPort.domain` | Target range maximum |

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
Signal >> Map(inMin: 0.0, inMax: 1.0, outMin: 0.0) >> Output;
```
