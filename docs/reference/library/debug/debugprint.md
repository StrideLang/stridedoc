---
title: DebugPrint
description: "DebugPrint module definition."
---

# DebugPrint

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Debug.stride#L1" target="_blank" rel="noopener" title="View source on GitHub">[Debug.stride:1]</a>

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `value` | `Value` | — | — |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `trigger` | `Trigger` | — | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Value` | `signal` | `0.0` | — | — |
| `Trigger` | `switch` | `on` | — | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> DebugPrint(trigger: ...) >> Output;
```
