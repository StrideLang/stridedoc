---
title: Abs
description: "Abs module definition."
---

# Abs

<span class="stride-badge">Module</span> `package Stride`

*Module declared in `library\1.0\Math.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | Input value |
| `OutputPort` | Output Stream | `Output` | — | Absolute value |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `signal` | — | Rate: type, Domain: } | Linearly maps Input from [inMin, inMax] to [outMin, outMax]: Input >> Map(inMin: 0.0 inMax: 1.0 outMin: 100.0 outMax: 1000.0) >> Output. |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Abs() >> Output;
```
