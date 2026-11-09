---
title: Oscillator
description: "Oscillator module reference."
---

# Oscillator

<span class="stride-badge">Module</span> `package Stride::Generators`

*Module defined in `library\1.0\Generators\Oscillator.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `OutputPort` | Output Stream | `Output` | — | — |
| `frequency` | Property In | `Frequency` | — | The frequency of the oscillator. |
| `amplitude` | Property In | `Amplitude` | — | The amplitude of the oscillator. |
| `phase` | Property In | `StartPhase` | — | The starting phase of the oscillator. |
| `reset` | Property In | `Reset` | — | Resets the oscillator to the starting phase. |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Frequency` | `signal` | `440.0` | — | — |
| `Amplitude` | `signal` | `1.0` | — | — |
| `Phase` | `signal` | `0.0` | Rate: >>, Domain: } | — |

## Usage Example

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::Oscillator(frequency: ..., amplitude: ..., phase: ...) >> Output;
```
