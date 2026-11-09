---
title: ExpectEqual
description: "Equality assertion module. Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectEqual

<span class="stride-badge">Module</span> `package Stride::Assertions`

Equality assertion module. Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Two-element input list with values expected to be equal: [Actual, Expected] |

## Usage Example

```stride
import Stride;

# Access via Assertions category:
Signal >> Assertions::ExpectEqual() >> Output;
```
