---
title: ExpectMaxError
description: "Statistical maximum absolute error assertion for stream differential testing."
---

# ExpectMaxError

<span class="stride-badge">Module</span> `package Stride`

Statistical maximum absolute error assertion for stream differential testing.

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Two-element input list for maximum absolute error comparison: [Candidate, Baseline] |
| `maxError` | Property In | `MaxError` | — | Maximum allowed absolute error |Candidate - Baseline| |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `MaxError` | `signal` | `0.0005` | — | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectMaxError(maxError: ...) >> Output;
```
