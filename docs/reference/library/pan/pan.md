---
title: Pan
description: "Pan module reference."
---

# Pan

<span class="stride-badge">Module</span> `package Stride::Pan`

*Module defined in `library\1.0\Pan.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `output` | Output Stream | `Output` | — | — |
| `input` | Input Stream | `Input` | — | — |
| `position` | Property In | `Position` | — | Sets the panning position with range [-1, 1]. |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `GainLeft` | `signal` | — | Domain: } | Stereo panner. |

## Usage Example

```stride
import Stride;

# Access via Pan category:
Signal >> Pan::Pan(position: ...) >> Output;
```
