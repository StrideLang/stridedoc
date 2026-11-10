---
title: Impulse
description: "Impulse module definition."
---

# Impulse

<span class="stride-badge">Module</span> `package Stride::Generators` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Generators/Oscillator.stride#L88" target="_blank" rel="noopener" title="View source on GitHub">[Oscillator.stride:88]</a>

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | — |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `Frequency` | — | The frequency of the oscillator. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `amplitude` | `Amplitude` | — | The amplitude of the oscillator. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Frequency` | `signal` | `440.0` | — | — |
| `Amplitude` | `signal` | `1.0` | — | — |
| `Phase` | `signal` | `1.0` | Domain: OutputPort.domain | — |
| `PhaseInc` | `signal` | `0.0` | Domain: FrequencyPort.domain | — |

## Usage

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::Impulse(frequency: ..., amplitude: ...) >> Output;
```
