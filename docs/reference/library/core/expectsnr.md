---
title: ExpectSnr
description: "Statistical Signal-to-Noise Ratio assertion for stream differential testing."
---

# ExpectSnr

<span class="stride-badge">Module</span> `package Stride`

Statistical Signal-to-Noise Ratio assertion for stream differential testing.

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Two-element input list for Signal-to-Noise Ratio comparison: [Candidate, Baseline] |
| `minSnr` | Property In | `MinSnr` | — | Minimum acceptable Signal-to-Noise Ratio in dB |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `MinSnr` | `signal` | `80.0` | — | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectSnr(minSnr: ...) >> Output;
```
