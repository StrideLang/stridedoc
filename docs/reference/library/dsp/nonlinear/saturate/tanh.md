---
title: Tanh
description: "Padé rational approximation of tanh(x) soft saturation: AudioIn >> Saturate::Tanh() >> Out."
---

# Tanh

<span class="stride-badge">Module</span> `package Dsp::Nonlinear::Saturate` &bull; Namespace: **`Dsp::Nonlinear::Saturate`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Nonlinear/Saturate.stride#L50" target="_blank" rel="noopener" title="View source on GitHub">[Saturate.stride:50]</a>

Padé rational approximation of tanh(x) soft saturation: AudioIn >> Saturate::Tanh() >> Out.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Input audio signal stream |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Tanh-saturated output signal stream in [-1.0, 1.0] |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Nonlinear::Saturate as Saturate;

Signal >> Saturate::Tanh() >> Output;
```
