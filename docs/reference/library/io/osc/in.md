---
title: In
description: "Receives OSC messages from a UDP network port."
---

# In

<span class="stride-badge">Module</span> `package IO::Osc` &bull; Namespace: **`IO::Osc`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Osc.stride#L42" target="_blank" rel="noopener" title="View source on GitHub">[Osc.stride:42]</a>

Receives OSC messages from a UDP network port.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | — | Received OSC signal values |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `address` | `signal` | `/Stride` | — | — | The OSC address filter |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `host` | `signal` | `127.0.0.1` | — | — | Network interface or IP to listen on |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `port` | `signal` | `9011` | — | — | Local UDP network port number to bind |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import IO::Osc as Osc;

Signal >> Osc::In(address: /Stride, host: 127.0.0.1, port: 9011) >> Output;
```
