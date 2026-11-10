---
title: BandPass
description: "Band pass filter"
---

# BandPass

<span class="stride-badge">Module</span> `package Stride::Filters`

Band pass filter

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `output` | Port | — | — | — |
| `input` | Port | — | — | — |
| `centerFrequency` | Port | `CenterFrequency` | — | The center frequency of the filter. |
| `qFactor` | Port | `QFactor` | — | The Q value of the filter. |
| `gain` | Port | `Gain` | — | — |

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
