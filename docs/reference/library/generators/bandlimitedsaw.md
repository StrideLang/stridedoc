---
title: BandLimitedSaw
description: "BandLimitedSaw module definition."
---

# BandLimitedSaw

<span class="stride-badge">Module</span> `package Stride::Generators` &bull; Namespace: **`Stride::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Generators/BandLimitedSaw.stride#L1" target="_blank" rel="noopener" title="View source on GitHub">[BandLimitedSaw.stride:1]</a>

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | — | The module's primary output port. |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `signal` | `220.0` | `FrequencyPort.rate` | `FrequencyPort.domain` | The frequency of the oscillator in Hz. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::BandLimitedSaw(frequency: 220.0) >> Output;
```
