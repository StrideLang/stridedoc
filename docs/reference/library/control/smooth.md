---
title: Smooth
description: "Exponential (one-pole low-pass) smoothing of Input with a time constant in seconds: Input >> Smooth(time: 0.05) >> Output. The time is conve"
---

# Smooth

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Control (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/ControlPrelude.stride#L160" target="_blank" rel="noopener" title="View source on GitHub">[ControlPrelude.stride:160]</a>

Exponential (one-pole low-pass) smoothing of Input with a time constant in seconds: Input >> Smooth(time: 0.05) >> Output. The time is converted with the rate of the output, so it is independent of the sample rate. Type must be a floating point type.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Signal to be smoothed |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Smoothed output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `time` | `OutputPort.type` | `0.01` | — | `OutputPort.domain` | Time constant in seconds: the time the output takes to cover 63% of a step in the input. 0 disables smoothing. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Smooth(time: 0.01) >> Output;
```
