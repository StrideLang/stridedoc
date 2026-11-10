---
title: HighPassCoefficients
description: "Designs RBJ 2nd-order highpass filter coefficients."
---

# HighPassCoefficients

<span class="stride-badge">Module</span> `package Dsp::FilterDesign` &bull; Namespace: **`Dsp::FilterDesign`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/FilterDesign.stride#L69" target="_blank" rel="noopener" title="View source on GitHub">[FilterDesign.stride:69]</a>

Designs RBJ 2nd-order highpass filter coefficients.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `FreqPort` | `signal` | — | `FreqPort.domain` | Cutoff frequency in Hz |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `BCoeffsPort` | `signal` | — | `BCoeffsPort.domain` | Feedforward numerator coefficients [b0, b1, b2] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `ACoeffsPort` | `signal` | — | `ACoeffsPort.domain` | Feedback denominator coefficients [a1, a2] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `q` | `signal` | `0.7071` | — | `QPort.domain` | Quality factor Q (default 0.7071 / Butterworth) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `sampleRate` | `signal` | `44100.0` | — | `RatePort.domain` | Sample rate in Hz (default 44100.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::FilterDesign as FilterDesign;

Signal >> FilterDesign::HighPassCoefficients(q: 0.7071, sampleRate: 44100.0) >> Output;
```
