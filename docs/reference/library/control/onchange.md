---
title: OnChange
description: "OnChange module reference."
---

# OnChange

<span class="stride-badge">Module</span> `package Stride::Control`

*Module defined in `library\1.0\Control.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | Signal or switch being monitored for changes |
| `OutputPort` | Output Stream | `Output` | — | Switch that is on when Input changed from its previous tick value |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `signal` | — | Rate: type, Domain: default | Applies first-order exponential smoothing to Input: Input >> Smooth(coefficient: 0.95) >> Output. |

## Usage Example

```stride
import Stride;

# Access via Control category:
Signal >> Control::OnChange() >> Output;
```
