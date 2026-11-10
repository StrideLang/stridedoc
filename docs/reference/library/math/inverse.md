---
title: Inverse
description: "Inverts (changes the sign of) an input value: -Input."
---

# Inverse

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Math** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Math.stride#L331" target="_blank" rel="noopener" title="View source on GitHub">[Math.stride:331]</a>

Inverts (changes the sign of) an input value: -Input.

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Value to negate |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | The negated value |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Inverse() >> Output;
```
