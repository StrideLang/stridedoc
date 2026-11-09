---
title: Level
description: "Level module reference."
---

# Level

<span class="stride-badge">Module</span> `package Stride::Level`

*Module defined in `library\1.0\Level.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | — |
| `OutputPort` | Output Stream | `Output` | — | — |
| `gain` | Property In | `Gain` | — | Amplifies or attenuates the signal. |
| `offset` | Property In | `Offset` | — | Adds an offset to the signal after applying the gain. |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Gain` | `signal` | `0.0` | Rate: domain, Domain: } | Scales the input signal and applies an offset to it. Formula: output = input * gain + offset  |

## Usage Example

```stride
import Stride;

# Access via Level category:
Signal >> Level::Level(gain: ..., offset: ...) >> Output;
```
