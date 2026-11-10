---
title: Xor
description: "Logical exclusive OR (XOR) operation on switch inputs: [A, B] >> Xor() >> Out."
---

# Xor

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Logic** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L106" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:106]</a>

Logical exclusive OR (XOR) operation on switch inputs: [A, B] >> Xor() >> Out.

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `switch` | `OutputPort.domain` | Two-element switch list: [A, B] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `switch` | `OutputPort.domain` | Switch output of A XOR B |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Xor() >> Output;
```
