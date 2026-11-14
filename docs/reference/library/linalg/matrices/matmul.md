---
title: MatMul
description: "Matrix product of any compatible shapes: MatA >> MatMul(with: MatB inner: 3 columns: 2) >> Result. All matrices are row-major. The number of"
---

# MatMul

<span class="stride-badge">Loop</span> `package LinAlg::Matrices` &bull; Namespace: **`LinAlg::Matrices`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Matrices.stride#L119" target="_blank" rel="noopener" title="View source on GitHub">[Matrices.stride:119]</a>

Matrix product of any compatible shapes: MatA >> MatMul(with: MatB inner: 3 columns: 2) >> Result. All matrices are row-major. The number of rows of A comes from the size of the result.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `MatrixAPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Row-major matrix A with m rows and `inner` columns |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Row-major result C with m rows and `columns` columns. Its size is m * columns |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `with` | `OutputPort.type` | — | — | `OutputPort.domain` | Row-major matrix B with `inner` rows and `columns` columns |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `inner` | `Int` | `2` | — | `OutputPort.domain` | Number of columns of A, which is the number of rows of B (default 2) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `columns` | `Int` | `2` | — | `OutputPort.domain` | Number of columns of B, which is the number of columns of the result (default 2) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Matrices as Matrices;

Signal >> Matrices::MatMul(with: ..., inner: 2, columns: 2) >> Output;
```
