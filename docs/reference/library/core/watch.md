---
title: Watch
description: "Signal watch module for non-intrusive runtime observation"
---

# Watch

<span class="stride-badge">Module</span> `package Stride`

Signal watch module for non-intrusive runtime observation

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Signal to be watched and passed through |
| `output` | Output Stream | `Output` | — | Pass-through of the input signal |
| `label` | Property In | `Label` | — | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Watch(label: ...) >> Output;
```
