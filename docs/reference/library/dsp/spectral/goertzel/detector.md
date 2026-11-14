---
title: Detector
description: "Goertzel single-frequency power detector: AudioIn >> Goertzel::Detector(frequency: 440.0) >> TonePower. The frequency is in Hz and is conver"
---

# Detector

<span class="stride-badge">Module</span> `package Dsp::Spectral::Goertzel` &bull; Namespace: **`Dsp::Spectral::Goertzel`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Spectral/Goertzel.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Goertzel.stride:7]</a>

Goertzel single-frequency power detector: AudioIn >> Goertzel::Detector(frequency: 440.0) >> TonePower. The frequency is in Hz and is converted against the rate of the output (the sample rate). Type must be floating point.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>PowerPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>PowerPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>PowerPort.domain</code></span></div> | Audio or sensor input stream |
| <span class="port-badge stream-out">» Out</span> | `PowerPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>PowerPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>PowerPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>PowerPort.domain</code></span></div> | Instantaneous signal power at target frequency |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>frequency</code></span> <span class="prop-default">= <code>440.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>PowerPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>PowerPort.domain</code></span></div> | Target tone frequency in Hz to detect |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Spectral::Goertzel as Goertzel;

Signal >> Goertzel::Detector(frequency: 440.0) >> Output;
```
