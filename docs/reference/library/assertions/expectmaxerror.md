---
title: ExpectMaxError
description: "Statistical maximum absolute error assertion for stream differential testing."
---

# ExpectMaxError

<span class="stride-badge">Module</span> `package Stride::Assertions`

Statistical maximum absolute error assertion for stream differential testing.

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Two-element input list for maximum absolute error comparison: [Candidate, Baseline] |
| `maxError` | Property In | `MaxError` | — | Maximum allowed absolute error |Candidate - Baseline| |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `MaxError` | `signal` | `0.0005` | — | — |

## Usage Example

```stride
import Stride;

# Access via Assertions category:
Signal >> Assertions::ExpectMaxError(maxError: ...) >> Output;
```
