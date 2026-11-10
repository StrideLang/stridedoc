---
title: BandPass
description: "Bandpass filter."
---

# BandPass

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/BandPass.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[BandPass.stride:7]</a>

Bandpass filter.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | — | `InputPort.domain` | Input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | `OutputPort.domain` | Bandpass filtered output |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `centerFrequency` | `signal` | `1000.0` | — | — | The center frequency of the filter. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `qFactor` | `signal` | `1.0` | — | — | The Q value of the filter. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `gain` | `signal` | `1.0` | — | — | Filter gain. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::BandPass(centerFrequency: 1000.0, qFactor: 1.0, gain: 1.0) >> Output;
```
