---
title: OnChange
description: "OnChange module definition."
---

# OnChange

<span class="stride-badge">Module</span> `package Stride`

*Module declared in `library\1.0\Control.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | Signal or switch being monitored for changes |
| `OutputPort` | Output Stream | `Output` | — | Switch that is on when Input changed from its previous tick value |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `signal` | — | Rate: type, Domain: default | Applies first-order exponential smoothing to Input: Input >> Smooth(coefficient: 0.95) >> Output. |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> OnChange() >> Output;
```
