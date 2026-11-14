---
title: MatMul
description: "Matrix product of any compatible shapes: MatA >> MatMul(with: MatB inner: 3 columns: 2) >> Result. All matrices are row-major. The number of"
---

# MatMul

<span class="stride-badge">Loop</span> `package LinAlg::Matrices` &bull; Namespace: **`LinAlg::Matrices`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Matrices.stride#L119" target="_blank" rel="noopener" title="View source on GitHub">[Matrices.stride:119]</a>

Matrix product of any compatible shapes: MatA >> MatMul(with: MatB inner: 3 columns: 2) >> Result. All matrices are row-major. The number of rows of A comes from the size of the result.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `MatrixAPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Row-major matrix A with m rows and `inner` columns |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Row-major result C with m rows and `columns` columns. Its size is m * columns |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>with</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Row-major matrix B with `inner` rows and `columns` columns |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>inner</code></span> <span class="prop-default">= <code>2</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>Int</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Number of columns of A, which is the number of rows of B (default 2) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>columns</code></span> <span class="prop-default">= <code>2</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>Int</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Number of columns of B, which is the number of columns of the result (default 2) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import LinAlg::Matrices as Matrices;

Signal >> Matrices::MatMul(with: ..., inner: 2, columns: 2) >> Output;
```
