---
title: Device
description: "Feedforward dynamic range compressor: AudioIn >> Compressor::Device(threshold: 0.5 ratio: 4.0 makeup: 1.2 attack: 0.01 release: 0.1) >> Out."
---

# Device

<span class="stride-badge">Module</span> `package Dsp::Dynamics::Compressor` &bull; Namespace: **`Dsp::Dynamics::Compressor`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Dynamics/Compressor.stride#L10" target="_blank" rel="noopener" title="View source on GitHub">[Compressor.stride:10]</a>

Feedforward dynamic range compressor: AudioIn >> Compressor::Device(threshold: 0.5 ratio: 4.0 makeup: 1.2 attack: 0.01 release: 0.1) >> Out. Attack and release are times in seconds, converted against the rate of the output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input audio signal stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Compressed audio signal stream |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `threshold` | `OutputPort.type` | `0.5` | — | `OutputPort.domain` | Compression threshold in linear amplitude (default 0.5) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `ratio` | `OutputPort.type` | `4.0` | — | `OutputPort.domain` | Compression slope ratio (e.g., 4.0 for 4:1) (default 4.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `makeup` | `OutputPort.type` | `1.0` | — | `OutputPort.domain` | Post-compression makeup gain multiplier (default 1.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `attack` | `OutputPort.type` | `0.01` | — | `OutputPort.domain` | Attack time constant of the level detector in seconds (default 0.01) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `release` | `OutputPort.type` | `0.1` | — | `OutputPort.domain` | Release time constant of the level detector in seconds (default 0.1) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Dynamics::Compressor as Compressor;

Signal >> Compressor::Device(threshold: 0.5, ratio: 4.0, makeup: 1.0) >> Output;
```
