---
title: ExpectFalse
description: "Condition assertion (false). Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectFalse

<span class="stride-badge">Module</span> `package Stride::Assertions`

Condition assertion (false). Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Condition value expected to be false (off) |

## Usage Example

```stride
import Stride;

# Access via Assertions category:
Signal >> Assertions::ExpectFalse() >> Output;
```
