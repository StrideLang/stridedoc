---
title: Pow
description: "Computes Base raised to the power of Exponent: pow(Input[0], Input[1])."
---

# Pow

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Math** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L360" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:360]</a>

Computes Base raised to the power of Exponent: pow(Input[0], Input[1]).

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Two-element input list: [Base, Exponent] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Result of Base raised to Exponent |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Pow() >> Output;
```
