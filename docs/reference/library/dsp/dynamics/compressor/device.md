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
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Input audio signal stream |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Compressed audio signal stream |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ threshold</span> <span class="prop-default">= <code>0.5</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Compression threshold in linear amplitude (default 0.5) |
| <span class="port-badge prop-in">↓ ratio</span> <span class="prop-default">= <code>4.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Compression slope ratio (e.g., 4.0 for 4:1) (default 4.0) |
| <span class="port-badge prop-in">↓ makeup</span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Post-compression makeup gain multiplier (default 1.0) |
| <span class="port-badge prop-in">↓ attack</span> <span class="prop-default">= <code>0.01</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Attack time constant of the level detector in seconds (default 0.01) |
| <span class="port-badge prop-in">↓ release</span> <span class="prop-default">= <code>0.1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Release time constant of the level detector in seconds (default 0.1) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Dynamics::Compressor as Compressor;

Signal >> Compressor::Device(threshold: 0.5, ratio: 4.0, makeup: 1.0) >> Output;
```
