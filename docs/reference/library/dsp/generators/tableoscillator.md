---
title: TableOscillator
description: "Table read oscillator."
---

# TableOscillator

<span class="stride-badge">Module</span> `package Dsp::Generators` &bull; Namespace: **`Dsp::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Generators/TableOscillator.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[TableOscillator.stride:7]</a>

Table read oscillator.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | — | — |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `OutputPort.type` | `440.0` | — | — | The frequency of the oscillator. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `amplitude` | `OutputPort.type` | `1.0` | — | — | The amplitude of the oscillator. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `phase` | `signal` | — | — | — | The starting phase of the oscillator. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `reset` | `signal` | — | — | — | Resets the oscillator to the starting phase. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Generators as Generators;

Signal >> Generators::TableOscillator(frequency: 440.0, amplitude: 1.0, phase: ...) >> Output;
```
