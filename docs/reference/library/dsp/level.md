---
title: Level
description: "Scales the input signal and applies an offset to it. Formula: output = input * gain + offset"
---

# Level

<span class="stride-badge">Module</span> `package Dsp` &bull; Namespace: **`Dsp`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp.stride#L14" target="_blank" rel="noopener" title="View source on GitHub">[Dsp.stride:14]</a>

Scales the input signal and applies an offset to it.
Formula: output = input * gain + offset

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Scaled output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `gain` | `GainPort.type` | `1.0` | `GainPort.rate` | `GainPort.domain` | Amplifies or attenuates the signal. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `offset` | `OffsetPort.type` | `0.0` | `OffsetPort.rate` | `OffsetPort.domain` | Adds an offset to the signal after applying the gain. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp;

Signal >> Level(gain: 1.0, offset: 0.0) >> Output;
```
