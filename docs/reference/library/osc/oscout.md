---
title: OSCOut
description: "Sends OSC messages."
---

# OSCOut

<span class="stride-badge">Module</span> `package Stride::Osc` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Osc/OSC.stride#L2" target="_blank" rel="noopener" title="View source on GitHub">[OSC.stride:2]</a>

Sends OSC messages.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `input` | — | — | — |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `address` | `Address` | — | The OSC address |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `ip` | `IP` | — | The IP address to send to. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `port` | `Port` | — | The Network port to send the data to. |

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
| `Port` | `signal` | `9010` | — | — |

## Usage

```stride
import Stride;

# Access via Osc category:
Signal >> Osc::OSCOut(address: ..., ip: ..., port: ...) >> Output;
```
