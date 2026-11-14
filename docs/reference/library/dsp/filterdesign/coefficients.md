---
title: Coefficients
description: "RBJ Audio EQ Cookbook biquad design: Frequency >> FilterDesign::Coefficients(mode: FilterDesign::ModeLowPass q: 0.7071) >> Coeffs. The sampl"
---

# Coefficients

<span class="stride-badge">Module</span> `package Dsp::FilterDesign` &bull; Namespace: **`Dsp::FilterDesign`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/FilterDesign.stride#L34" target="_blank" rel="noopener" title="View source on GitHub">[FilterDesign.stride:34]</a>

RBJ Audio EQ Cookbook biquad design: Frequency >> FilterDesign::Coefficients(mode: FilterDesign::ModeLowPass q: 0.7071) >> Coeffs. The sample rate is the rate of the output; Coeffs is [b0, b1, b2, a1, a2] normalised by a0.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `FrequencyPort` | `CoefficientsPort.type` | `CoefficientsPort.rate` | `CoefficientsPort.domain` | Cutoff, centre or corner frequency in Hz |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `CoefficientsPort` | `CoefficientsPort.type` | `CoefficientsPort.rate` | `CoefficientsPort.domain` | Normalised coefficients [b0, b1, b2, a1, a2] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `mode` | `Int` | `0` | — | `CoefficientsPort.domain` | Filter response: ModeLowPass, ModeHighPass, ModeBandPass, ModeNotch, ModeAllPass or ModePeak (default ModeLowPass) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `q` | `CoefficientsPort.type` | `0.7071` | — | `CoefficientsPort.domain` | Quality factor (default 0.7071, a maximally flat Butterworth response for low-pass and high-pass). Must be greater than 0 |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `gain` | `CoefficientsPort.type` | `0.0` | — | `CoefficientsPort.domain` | Boost (positive) or cut (negative) in dB. Only used by ModePeak (default 0.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::FilterDesign as FilterDesign;

Signal >> FilterDesign::Coefficients(mode: 0, q: 0.7071, gain: 0.0) >> Output;
```
