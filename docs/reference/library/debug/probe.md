---
title: Probe
description: "Lightweight signal probe that non-intrusively monitors a stream while passing it through"
---

# Probe

<span class="stride-badge">Module</span> `package Stride::Debug`

Lightweight signal probe that non-intrusively monitors a stream while passing it through

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Signal to be probed and passed through |
| `output` | Output Stream | `Output` | — | Pass-through of the input signal |
| `label` | Property In | `Label` | — | Label identifier for the probe |

## Usage Example

```stride
import Stride;

# Access via Debug category:
Signal >> Debug::Probe(label: ...) >> Output;
```
