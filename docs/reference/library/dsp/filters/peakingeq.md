---
title: PeakingEq
description: "Second-order peaking equaliser: Input >> PeakingEq(frequency: 1000.0 q: 1.0 gain: 6.0) >> Output. A BiQuad with FilterDesign::ModePeak; gain"
---

# PeakingEq

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/PeakingEq.stride#L10" target="_blank" rel="noopener" title="View source on GitHub">[PeakingEq.stride:10]</a>

Second-order peaking equaliser: Input >> PeakingEq(frequency: 1000.0 q: 1.0 gain: 6.0) >> Output. A BiQuad with FilterDesign::ModePeak; gain is in dB. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Filtered output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `OutputPort.type` | `1000.0` | `OutputPort.rate` | `OutputPort.domain` | Centre frequency of the band in Hz (default 1000.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `q` | `OutputPort.type` | `1.0` | — | `OutputPort.domain` | Quality factor (default 1.0). Higher values give a narrower band |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `gain` | `OutputPort.type` | `6.0` | — | `OutputPort.domain` | Boost (positive) or cut (negative) in dB (default 6.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::PeakingEq(frequency: 1000.0, q: 1.0, gain: 6.0) >> Output;
```
