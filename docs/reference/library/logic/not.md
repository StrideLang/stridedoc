---
title: Not
description: "Logical NOT operation: inverts a switch input."
---

# Not

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L85" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:85]</a>

Logical NOT operation: inverts a switch input.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Switch input to invert |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Inverted switch output |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Not() >> Output;
```
