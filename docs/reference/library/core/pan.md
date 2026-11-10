---
title: Pan
description: "Pan module definition."
---

# Pan

<span class="stride-badge">Module</span> `package Stride`

*Module declared in `library\1.0\Pan.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `output` | Output Stream | `Output` | — | — |
| `input` | Input Stream | `Input` | — | — |
| `position` | Property In | `Position` | — | Sets the panning position with range [-1, 1]. |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `GainLeft` | `signal` | — | Domain: } | Stereo panner. |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Pan(position: ...) >> Output;
```
