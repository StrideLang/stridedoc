---
title: Fast
description: "Hard peak clamping limiter: AudioIn >> Limiter::Fast(threshold: 0.95) >> Out."
---

# Fast

<span class="stride-badge">Module</span> `package Dsp::Dynamics::Limiter` &bull; Namespace: **`Dsp::Dynamics::Limiter`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Dynamics/Limiter.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Limiter.stride:8]</a>

Hard peak clamping limiter: AudioIn >> Limiter::Fast(threshold: 0.95) >> Out.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Input audio signal stream |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Peak-limited audio signal stream |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>threshold</code></span> <span class="prop-default">= <code>0.95</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Maximum peak ceiling amplitude (default 0.95) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Dynamics::Limiter as Limiter;

Signal >> Limiter::Fast(threshold: 0.95) >> Output;
```
