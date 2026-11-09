---
title: ClassicAccumulatorModule
description: "ClassicAccumulatorModule module reference."
---

# ClassicAccumulatorModule

<span class="stride-badge">Module</span> `package Stride::tests`

*Module defined in `library\1.0\tests\CallableTest.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InPort` | Input Stream | `Input` | — | — |
| `reset` | Property In | `Reset` | — | — |
| `OutPort` | Output Stream | `Output` | — | — |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `signal` | `0.0` | — | — |
| `Reset` | `switch` | `off` | — | — |
| `Output` | `signal` | `0.0` | — | — |
| `Total` | `signal` | `0.0` | — | — |

## Usage Example

```stride
import Stride;

# Access via tests category:
Signal >> tests::ClassicAccumulatorModule(reset: ...) >> Output;
```
