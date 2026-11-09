---
title: Abs
description: "Abs module reference."
---

# Abs

<span class="stride-badge">Module</span> `package Stride::Math`

*Module defined in `library\1.0\Math.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | Input value |
| `OutputPort` | Output Stream | `Output` | — | Absolute value |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `signal` | — | Rate: type, Domain: } | Linearly maps Input from [inMin, inMax] to [outMin, outMax]: Input >> Map(inMin: 0.0 inMax: 1.0 outMin: 100.0 outMax: 1000.0) >> Output. |

## Usage Example

```stride
import Stride;

# Access via Math category:
Signal >> Math::Abs() >> Output;
```
