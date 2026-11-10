---
title: BandLimitedSaw
description: "BandLimitedSaw module definition."
---

# BandLimitedSaw

<span class="stride-badge">Module</span> `package Stride::Generators`

*Module declared in `library\1.0\Generators\BandLimitedSaw.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `output` | Output Stream | `Output` | — | The module's primary output port. |
| `frequency` | Property In | `Frequency` | — | The frequency of the oscillator in Hz. |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Output` | `signal` | `0.0` | — | — |
| `Frequency` | `signal` | `0.0` | Rate: /, Domain: } | — |

## Usage

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::BandLimitedSaw(frequency: ...) >> Output;
```
