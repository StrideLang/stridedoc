---
title: Level
description: "Scales the input signal and applies an offset to it. Formula: output = input * gain + offset"
---

# Level

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Level.stride#L1" target="_blank" rel="noopener" title="View source on GitHub">[Level.stride:1]</a>

Scales the input signal and applies an offset to it.
Formula: output = input * gain + offset

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | — |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | — |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `gain` | `Gain` | — | Amplifies or attenuates the signal. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `offset` | `Offset` | — | Adds an offset to the signal after applying the gain. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Gain` | `signal` | `1.0` | Rate: GainPort.rate, Domain: GainPort.domain | — |
| `Offset` | `signal` | `0.0` | Rate: OffsetPort.rate, Domain: OffsetPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Level(gain: ..., offset: ...) >> Output;
```
