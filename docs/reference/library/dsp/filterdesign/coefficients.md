---
title: Coefficients
description: "RBJ Audio EQ Cookbook biquad design: Frequency >> FilterDesign::Coefficients(mode: FilterDesign::ModeLowPass q: 0.7071) >> Coeffs. The sampl"
---

# Coefficients

<span class="stride-badge">Module</span> `package Dsp::FilterDesign` &bull; Namespace: **`Dsp::FilterDesign`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/FilterDesign.stride#L34" target="_blank" rel="noopener" title="View source on GitHub">[FilterDesign.stride:34]</a>

RBJ Audio EQ Cookbook biquad design: Frequency >> FilterDesign::Coefficients(mode: FilterDesign::ModeLowPass q: 0.7071) >> Coeffs. The sample rate is the rate of the output; Coeffs is [b0, b1, b2, a1, a2] normalised by a0.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» frequency</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» coefficients</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» coefficients</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» coefficients</span></span></div> | Cutoff, centre or corner frequency in Hz |
| <span class="port-badge stream-out">» coefficients</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» coefficients</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» coefficients</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» coefficients</span></span></div> | Normalised coefficients [b0, b1, b2, a1, a2] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge stream-in">» In</span> Stream Input</span>
  <span class="port-legend-item"><span class="port-badge stream-out">» Out</span> Stream Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ mode</span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>Int</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» coefficients</span></span></div> | Filter response: ModeLowPass, ModeHighPass, ModeBandPass, ModeNotch, ModeAllPass or ModePeak (default ModeLowPass) |
| <span class="port-badge prop-in">↓ q</span> <span class="prop-default">= <code>0.7071</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» coefficients</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» coefficients</span></span></div> | Quality factor (default 0.7071, a maximally flat Butterworth response for low-pass and high-pass). Must be greater than 0 |
| <span class="port-badge prop-in">↓ gain</span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» coefficients</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» coefficients</span></span></div> | Boost (positive) or cut (negative) in dB. Only used by ModePeak (default 0.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import Dsp::FilterDesign as FilterDesign;

Signal >> FilterDesign::Coefficients(mode: 0, q: 0.7071, gain: 0.0) >> Output;
```
