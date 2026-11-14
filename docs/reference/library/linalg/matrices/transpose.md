---
title: Transpose
description: "Transposes a matrix of any shape: Mat >> Transpose(rows: 2 columns: 3) >> Transposed."
---

# Transpose

<span class="stride-badge">Loop</span> `package LinAlg::Matrices` &bull; Namespace: **`LinAlg::Matrices`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Matrices.stride#L275" target="_blank" rel="noopener" title="View source on GitHub">[Matrices.stride:275]</a>

Transposes a matrix of any shape: Mat >> Transpose(rows: 2 columns: 3) >> Transposed.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `MatrixPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Row-major input matrix with `rows` rows and `columns` columns |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Row-major transposed matrix with `columns` rows and `rows` columns. Same size as the input |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>rows</code></span> <span class="prop-default">= <code>2</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>Int</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Number of rows of the input matrix (default 2) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>columns</code></span> <span class="prop-default">= <code>2</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>Int</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Number of columns of the input matrix (default 2) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import LinAlg::Matrices as Matrices;

Signal >> Matrices::Transpose(rows: 2, columns: 2) >> Output;
```
