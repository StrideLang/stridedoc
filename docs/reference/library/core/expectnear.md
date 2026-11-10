---
title: ExpectNear
description: "Approximate equality assertion within epsilon tolerance. Declared for schema validation; handled with special treatment in the testing frame"
---

# ExpectNear

<span class="stride-badge">Module</span> `package Stride`

Approximate equality assertion within epsilon tolerance. Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Two-element input list with values expected to be close: [Actual, Expected] |
| `epsilon` | Property In | `Epsilon` | — | Tolerance threshold for approximate comparison |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Epsilon` | `signal` | `0.0001` | — | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectNear(epsilon: ...) >> Output;
```
