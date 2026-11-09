---
title: Sum
description: "Sum loop reference."
---

# Sum

<span class="stride-badge">Loop</span> `package Stride::BasicOperations`

*Loop defined in `library\1.0\BasicOperations.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Sum_Input` | — | Array of signals to be summed |
| `OutputPort` | Output Stream | `Sum_Output` | — | The sum of all signals in the array |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Sum_Input[InputPort.size]` | `signal` | `0` | Rate: type, Domain: default | Limits signal within minimum and maximum values: Input >> Clip(minimum: 0.0 maximum: 1.0) >> Output. |

## Usage Example

```stride
import Stride;

# Access via BasicOperations category:
Signal >> BasicOperations::Sum() >> Output;
```
