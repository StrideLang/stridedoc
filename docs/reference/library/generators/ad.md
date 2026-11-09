---
title: AD
description: "AD module reference."
---

# AD

<span class="stride-badge">Module</span> `package Stride::Generators`

*Module defined in `library\1.0\Generators\Envelope.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `output` | Output Stream | `Output` | — | The module's primary output port. |
| `output` | Input Stream | `TriggerEnv` | — | Triggers the envelope |
| `attack` | Property In | `AttackTime` | — | Attack time in seconds |
| `decay` | Property In | `DecayTime` | — | Decay time in seconds |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AttackTime` | `signal` | `0.2` | — | — |
| `DecayTime` | `signal` | `3.0` | — | — |
| `Output` | `signal` | `0.0` | — | — |
| `StageIncrements[2]` | `signal` | `0.0` | — | — |
| `TriggerEnv` | `trigger` | `-1` | Rate: ), Domain: } | — |

## Usage Example

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::AD(attack: ..., decay: ...) >> Output;
```
