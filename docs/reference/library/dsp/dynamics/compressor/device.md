---
title: Device
description: "Feedforward dynamic range compressor: AudioIn >> Compressor::Device(threshold: 0.5 ratio: 4.0 makeup: 1.2 attack: 0.01 release: 0.1) >> Out."
---

# Device

<span class="stride-badge">Module</span> `package Dsp::Dynamics::Compressor` &bull; Namespace: **`Dsp::Dynamics::Compressor`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Dynamics/Compressor.stride#L10" target="_blank" rel="noopener" title="View source on GitHub">[Compressor.stride:10]</a>

Feedforward dynamic range compressor: AudioIn >> Compressor::Device(threshold: 0.5 ratio: 4.0 makeup: 1.2 attack: 0.01 release: 0.1) >> Out. Attack and release are times in seconds, converted against the rate of the output.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Input audio signal stream |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Compressed audio signal stream |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>threshold</code></span> <span class="prop-default">= <code>0.5</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Compression threshold in linear amplitude (default 0.5) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>ratio</code></span> <span class="prop-default">= <code>4.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Compression slope ratio (e.g., 4.0 for 4:1) (default 4.0) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>makeup</code></span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Post-compression makeup gain multiplier (default 1.0) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>attack</code></span> <span class="prop-default">= <code>0.01</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Attack time constant of the level detector in seconds (default 0.01) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>release</code></span> <span class="prop-default">= <code>0.1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Release time constant of the level detector in seconds (default 0.1) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Dynamics::Compressor as Compressor;

Signal >> Compressor::Device(threshold: 0.5, ratio: 4.0, makeup: 1.0) >> Output;
```
