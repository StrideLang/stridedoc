---
title: ExpectNear
description: "Approximate equality assertion within epsilon tolerance. Declared for schema validation; handled with special treatment in the testing frame"
---

# ExpectNear

<span class="stride-badge">Module</span> `package Stride::Assertions`

Approximate equality assertion within epsilon tolerance. Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Two-element input list with values expected to be close: [Actual, Expected] |
| `epsilon` | Property In | `Epsilon` | — | Tolerance threshold for approximate comparison |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Epsilon` | `signal` | `0.0001` | — | — |

## Usage Example

```stride
import Stride;

# Access via Assertions category:
Signal >> Assertions::ExpectNear(epsilon: ...) >> Output;
```
