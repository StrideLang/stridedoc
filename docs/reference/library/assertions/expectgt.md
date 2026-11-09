---
title: ExpectGt
description: "Greater-than assertion module (Actual > Expected). Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectGt

<span class="stride-badge">Module</span> `package Stride::Assertions`

Greater-than assertion module (Actual > Expected). Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Two-element input list for greater-than comparison: [Actual, Expected] |

## Usage Example

```stride
import Stride;

# Access via Assertions category:
Signal >> Assertions::ExpectGt() >> Output;
```
