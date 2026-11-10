---
title: Oscillator
description: "Bipolar output [ -1. , 1. ] scaled by amplitude"
---

# Oscillator

<span class="stride-badge">Module</span> `package Stride::Generators` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Generators/Oscillator.stride#L2" target="_blank" rel="noopener" title="View source on GitHub">[Oscillator.stride:2]</a>

Bipolar output [ -1. , 1. ] scaled by amplitude

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | — |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `Frequency` | — | The frequency of the oscillator. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `amplitude` | `Amplitude` | — | The amplitude of the oscillator. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `phase` | `StartPhase` | — | The starting phase of the oscillator. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `reset` | `Reset` | — | Resets the oscillator to the starting phase. |

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
| `Phase` | `signal` | `0.0` | Domain: OutputPort.domain | — |
| `PhaseInc` | `signal` | `0.0` | Domain: FrequencyPort.domain | — |

## Usage

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::Oscillator(frequency: ..., amplitude: ..., phase: ...) >> Output;
```
