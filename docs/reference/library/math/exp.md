---
title: Exp
description: "Computes the natural exponential: exp(Input)."
---

# Exp

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Math** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L389" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:389]</a>

Computes the natural exponential: exp(Input).

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `OutputPort.type` | `OutputPort.rate` / `OutputPort.domain` | Exponent value |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `OutputPort.type` | `OutputPort.rate` / `OutputPort.domain` | Result of e raised to Input |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Exp() >> Output;
```
