---
title: OSCOut
description: "Sends OSC messages."
---

# OSCOut

<span class="stride-badge">Module</span> `package Stride::Osc` &bull; Namespace: **`Stride::Osc`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Osc/OSC.stride#L2" target="_blank" rel="noopener" title="View source on GitHub">[OSC.stride:2]</a>

Sends OSC messages.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | — | — | — |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `address` | `signal` | `/Stride` | — | — | The OSC address |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `ip` | `signal` | `127.0.0.1` | — | — | The IP address to send to. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `port` | `signal` | `9010` | — | — | The Network port to send the data to. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Stride;

# Access via Osc category:
Signal >> Osc::OSCOut(address: /Stride, ip: 127.0.0.1, port: 9010) >> Output;
```
