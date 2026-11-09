---
title: BiQuad
description: "BiQuad filter"
---

# BiQuad

<span class="stride-badge">Module</span> `package Stride::Filters`

BiQuad filter

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `MainInputPort` | Input Stream | `Input` | — | — |
| `OutputPort` | Output Stream | `Output` | — | — |
| `centerFrequency` | Property In | `CenterFrequency` | — | The center frequency of the filter. |
| `resonance` | Property In | `Resonance` | — | Resonance (Q) amount. Should be greater than on equal to 1.0. |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Resonance` | `signal` | `50` | — | — |

## Usage Example

```stride
import Stride;

# Access via Filters category:
Signal >> Filters::BiQuad(centerFrequency: ..., resonance: ...) >> Output;
```
