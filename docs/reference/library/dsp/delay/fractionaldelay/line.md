---
title: Line
description: "Ring-buffer fractional delay line with linear interpolation: AudioIn >> FractionalDelay::Line(delay: 0.0025) >> DelayedOut. The delay is in "
---

# Line

<span class="stride-badge">Module</span> `package Dsp::Delay::FractionalDelay` &bull; Namespace: **`Dsp::Delay::FractionalDelay`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Delay/FractionalDelay.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[FractionalDelay.stride:8]</a>

Ring-buffer fractional delay line with linear interpolation: AudioIn >> FractionalDelay::Line(delay: 0.0025) >> DelayedOut. The delay is in seconds, converted against the rate of the output, up to 4096 samples (4096 / rate seconds).

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Input audio signal stream |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Delayed audio signal stream |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>delay</code></span> <span class="prop-default">= <code>0.002</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Delay time in seconds, converted to samples with the rate of the output. Limited to the buffer size (4096 samples) (default 0.002) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Delay::FractionalDelay as FractionalDelay;

Signal >> FractionalDelay::Line(delay: 0.002) >> Output;
```
