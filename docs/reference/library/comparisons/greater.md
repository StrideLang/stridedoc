---
title: Greater
description: "Greater module reference."
---

# Greater

<span class="stride-badge">Module</span> `package Stride::Comparisons`

*Module defined in `library\1.0\Comparisons.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | Two-element list with values to compare: [Left, Right] |
| `OutputPort` | Output Stream | `Output` | — | Switch indicating if Left > Right |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input[2]` | `signal` | `0` | Rate: none, Domain: } | Outputs on if all switches in the input array are off: Input >> AllOff() >> Output. |

## Usage Example

```stride
import Stride;

# Access via Comparisons category:
Signal >> Comparisons::Greater() >> Output;
```
