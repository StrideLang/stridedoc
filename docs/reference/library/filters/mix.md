---
title: Mix
description: "Mix module reference."
---

# Mix

<span class="stride-badge">Module</span> `package Stride::Filters`

*Module defined in `library\1.0\Filters\Mix.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `output` | Port | `Output` | — | The module's primary output port. |
| `input` | Port | `Input` | — | The module's primary output port. |
| `gain` | Port | `Gain` | — | Gain applied to channel. |
| `bias` | Port | `Bias` | — | Bias applied to channel. |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Gain[InputPortSize]` | `signal` | `[` | — | — |
| `Bias[InputPortSize]` | `signal` | `[` | — | — |
| `ComputeMix_Index` | `signal` | `1` | Rate: none, Domain: OutputPortDomain | — |

## Usage Example

```stride
import Stride;

# Access via Filters category:
Signal >> Filters::Mix() >> Output;
```
