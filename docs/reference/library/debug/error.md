---
title: Error
description: "Error module reference."
---

# Error

<span class="stride-badge">Module</span> `package Stride::Debug`

*Module defined in `library\1.0\Debug.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `TriggerPort` | Input Stream | `Trigger` | — | — |
| `message` | Property In | `Message` | — | — |

## Usage Example

```stride
import Stride;

# Access via Debug category:
Signal >> Debug::Error(message: ...) >> Output;
```
