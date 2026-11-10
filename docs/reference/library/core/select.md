---
title: Select
description: "Select module definition."
---

# Select

<span class="stride-badge">Module</span> `package Stride`

*Module declared in `library\1.0\Logic.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | Default signal flowing along the primary path |
| `OutputPort` | Output Stream | `Output` | — | Selected output signal |
| `condition` | Property In | `Condition` | — | Switch condition determining which value is output |
| `whenOn` | Property In | `WhenOn` | — | Signal produced when Condition is on |
| `whenOff` | Property In | `WhenOff` | — | Signal produced when Condition is off (defaults to Input if not specified) |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `signal` | — | Domain: } | Logical NOR operation on switch inputs: [A, B] >> Nor() >> Out. |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Select(condition: ..., whenOn: ..., whenOff: ...) >> Output;
```
