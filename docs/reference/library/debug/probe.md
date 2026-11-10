---
title: Probe
description: "Lightweight signal probe that non-intrusively monitors a stream while passing it through"
---

# Probe

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Debug.stride#L41" target="_blank" rel="noopener" title="View source on GitHub">[Debug.stride:41]</a>

Lightweight signal probe that non-intrusively monitors a stream while passing it through

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `input` | `Input` | — | Signal to be probed and passed through |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `output` | `Output` | — | Pass-through of the input signal |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `label` | `Label` | — | Label identifier for the probe |

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
Signal >> Probe(label: ...) >> Output;
```
