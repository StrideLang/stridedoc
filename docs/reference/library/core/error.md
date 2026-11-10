---
title: Error
description: "Error module definition."
---

# Error

<span class="stride-badge">Module</span> `package Stride`

*Module declared in `library\1.0\Debug.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `TriggerPort` | Input Stream | `Trigger` | — | — |
| `message` | Property In | `Message` | — | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Error(message: ...) >> Output;
```
