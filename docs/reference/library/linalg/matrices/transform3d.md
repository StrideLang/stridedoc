---
title: Transform3D
description: "Applies 3x3 matrix transformation: Vec3D >> Transform3D(matrix: Mat3x3) >> Out3D."
---

# Transform3D

<span class="stride-badge">Module</span> `package LinAlg::Matrices` &bull; Namespace: **`LinAlg::Matrices`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Matrices.stride#L39" target="_blank" rel="noopener" title="View source on GitHub">[Matrices.stride:39]</a>

Applies 3x3 matrix transformation: Vec3D >> Transform3D(matrix: Mat3x3) >> Out3D.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | 3D vector [x, y, z] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Transformed 3D vector [x, y, z] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `matrix` | `signal` | — | — | `OutputPort.domain` | 3x3 matrix row-major array of 9 elements |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Matrices as Matrices;

Signal >> Matrices::Transform3D(matrix: ...) >> Output;
```
