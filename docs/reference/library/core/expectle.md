---
title: ExpectLe
description: "Less-than-or-equal assertion module (Actual <= Expected). Declared for schema validation; handled with special treatment in the testing fram"
---

# ExpectLe

<span class="stride-badge">Module</span> `package Stride`

Less-than-or-equal assertion module (Actual <= Expected). Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Two-element input list for less-than-or-equal comparison: [Actual, Expected] |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectLe() >> Output;
```
