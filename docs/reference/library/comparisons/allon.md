---
title: AllOn
description: "Outputs on if all switches in the input array are on: Input >> AllOn() >> Output."
---

# AllOn

<span class="stride-badge">Loop</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Comparisons.stride#L172" target="_blank" rel="noopener" title="View source on GitHub">[Comparisons.stride:172]</a>

Outputs on if all switches in the input array are on: Input >> AllOn() >> Output.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `AllOn_Input` | — | Array of switches to be checked |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `AllOn_Output` | — | Switch that is on only if all input switches are on |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AllOn_Input[InputPort.size]` | `switch` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `AllOn_Output` | `switch` | `on` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `AllOn_Index` | `signal` | `0` | Rate: none, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> AllOn() >> Output;
```
