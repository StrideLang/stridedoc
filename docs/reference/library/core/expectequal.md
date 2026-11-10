---
title: ExpectEqual
description: "Equality assertion module. Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectEqual

<span class="stride-badge">Module</span> `package Stride`

Equality assertion module. Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Two-element input list with values expected to be equal: [Actual, Expected] |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectEqual() >> Output;
```
