---
title: LowPass
description: "Placeholder for low pass filter. Currently not implemented."
---

# LowPass

<span class="stride-badge">Module</span> `package Stride::Filters`

Placeholder for low pass filter. Currently not implemented.

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `output` | Output Stream | — | — | — |
| `input` | Input Stream | — | — | — |
| `frequency` | Property In | `CenterFrequency` | — | The frequency of the filter. |
| `qFactor` | Property In | `QFactor` | — | The Q value of the filter. |
| `gain` | Property In | `Gain` | — | — |

## Usage

```stride
import Stride;

# Access via Filters category:
Signal >> Filters::LowPass(frequency: ..., qFactor: ..., gain: ...) >> Output;
```
