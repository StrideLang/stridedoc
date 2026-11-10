---
title: ExpectFalse
description: "Condition assertion (false). Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectFalse

<span class="stride-badge">Module</span> `package Stride`

Condition assertion (false). Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Condition value expected to be false (off) |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectFalse() >> Output;
```
