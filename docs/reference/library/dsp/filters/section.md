---
title: Section
description: "Second-order IIR section with explicit normalised coefficients: Input >> Section(coefficients: Coeffs) >> Output. With the default coefficie"
---

# Section

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/Section.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Section.stride:8]</a>

Second-order IIR section with explicit normalised coefficients: Input >> Section(coefficients: Coeffs) >> Output. With the default coefficients [1, 0, 0, 0, 0] the section passes the input unchanged. The data type must be floating point.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Filtered output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `coefficients` | `OutputPort.type` | `[ 1.0 , 0.0 , 0.0 , 0.0 , 0.0 ]` | — | `OutputPort.domain` | Normalised coefficients [b0, b1, b2, a1, a2] (a0 = 1), e.g. from FilterDesign::Coefficients |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::Section(coefficients: [ 1.0 , 0.0 , 0.0 , 0.0 , 0.0 ]) >> Output;
```
