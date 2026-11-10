---
title: LowPass
description: "Placeholder for low pass filter. Currently not implemented."
---

# LowPass

<span class="stride-badge">Module</span> `package Stride::Filters` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Filters/LowPass.stride#L2" target="_blank" rel="noopener" title="View source on GitHub">[LowPass.stride:2]</a>

Placeholder for low pass filter. Currently not implemented.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `output` | — | — | — |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `input` | — | — | — |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `frequency` | `CenterFrequency` | — | The frequency of the filter. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `qFactor` | `QFactor` | — | The Q value of the filter. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `gain` | `Gain` | — | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Stride;

# Access via Filters category:
Signal >> Filters::LowPass(frequency: ..., qFactor: ..., gain: ...) >> Output;
```
