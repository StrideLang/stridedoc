---
title: Oscillator
description: "Oscillator module definition."
---

# Oscillator

<span class="stride-badge">Module</span> `package Stride::Generators`

*Module declared in `library\1.0\Generators\Oscillator.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `OutputPort` | Output Stream | `Output` | — | — |
| `frequency` | Property In | `Frequency` | — | The frequency of the oscillator. |
| `amplitude` | Property In | `Amplitude` | — | The amplitude of the oscillator. |
| `phase` | Property In | `StartPhase` | — | The starting phase of the oscillator. |
| `reset` | Property In | `Reset` | — | Resets the oscillator to the starting phase. |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Frequency` | `signal` | `440.0` | — | — |
| `Amplitude` | `signal` | `1.0` | — | — |
| `Phase` | `signal` | `0.0` | Rate: >>, Domain: } | — |

## Usage

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::Oscillator(frequency: ..., amplitude: ..., phase: ...) >> Output;
```
