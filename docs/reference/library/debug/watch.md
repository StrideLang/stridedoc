---
title: Watch
description: "Signal watch module for non-intrusive runtime observation"
---

# Watch

<span class="stride-badge">Module</span> `package Stride::Debug`

Signal watch module for non-intrusive runtime observation

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | `Input` | — | Signal to be watched and passed through |
| `output` | Output Stream | `Output` | — | Pass-through of the input signal |
| `label` | Property In | `Label` | — | — |

## Usage Example

```stride
import Stride;

# Access via Debug category:
Signal >> Debug::Watch(label: ...) >> Output;
```
