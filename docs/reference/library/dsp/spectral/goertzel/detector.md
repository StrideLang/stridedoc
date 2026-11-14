---
title: Detector
description: "Goertzel single-frequency power detector: AudioIn >> Goertzel::Detector(frequency: 440.0) >> TonePower. The frequency is in Hz and is conver"
---

# Detector

<span class="stride-badge">Module</span> `package Dsp::Spectral::Goertzel` &bull; Namespace: **`Dsp::Spectral::Goertzel`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Spectral/Goertzel.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Goertzel.stride:7]</a>

Goertzel single-frequency power detector: AudioIn >> Goertzel::Detector(frequency: 440.0) >> TonePower. The frequency is in Hz and is converted against the rate of the output (the sample rate). Type must be floating point.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `PowerPort.type` | `PowerPort.rate` | `PowerPort.domain` | Audio or sensor input stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `PowerPort` | `PowerPort.type` | `PowerPort.rate` | `PowerPort.domain` | Instantaneous signal power at target frequency |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `PowerPort.type` | `440.0` | — | `PowerPort.domain` | Target tone frequency in Hz to detect |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Spectral::Goertzel as Goertzel;

Signal >> Goertzel::Detector(frequency: 440.0) >> Output;
```
