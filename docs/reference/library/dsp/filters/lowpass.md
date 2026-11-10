---
title: LowPass
description: "Lowpass filter."
---

# LowPass

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/LowPass.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[LowPass.stride:7]</a>

Lowpass filter.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | — | `InputPort.domain` | Input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | `OutputPort.domain` | Filtered output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `signal` | `1000.0` | — | — | The cutoff frequency of the filter. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `qFactor` | `signal` | `0.7071` | — | — | The Q value of the filter. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `gain` | `signal` | `1.0` | — | — | Filter passband gain. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::LowPass(frequency: 1000.0, qFactor: 0.7071, gain: 1.0) >> Output;
```
