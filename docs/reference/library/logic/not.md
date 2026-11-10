---
title: Not
description: "Logical NOT operation: inverts a switch input."
---

# Not

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Logic** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L85" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:85]</a>

Logical NOT operation: inverts a switch input.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `switch` | — | `OutputPort.domain` | Switch input to invert |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `switch` | — | `OutputPort.domain` | Inverted switch output |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Not() >> Output;
```
