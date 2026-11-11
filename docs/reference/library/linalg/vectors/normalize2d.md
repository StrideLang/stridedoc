---
title: Normalize2D
description: "Normalizes 2D vector to unit length: Vec >> Normalize2D() >> UnitVec."
---

# Normalize2D

<span class="stride-badge">Module</span> `package LinAlg::Vectors` &bull; Namespace: **`LinAlg::Vectors`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Vectors.stride#L152" target="_blank" rel="noopener" title="View source on GitHub">[Vectors.stride:152]</a>

Normalizes 2D vector to unit length: Vec >> Normalize2D() >> UnitVec.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | 2D vector [x, y] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Normalized unit 2D vector [x, y] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import LinAlg::Vectors as Vectors;

Signal >> Vectors::Normalize2D() >> Output;
```
