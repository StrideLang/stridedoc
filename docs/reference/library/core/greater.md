---
title: Greater
description: "Greater module definition."
---

# Greater

<span class="stride-badge">Module</span> `package Stride`

*Module declared in `library\1.0\Comparisons.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | Two-element list with values to compare: [Left, Right] |
| `OutputPort` | Output Stream | `Output` | — | Switch indicating if Left > Right |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input[2]` | `signal` | `0` | Rate: none, Domain: } | Outputs on if all switches in the input array are off: Input >> AllOff() >> Output. |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Greater() >> Output;
```
