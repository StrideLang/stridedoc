---
title: Section
description: "Second-order IIR section with explicit normalised coefficients: Input >> Section(coefficients: Coeffs) >> Output. With the default coefficie"
---

# Section

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/Section.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Section.stride:8]</a>

Second-order IIR section with explicit normalised coefficients: Input >> Section(coefficients: Coeffs) >> Output. With the default coefficients [1, 0, 0, 0, 0] the section passes the input unchanged. The data type must be floating point.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Input signal |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Filtered output signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>coefficients</code></span> <span class="prop-default">= <code>[ 1.0 , 0.0 , 0.0 , 0.0 , 0.0 ]</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Normalised coefficients [b0, b1, b2, a1, a2] (a0 = 1), e.g. from FilterDesign::Coefficients |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::Section(coefficients: [ 1.0 , 0.0 , 0.0 , 0.0 , 0.0 ]) >> Output;
```
