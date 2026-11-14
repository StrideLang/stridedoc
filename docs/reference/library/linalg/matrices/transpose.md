---
title: Transpose
description: "Transposes a matrix of any shape: Mat >> Transpose(rows: 2 columns: 3) >> Transposed."
---

# Transpose

<span class="stride-badge">Loop</span> `package LinAlg::Matrices` &bull; Namespace: **`LinAlg::Matrices`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Matrices.stride#L275" target="_blank" rel="noopener" title="View source on GitHub">[Matrices.stride:275]</a>

Transposes a matrix of any shape: Mat >> Transpose(rows: 2 columns: 3) >> Transposed.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `MatrixPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Row-major input matrix with `rows` rows and `columns` columns |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Row-major transposed matrix with `columns` rows and `rows` columns. Same size as the input |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `rows` | `Int` | `2` | — | `OutputPort.domain` | Number of rows of the input matrix (default 2) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `columns` | `Int` | `2` | — | `OutputPort.domain` | Number of columns of the input matrix (default 2) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Matrices as Matrices;

Signal >> Matrices::Transpose(rows: 2, columns: 2) >> Output;
```
