---
title: AllPass
description: "Second-order all-pass filter: Input >> AllPass(frequency: 1000.0) >> Output. A BiQuad with FilterDesign::ModeAllPass. The frequency is in Hz"
---

# AllPass

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/AllPass.stride#L10" target="_blank" rel="noopener" title="View source on GitHub">[AllPass.stride:10]</a>

Second-order all-pass filter: Input >> AllPass(frequency: 1000.0) >> Output. A BiQuad with FilterDesign::ModeAllPass. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Filtered output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `OutputPort.type` | `1000.0` | `OutputPort.rate` | `OutputPort.domain` | Frequency at which the phase shift is 180 degrees in Hz (default 1000.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `q` | `OutputPort.type` | `0.7071` | — | `OutputPort.domain` | Quality factor (default 0.7071). Higher values give a sharper phase transition |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::AllPass(frequency: 1000.0, q: 0.7071) >> Output;
```
