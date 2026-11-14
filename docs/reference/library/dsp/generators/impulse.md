---
title: Impulse
description: "Impulse train generator."
---

# Impulse

<span class="stride-badge">Module</span> `package Dsp::Generators` &bull; Namespace: **`Dsp::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Generators/Oscillator.stride#L80" target="_blank" rel="noopener" title="View source on GitHub">[Oscillator.stride:80]</a>

Impulse train generator.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | — | — |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `OutputPort.type` | `440.0` | — | — | The frequency of the oscillator. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `amplitude` | `OutputPort.type` | `1.0` | — | — | The amplitude of the oscillator. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Generators as Generators;

Signal >> Generators::Impulse(frequency: 440.0, amplitude: 1.0) >> Output;
```
