---
title: OSCIn
description: "Receives OSC messages."
---

# OSCIn

<span class="stride-badge">Module</span> `package Stride::Osc` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Osc/OSC.stride#L35" target="_blank" rel="noopener" title="View source on GitHub">[OSC.stride:35]</a>

Receives OSC messages.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `output` | — | — | — |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `address` | `Address` | — | The OSC address |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `ip` | `IP` | — | The IP address to receive from. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `port` | `Port` | — | The Network port to receive the data from. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Address` | `signal` | `/Stride` | — | — |
| `IP` | `signal` | `127.0.0.1` | — | — |
| `Port` | `signal` | `9011` | — | — |

## Usage

```stride
import Stride;

# Access via Osc category:
Signal >> Osc::OSCIn(address: ..., ip: ..., port: ...) >> Output;
```
