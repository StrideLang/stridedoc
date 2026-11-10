---
title: SerialPrint
description: "SerialPrint module definition."
---

# SerialPrint

<span class="stride-badge">Module</span> `package Stride::Serial` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Serial/Serial.stride#L2" target="_blank" rel="noopener" title="View source on GitHub">[Serial.stride:2]</a>

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `value` | `Value` | — | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Value` | `signal` | `0` | Domain: ValuePort.domain | — |

## Usage

```stride
import Stride;

# Access via Serial category:
Signal >> Serial::SerialPrint() >> Output;
```
