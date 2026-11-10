---
title: Or
description: "Logical OR operation on switch inputs: [A, B] >> Or() >> Out."
---

# Or

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L64" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:64]</a>

Logical OR operation on switch inputs: [A, B] >> Or() >> Out.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Two-element switch list: [A, B] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Switch output of A OR B |

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
Signal >> Or() >> Output;
```
