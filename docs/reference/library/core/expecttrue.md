---
title: ExpectTrue
description: "Condition assertion (true). Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectTrue

<span class="stride-badge">Module</span> `package Stride`

Condition assertion (true). Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Condition value expected to be true (on) |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectTrue() >> Output;
```
