---
title: BiQuad
description: "Second-order IIR filter with a selectable response (RBJ Audio EQ Cookbook): Input >> BiQuad(mode: FilterDesign::ModeLowPass frequency: 800.0"
---

# BiQuad

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/BiQuad.stride#L10" target="_blank" rel="noopener" title="View source on GitHub">[BiQuad.stride:10]</a>

Second-order IIR filter with a selectable response (RBJ Audio EQ Cookbook): Input >> BiQuad(mode: FilterDesign::ModeLowPass frequency: 800.0 q: 0.7071) >> Output. LowPass, HighPass, BandPass, Notch, AllPass and PeakingEq are shortcuts for the common modes. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Input signal |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Filtered output signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>mode</code></span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>Int</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Response: FilterDesign::ModeLowPass (default), ModeHighPass, ModeBandPass, ModeNotch, ModeAllPass or ModePeak |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>frequency</code></span> <span class="prop-default">= <code>1000.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Cutoff, centre or corner frequency in Hz (default 1000.0) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>q</code></span> <span class="prop-default">= <code>0.7071</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Quality factor (default 0.7071). Must be greater than 0 |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>gain</code></span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Boost or cut in dB, only used by ModePeak (default 0.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::BiQuad(mode: 0, frequency: 1000.0, q: 0.7071) >> Output;
```
