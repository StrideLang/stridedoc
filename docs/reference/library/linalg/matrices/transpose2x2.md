---
title: Transpose2x2
description: "Transposes a 2x2 matrix: Mat2x2 >> Transpose2x2() >> Transposed."
---

# Transpose2x2

<span class="stride-badge">Module</span> `package LinAlg::Matrices` &bull; Namespace: **`LinAlg::Matrices`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Matrices.stride#L104" target="_blank" rel="noopener" title="View source on GitHub">[Matrices.stride:104]</a>

Transposes a 2x2 matrix: Mat2x2 >> Transpose2x2() >> Transposed.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `MatrixPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | 2x2 input matrix [m00, m01, m10, m11] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Transposed 2x2 matrix [m00, m10, m01, m11] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import LinAlg::Matrices as Matrices;

Signal >> Matrices::Transpose2x2() >> Output;
```
