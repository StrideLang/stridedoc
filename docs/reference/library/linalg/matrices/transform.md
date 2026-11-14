---
title: Transform
description: "Matrix-vector product of any dimension: Vec >> Transform(matrix: Mat) >> Out. The matrix is row-major with (size of the output) rows and (si"
---

# Transform

<span class="stride-badge">Loop</span> `package LinAlg::Matrices` &bull; Namespace: **`LinAlg::Matrices`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Matrices.stride#L26" target="_blank" rel="noopener" title="View source on GitHub">[Matrices.stride:26]</a>

Matrix-vector product of any dimension: Vec >> Transform(matrix: Mat) >> Out. The matrix is row-major with (size of the output) rows and (size of the input) columns.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Vector v with n components. n is the size of this port |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Transformed vector y with m components. m is the size of this port |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `matrix` | `OutputPort.type` | — | — | `OutputPort.domain` | Row-major matrix with m rows and n columns: m * n elements |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Matrices as Matrices;

Signal >> Matrices::Transform(matrix: ...) >> Output;
```
