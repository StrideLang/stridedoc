---
title: Decimator2
description: "2nd-order multiplierless Cascaded Integrator-Comb (CIC) filter: HighRateIn >> Cic::Decimator2() >> Out."
---

# Decimator2

<span class="stride-badge">Module</span> `package Dsp::Filters::Cic` &bull; Namespace: **`Dsp::Filters::Cic`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/Cic.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Cic.stride:8]</a>

2nd-order multiplierless Cascaded Integrator-Comb (CIC) filter: HighRateIn >> Cic::Decimator2() >> Out.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | High-rate input signal stream (e.g., PDM microphone / oversampled ADC) |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Integrator-comb filtered output stream |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Filters::Cic as Cic;

Signal >> Cic::Decimator2() >> Output;
```
