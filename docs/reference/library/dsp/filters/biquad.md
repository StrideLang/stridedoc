---
title: BiQuad
description: "Second-order IIR filter with a selectable response (RBJ Audio EQ Cookbook): Input >> BiQuad(mode: FilterDesign::ModeLowPass frequency: 800.0"
---

# BiQuad

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/BiQuad.stride#L10" target="_blank" rel="noopener" title="View source on GitHub">[BiQuad.stride:10]</a>

Second-order IIR filter with a selectable response (RBJ Audio EQ Cookbook): Input >> BiQuad(mode: FilterDesign::ModeLowPass frequency: 800.0 q: 0.7071) >> Output. LowPass, HighPass, BandPass, Notch, AllPass and PeakingEq are shortcuts for the common modes. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Filtered output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `mode` | `Int` | `0` | — | `OutputPort.domain` | Response: FilterDesign::ModeLowPass (default), ModeHighPass, ModeBandPass, ModeNotch, ModeAllPass or ModePeak |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `OutputPort.type` | `1000.0` | `OutputPort.rate` | `OutputPort.domain` | Cutoff, centre or corner frequency in Hz (default 1000.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `q` | `OutputPort.type` | `0.7071` | — | `OutputPort.domain` | Quality factor (default 0.7071). Must be greater than 0 |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `gain` | `OutputPort.type` | `0.0` | — | `OutputPort.domain` | Boost or cut in dB, only used by ModePeak (default 0.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::BiQuad(mode: 0, frequency: 1000.0, q: 0.7071) >> Output;
```
