---
title: BandPass
description: "Band pass filter"
---

# BandPass

<span class="stride-badge">Module</span> `package Stride::Filters` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Filters/BandPass.stride#L2" target="_blank" rel="noopener" title="View source on GitHub">[BandPass.stride:2]</a>

Band pass filter

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Port">»</span> | `output` | — | — | — |
| <span class="port-icon stream-in" title="Port">»</span> | `input` | — | — | — |
| <span class="port-icon stream-in" title="Port">»</span> | `centerFrequency` | `CenterFrequency` | — | The center frequency of the filter. |
| <span class="port-icon stream-in" title="Port">»</span> | `qFactor` | `QFactor` | — | The Q value of the filter. |
| <span class="port-icon stream-in" title="Port">»</span> | `gain` | `Gain` | — | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `QFactor` | `signal` | `1.0` | — | — |

## Usage

```stride
import Stride;

# Access via Filters category:
Signal >> Filters::BandPass() >> Output;
```
