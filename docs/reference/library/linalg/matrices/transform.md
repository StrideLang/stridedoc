---
title: Transform
description: "Matrix-vector product of any dimension: Vec >> Transform(matrix: Mat) >> Out. The matrix is row-major with (size of the output) rows and (si"
---

# Transform

<span class="stride-badge">Loop</span> `package LinAlg::Matrices` &bull; Namespace: **`LinAlg::Matrices`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Matrices.stride#L26" target="_blank" rel="noopener" title="View source on GitHub">[Matrices.stride:26]</a>

Matrix-vector product of any dimension: Vec >> Transform(matrix: Mat) >> Out. The matrix is row-major with (size of the output) rows and (size of the input) columns.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» vector</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Vector v with n components. n is the size of this port |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Transformed vector y with m components. m is the size of this port |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ matrix</span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Row-major matrix with m rows and n columns: m * n elements |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import LinAlg::Matrices as Matrices;

Signal >> Matrices::Transform(matrix: ...) >> Output;
```
