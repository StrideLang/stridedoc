---
title: DbToLinear
description: "Converts decibels (dB) to linear amplitude ratio."
---

# DbToLinear

<span class="stride-badge">Module</span> `package Dsp::Units` &bull; Namespace: **`Dsp::Units`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Units.stride#L91" target="_blank" rel="noopener" title="View source on GitHub">[Units.stride:91]</a>

Converts decibels (dB) to linear amplitude ratio.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `DbPort` | `LinearPort.type` | — | `DbPort.domain` | Amplitude in decibels (dB) |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `LinearPort` | `LinearPort.type` | — | `LinearPort.domain` | Linear amplitude ratio |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Dsp::Units as Units;

Signal >> Units::DbToLinear() >> Output;
```
