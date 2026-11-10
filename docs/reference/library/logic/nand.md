---
title: Nand
description: "Logical NAND operation on switch inputs: [A, B] >> Nand() >> Out."
---

# Nand

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Logic** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L127" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:127]</a>

Logical NAND operation on switch inputs: [A, B] >> Nand() >> Out.

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Input` | `switch` | `OutputPort.domain` | Two-element switch list: [A, B] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `Output` | `switch` | `OutputPort.domain` | Switch output of A NAND B |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Nand() >> Output;
```
