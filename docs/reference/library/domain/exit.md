---
title: Exit
description: "When input is true, the current domain terminates without executing any further."
---

# Exit

<span class="stride-badge">Module</span> `package Stride::Domain`

When input is true, the current domain terminates without executing any further.

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `MainInputPort` | Input Stream | `Input` | — | — |

## Usage Example

```stride
import Stride;

# Access via Domain category:
Signal >> Domain::Exit() >> Output;
```
