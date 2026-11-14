---
title: Line
description: "Ring-buffer fractional delay line with linear interpolation: AudioIn >> FractionalDelay::Line(delay: 0.0025) >> DelayedOut. The delay is in "
---

# Line

<span class="stride-badge">Module</span> `package Dsp::Delay::FractionalDelay` &bull; Namespace: **`Dsp::Delay::FractionalDelay`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Delay/FractionalDelay.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[FractionalDelay.stride:8]</a>

Ring-buffer fractional delay line with linear interpolation: AudioIn >> FractionalDelay::Line(delay: 0.0025) >> DelayedOut. The delay is in seconds, converted against the rate of the output, up to 4096 samples (4096 / rate seconds).

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input audio signal stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Delayed audio signal stream |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `delay` | `OutputPort.type` | `0.002` | — | `OutputPort.domain` | Delay time in seconds, converted to samples with the rate of the output. Limited to the buffer size (4096 samples) (default 0.002) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Delay::FractionalDelay as FractionalDelay;

Signal >> FractionalDelay::Line(delay: 0.002) >> Output;
```
