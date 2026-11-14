---
title: BandPass
description: "Second-order band-pass filter: Input >> BandPass(frequency: 1000.0 q: 2.0) >> Output. A BiQuad with FilterDesign::ModeBandPass. The frequenc"
---

# BandPass

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/BandPass.stride#L10" target="_blank" rel="noopener" title="View source on GitHub">[BandPass.stride:10]</a>

Second-order band-pass filter: Input >> BandPass(frequency: 1000.0 q: 2.0) >> Output. A BiQuad with FilterDesign::ModeBandPass. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Filtered output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `OutputPort.type` | `1000.0` | `OutputPort.rate` | `OutputPort.domain` | Centre frequency in Hz (default 1000.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `q` | `OutputPort.type` | `1.0` | — | `OutputPort.domain` | Quality factor (default 1.0). Bandwidth in octaves is about 1.44 / q: higher values give a narrower band |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::BandPass(frequency: 1000.0, q: 1.0) >> Output;
```
