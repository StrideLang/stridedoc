---
title: Print
description: "Writes values formatted to the serial port."
---

# Print

<span class="stride-badge">Module</span> `package IO::Serial` &bull; Namespace: **`IO::Serial`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Serial.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Serial.stride:7]</a>

Writes values formatted to the serial port.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `ValuePort` | `signal` | — | `ValuePort.domain` | Value to write to serial |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import IO::Serial as Serial;

Signal >> Serial::Print() >> Output;
```
