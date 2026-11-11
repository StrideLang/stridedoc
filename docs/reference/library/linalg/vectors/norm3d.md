---
title: Norm3D
description: "3D Vector Euclidean norm: Vec >> Norm3D() >> Length."
---

# Norm3D

<span class="stride-badge">Module</span> `package LinAlg::Vectors` &bull; Namespace: **`LinAlg::Vectors`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Vectors.stride#L126" target="_blank" rel="noopener" title="View source on GitHub">[Vectors.stride:126]</a>

3D Vector Euclidean norm: Vec >> Norm3D() >> Length.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | 3D vector [x, y, z] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Euclidean vector magnitude / norm |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import LinAlg::Vectors as Vectors;

Signal >> Vectors::Norm3D() >> Output;
```
