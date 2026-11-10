---
title: Nor
description: "Logical NOR operation on switch inputs: [A, B] >> Nor() >> Out."
---

# Nor

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L148" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:148]</a>

Logical NOR operation on switch inputs: [A, B] >> Nor() >> Out.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Two-element switch list: [A, B] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Switch output of A NOR B |

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
Signal >> Nor() >> Output;
```
