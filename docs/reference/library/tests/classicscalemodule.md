---
title: ClassicScaleModule
description: "ClassicScaleModule module reference."
---

# ClassicScaleModule

<span class="stride-badge">Module</span> `package Stride::tests`

*Module defined in `library\1.0\tests\CallableTest.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InPort` | Input Stream | `Input` | — | — |
| `factor` | Property In | `Factor` | — | — |
| `OutPort` | Output Stream | `Output` | — | — |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `signal` | `0.0` | — | — |
| `Factor` | `signal` | `2.0` | — | — |
| `Output` | `signal` | `0.0` | — | — |

## Usage Example

```stride
import Stride;

# Access via tests category:
Signal >> tests::ClassicScaleModule(factor: ...) >> Output;
```
