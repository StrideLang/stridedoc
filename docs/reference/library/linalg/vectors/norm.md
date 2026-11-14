---
title: Norm
description: "Euclidean norm of a vector of any dimension: Vec >> Norm() >> Length. This is also the norm of a quaternion."
---

# Norm

<span class="stride-badge">Module</span> `package LinAlg::Vectors` &bull; Namespace: **`LinAlg::Vectors`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Vectors.stride#L134" target="_blank" rel="noopener" title="View source on GitHub">[Vectors.stride:134]</a>

Euclidean norm of a vector of any dimension: Vec >> Norm() >> Length. This is also the norm of a quaternion.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Vector of any size |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Euclidean vector magnitude / norm |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import LinAlg::Vectors as Vectors;

Signal >> Vectors::Norm() >> Output;
```
