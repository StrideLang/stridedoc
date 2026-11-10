---
title: DebugPrint
description: "DebugPrint module definition."
---

# DebugPrint

<span class="stride-badge">Module</span> `package Stride`

*Module declared in `library\1.0\Debug.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `value` | Input Stream | `Value` | — | — |
| `trigger` | Property In | `Trigger` | — | — |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Value` | `signal` | `0.0` | — | — |
| `Trigger` | `switch` | `on` | — | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> DebugPrint(trigger: ...) >> Output;
```
