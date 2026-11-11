---
title: Detector
description: "Goertzel single-frequency power detector: AudioIn >> Goertzel::Detector(frequency: 440.0) >> TonePower."
---

# Detector

<span class="stride-badge">Module</span> `package Dsp::Spectral::Goertzel` &bull; Namespace: **`Dsp::Spectral::Goertzel`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Spectral/Goertzel.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Goertzel.stride:7]</a>

Goertzel single-frequency power detector: AudioIn >> Goertzel::Detector(frequency: 440.0) >> TonePower.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `PowerPort.rate` | `PowerPort.domain` | Audio or sensor input stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `PowerPort` | `signal` | `PowerPort.rate` | `PowerPort.domain` | Instantaneous signal power at target frequency |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `signal` | `440.0` | — | `PowerPort.domain` | Target tone frequency in Hz to detect |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `sampleRate` | `signal` | `44100.0` | — | `PowerPort.domain` | Sample rate in Hz (default 44100.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Spectral::Goertzel as Goertzel;

Signal >> Goertzel::Detector(frequency: 440.0, sampleRate: 44100.0) >> Output;
```
