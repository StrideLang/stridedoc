---
title: BandLimitedSaw
description: "Band-limited sawtooth generator (differentiated parabolic wave, DPW): Saw(frequency: 220.0) >> Out. Output in [-1, 1). The frequency is in H"
---

# BandLimitedSaw

<span class="stride-badge">Module</span> `package Dsp::Generators` &bull; Namespace: **`Dsp::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Generators/BandLimitedSaw.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[BandLimitedSaw.stride:7]</a>

Band-limited sawtooth generator (differentiated parabolic wave, DPW): Saw(frequency: 220.0) >> Out. Output in [-1, 1). The frequency is in Hz and is converted against the rate of the output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | — | — | The module's primary output port. |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `OutputPort.type` | `220.0` | `FrequencyPort.rate` | `FrequencyPort.domain` | The frequency of the oscillator in Hz. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Generators as Generators;

Signal >> Generators::BandLimitedSaw(frequency: 220.0) >> Output;
```
