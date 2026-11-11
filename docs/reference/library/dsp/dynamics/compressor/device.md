---
title: Device
description: "Feedforward dynamic range compressor: AudioIn >> Compressor::Device(threshold: 0.5 ratio: 4.0 makeup: 1.2) >> Out."
---

# Device

<span class="stride-badge">Module</span> `package Dsp::Dynamics::Compressor` &bull; Namespace: **`Dsp::Dynamics::Compressor`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Dynamics/Compressor.stride#L10" target="_blank" rel="noopener" title="View source on GitHub">[Compressor.stride:10]</a>

Feedforward dynamic range compressor: AudioIn >> Compressor::Device(threshold: 0.5 ratio: 4.0 makeup: 1.2) >> Out.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Input audio signal stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Compressed audio signal stream |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `threshold` | `signal` | `0.5` | — | `OutputPort.domain` | Compression threshold in linear amplitude (default 0.5) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `ratio` | `signal` | `4.0` | — | `OutputPort.domain` | Compression slope ratio (e.g., 4.0 for 4:1) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `makeup` | `signal` | `1.0` | — | `OutputPort.domain` | Post-compression makeup gain multiplier |

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
