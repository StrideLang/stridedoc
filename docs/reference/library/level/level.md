---
title: Level
description: "Scales the input signal and applies an offset to it. Formula: output = input * gain + offset"
---

# Level

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Level** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Level.stride#L1" target="_blank" rel="noopener" title="View source on GitHub">[Level.stride:1]</a>

Scales the input signal and applies an offset to it.
Formula: output = input * gain + offset

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `signal` | — | — | — |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `signal` | — | — | — |

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
import Stride;

# Available in root namespace:
Signal >> Level(gain: 1.0, offset: 0.0) >> Output;
```
