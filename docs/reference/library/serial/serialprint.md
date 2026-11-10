---
title: SerialPrint
description: "SerialPrint module definition."
---

# SerialPrint

<span class="stride-badge">Module</span> `package Stride::Serial`

*Module declared in `library\1.0\Serial\Serial.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `value` | Input Stream | `Value` | — | — |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Value` | `signal` | `0` | Domain: } | — |

## Usage

```stride
import Stride;

# Access via Serial category:
Signal >> Serial::SerialPrint() >> Output;
```
