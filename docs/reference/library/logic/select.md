---
title: Select
description: "Select module reference."
---

# Select

<span class="stride-badge">Module</span> `package Stride::Logic`

*Module defined in `library\1.0\Logic.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | Default signal flowing along the primary path |
| `OutputPort` | Output Stream | `Output` | — | Selected output signal |
| `condition` | Property In | `Condition` | — | Switch condition determining which value is output |
| `whenOn` | Property In | `WhenOn` | — | Signal produced when Condition is on |
| `whenOff` | Property In | `WhenOff` | — | Signal produced when Condition is off (defaults to Input if not specified) |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `signal` | — | Domain: } | Logical NOR operation on switch inputs: [A, B] >> Nor() >> Out. |

## Usage Example

```stride
import Stride;

# Access via Logic category:
Signal >> Logic::Select(condition: ..., whenOn: ..., whenOff: ...) >> Output;
```
