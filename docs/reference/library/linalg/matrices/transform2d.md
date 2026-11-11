---
title: Transform2D
description: "Applies 2x2 matrix transformation: Vec2D >> Transform2D(matrix: Mat2x2) >> Out2D."
---

# Transform2D

<span class="stride-badge">Module</span> `package LinAlg::Matrices` &bull; Namespace: **`LinAlg::Matrices`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Matrices.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Matrices.stride:8]</a>

Applies 2x2 matrix transformation: Vec2D >> Transform2D(matrix: Mat2x2) >> Out2D.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | 2D vector [x, y] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Transformed 2D vector [x, y] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `matrix` | `signal` | — | — | `OutputPort.domain` | 2x2 matrix row-major [m00, m01, m10, m11] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Matrices as Matrices;

Signal >> Matrices::Transform2D(matrix: ...) >> Output;
```
