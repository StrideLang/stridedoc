---
title: Fir7
description: "Efficient 7-tap halfband FIR filter with 50% zero-tap reduction: AudioIn >> Halfband::Fir7() >> Out."
---

# Fir7

<span class="stride-badge">Module</span> `package Dsp::Filters::Halfband` &bull; Namespace: **`Dsp::Filters::Halfband`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/Halfband.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Halfband.stride:8]</a>

Efficient 7-tap halfband FIR filter with 50% zero-tap reduction: AudioIn >> Halfband::Fir7() >> Out.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Input audio signal stream |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Filtered halfband audio signal stream |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Filters::Halfband as Halfband;

Signal >> Halfband::Fir7() >> Output;
```
