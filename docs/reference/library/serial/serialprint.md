---
title: SerialPrint
description: "SerialPrint module reference."
---

# SerialPrint

<span class="stride-badge">Module</span> `package Stride::Serial`

*Module defined in `library\1.0\Serial\Serial.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `value` | Input Stream | `Value` | — | — |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Value` | `signal` | `0` | Domain: } | — |

## Usage Example

```stride
import Stride;

# Access via Serial category:
Signal >> Serial::SerialPrint() >> Output;
```
