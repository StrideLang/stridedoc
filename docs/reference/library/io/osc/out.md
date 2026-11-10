---
title: Out
description: "Transmits OSC messages over UDP to a network host."
---

# Out

<span class="stride-badge">Module</span> `package IO::Osc` &bull; Namespace: **`IO::Osc`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Osc.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Osc.stride:7]</a>

Transmits OSC messages over UDP to a network host.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | — | `InputPort.domain` | Signal data to send via OSC |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `address` | `signal` | `/Stride` | — | — | The OSC address string (default /Stride) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `host` | `signal` | `127.0.0.1` | — | — | Destination hostname or IP address |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `port` | `signal` | `9010` | — | — | Destination UDP network port number |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import IO::Osc as Osc;

Signal >> Osc::Out(address: /Stride, host: 127.0.0.1, port: 9010) >> Output;
```
