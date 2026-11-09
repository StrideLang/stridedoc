---
title: ExpectTrue
description: "Condition assertion (true). Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectTrue

<span class="stride-badge">Module</span> `package Stride::Assertions`

Condition assertion (true). Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Condition value expected to be true (on) |

## Usage Example

```stride
import Stride;

# Access via Assertions category:
Signal >> Assertions::ExpectTrue() >> Output;
```
