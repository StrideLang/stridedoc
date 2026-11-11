---
title: Decimator2
description: "2nd-order multiplierless Cascaded Integrator-Comb (CIC) filter: HighRateIn >> Cic::Decimator2() >> Out."
---

# Decimator2

<span class="stride-badge">Module</span> `package Dsp::Filters::Cic` &bull; Namespace: **`Dsp::Filters::Cic`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/Cic.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Cic.stride:8]</a>

2nd-order multiplierless Cascaded Integrator-Comb (CIC) filter: HighRateIn >> Cic::Decimator2() >> Out.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | High-rate input signal stream (e.g., PDM microphone / oversampled ADC) |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Integrator-comb filtered output stream |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Dsp::Filters::Cic as Cic;

Signal >> Cic::Decimator2() >> Output;
```
