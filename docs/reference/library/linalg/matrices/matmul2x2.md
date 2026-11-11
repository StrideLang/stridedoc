---
title: MatMul2x2
description: "Multiplies two 2x2 matrices: MatA >> MatMul2x2(with: MatB) >> Result."
---

# MatMul2x2

<span class="stride-badge">Module</span> `package LinAlg::Matrices` &bull; Namespace: **`LinAlg::Matrices`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Matrices.stride#L71" target="_blank" rel="noopener" title="View source on GitHub">[Matrices.stride:71]</a>

Multiplies two 2x2 matrices: MatA >> MatMul2x2(with: MatB) >> Result.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `MatrixAPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | First 2x2 matrix [a00, a01, a10, a11] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Result 2x2 matrix [c00, c01, c10, c11] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `with` | `signal` | — | — | `OutputPort.domain` | Second 2x2 matrix [b00, b01, b10, b11] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Matrices as Matrices;

Signal >> Matrices::MatMul2x2(with: ...) >> Output;
```
