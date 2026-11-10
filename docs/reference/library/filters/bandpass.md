---
title: BandPass
description: "Band pass filter"
---

# BandPass

<span class="stride-badge">Module</span> `package Stride::Filters` &bull; Namespace: **`Stride::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Filters/BandPass.stride#L2" target="_blank" rel="noopener" title="View source on GitHub">[BandPass.stride:2]</a>

Band pass filter

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Port">»</span> | `output` | `signal` | — | — | — |
| <span class="port-icon stream-in" title="Port">»</span> | `input` | `signal` | — | — | — |
| <span class="port-icon stream-in" title="Port">»</span> | `centerFrequency` | `signal` | — | — | The center frequency of the filter. |
| <span class="port-icon stream-in" title="Port">»</span> | `qFactor` | `signal` | — | — | The Q value of the filter. |
| <span class="port-icon stream-in" title="Port">»</span> | `gain` | `signal` | — | — | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Access via Filters category:
Signal >> Filters::BandPass() >> Output;
```
