---
title: BandLimitedSaw
description: "BandLimitedSaw module definition."
---

# BandLimitedSaw

<span class="stride-badge">Module</span> `package Stride::Generators` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Generators/BandLimitedSaw.stride#L1" target="_blank" rel="noopener" title="View source on GitHub">[BandLimitedSaw.stride:1]</a>

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `output` | `Output` | — | The module's primary output port. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `Frequency` | — | The frequency of the oscillator in Hz. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Output` | `signal` | `0.0` | — | — |
| `Frequency` | `signal` | `220.0` | Rate: FrequencyPort.rate, Domain: FrequencyPort.domain | — |
| `Osc` | `signal` | `0.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `History` | `signal` | `0.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `PhaseResidue` | `signal` | `0.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Phase` | `signal` | `0.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `W` | `signal` | `0.0` | Rate: none, Domain: FrequencyPort.domain | — |
| `N` | `signal` | `0.0` | Rate: none, Domain: FrequencyPort.domain | — |
| `Scaling` | `signal` | `0.0` | Rate: none, Domain: FrequencyPort.domain | — |
| `DC` | `signal` | `0.0` | Rate: none, Domain: FrequencyPort.domain | — |
| `Norm` | `signal` | `0.0` | Rate: none, Domain: FrequencyPort.domain | — |

## Usage

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::BandLimitedSaw(frequency: ...) >> Output;
```
