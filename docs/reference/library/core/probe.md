---
title: Probe
description: "Lightweight signal probe that non-intrusively monitors a stream while passing it through"
---

# Probe

<span class="stride-badge">Module</span> `package Stride`

Lightweight signal probe that non-intrusively monitors a stream while passing it through

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Signal to be probed and passed through |
| `output` | Output Stream | `Output` | — | Pass-through of the input signal |
| `label` | Property In | `Label` | — | Label identifier for the probe |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Probe(label: ...) >> Output;
```
