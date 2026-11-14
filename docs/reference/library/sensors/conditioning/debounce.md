---
title: Debounce
description: "Suppresses mechanical switch bounce: RawButton >> Debounce(time: 0.01) >> CleanButton. The output follows the input once it has been differe"
---

# Debounce

<span class="stride-badge">Module</span> `package Sensors::Conditioning` &bull; Namespace: **`Sensors::Conditioning`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Sensors/Conditioning.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Conditioning.stride:8]</a>

Suppresses mechanical switch bounce: RawButton >> Debounce(time: 0.01) >> CleanButton. The output follows the input once it has been different for the given time in seconds, converted against the rate of the output.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>switch</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Raw digital input switch |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>switch</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Debounced output switch |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>time</code></span> <span class="prop-default">= <code>0.01</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>Real</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Time in seconds the input must stay different from the output before the output follows it (default 0.01) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Sensors::Conditioning as Conditioning;

Signal >> Conditioning::Debounce(time: 0.01) >> Output;
```
