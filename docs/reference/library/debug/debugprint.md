---
title: DebugPrint
description: "DebugPrint module reference."
---

# DebugPrint

<span class="stride-badge">Module</span> `package Stride::Debug`

*Module defined in `library\1.0\Debug.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `value` | Input Stream | `Value` | — | — |
| `trigger` | Property In | `Trigger` | — | — |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Value` | `signal` | `0.0` | — | — |
| `Trigger` | `switch` | `on` | — | — |

## Usage Example

```stride
import Stride;

# Access via Debug category:
Signal >> Debug::DebugPrint(trigger: ...) >> Output;
```
