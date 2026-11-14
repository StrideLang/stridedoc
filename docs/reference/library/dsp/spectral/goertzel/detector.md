---
title: Detector
description: "Goertzel single-frequency power detector: AudioIn >> Goertzel::Detector(frequency: 440.0) >> TonePower. The frequency is in Hz and is conver"
---

# Detector

<span class="stride-badge">Module</span> `package Dsp::Spectral::Goertzel` &bull; Namespace: **`Dsp::Spectral::Goertzel`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Spectral/Goertzel.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Goertzel.stride:7]</a>

Goertzel single-frequency power detector: AudioIn >> Goertzel::Detector(frequency: 440.0) >> TonePower. The frequency is in Hz and is converted against the rate of the output (the sample rate). Type must be floating point.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» power</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» power</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» power</span></span></div> | Audio or sensor input stream |
| <span class="port-badge stream-out">» power</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» power</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» power</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» power</span></span></div> | Instantaneous signal power at target frequency |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ frequency</span> <span class="prop-default">= <code>440.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» power</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» power</span></span></div> | Target tone frequency in Hz to detect |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import Dsp::Spectral::Goertzel as Goertzel;

Signal >> Goertzel::Detector(frequency: 440.0) >> Output;
```
