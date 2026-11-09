---
title: BandLimitedSaw
description: "BandLimitedSaw module reference."
---

# BandLimitedSaw

<span class="stride-badge">Module</span> `package Stride::Generators`

*Module defined in `library\1.0\Generators\BandLimitedSaw.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `output` | Output Stream | `Output` | — | The module's primary output port. |
| `frequency` | Property In | `Frequency` | — | The frequency of the oscillator in Hz. |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Output` | `signal` | `0.0` | — | — |
| `Frequency` | `signal` | `0.0` | Rate: /, Domain: } | — |

## Usage Example

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::BandLimitedSaw(frequency: ...) >> Output;
```
