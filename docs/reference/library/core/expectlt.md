---
title: ExpectLt
description: "Less-than-or-equal assertion module (Actual < Expected). Declared for schema validation; handled with special treatment in the testing frame"
---

# ExpectLt

<span class="stride-badge">Module</span> `package Stride`

Less-than-or-equal assertion module (Actual < Expected). Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Two-element input list for less-than comparison: [Actual, Expected] |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectLt() >> Output;
```
