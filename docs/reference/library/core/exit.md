---
title: Exit
description: "When input is true, the current domain terminates without executing any further."
---

# Exit

<span class="stride-badge">Module</span> `package Stride`

When input is true, the current domain terminates without executing any further.

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `MainInputPort` | Input Stream | `Input` | — | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Exit() >> Output;
```
