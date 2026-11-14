---
title: PeakingEq
description: "Second-order peaking equaliser: Input >> PeakingEq(frequency: 1000.0 q: 1.0 gain: 6.0) >> Output. A BiQuad with FilterDesign::ModePeak; gain"
---

# PeakingEq

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/PeakingEq.stride#L10" target="_blank" rel="noopener" title="View source on GitHub">[PeakingEq.stride:10]</a>

Second-order peaking equaliser: Input >> PeakingEq(frequency: 1000.0 q: 1.0 gain: 6.0) >> Output. A BiQuad with FilterDesign::ModePeak; gain is in dB. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Input signal |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Filtered output signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>frequency</code></span> <span class="prop-default">= <code>1000.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Centre frequency of the band in Hz (default 1000.0) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>q</code></span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Quality factor (default 1.0). Higher values give a narrower band |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>gain</code></span> <span class="prop-default">= <code>6.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Boost (positive) or cut (negative) in dB (default 6.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::PeakingEq(frequency: 1000.0, q: 1.0, gain: 6.0) >> Output;
```
