---
title: Normalize
description: "Normalizes a vector of any dimension to unit length: Vec >> Normalize() >> UnitVec."
---

# Normalize

<span class="stride-badge">Module</span> `package LinAlg::Vectors` &bull; Namespace: **`LinAlg::Vectors`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Vectors.stride#L171" target="_blank" rel="noopener" title="View source on GitHub">[Vectors.stride:171]</a>

Normalizes a vector of any dimension to unit length: Vec >> Normalize() >> UnitVec.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Vector of any size |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Unit vector with the same size as the input. The zero vector stays zero |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import LinAlg::Vectors as Vectors;

Signal >> Vectors::Normalize() >> Output;
```
