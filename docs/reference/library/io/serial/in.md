---
title: In
description: "Reads signal values from platform serial input stream."
---

# In

<span class="stride-badge">Module</span> `package IO::Serial` &bull; Namespace: **`IO::Serial`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Serial.stride#L50" target="_blank" rel="noopener" title="View source on GitHub">[Serial.stride:50]</a>

Reads signal values from platform serial input stream.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | `OutputPort.domain` | Serial input signal stream |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `channel` | `signal` | `0` | — | — | Serial channel index (default 0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import IO::Serial as Serial;

Signal >> Serial::In(channel: 0) >> Output;
```
