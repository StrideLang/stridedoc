---
title: Wedge
description: "Wedge (exterior) product of two vectors of any dimension: VecA >> Wedge(with: VecB) >> Bivector. For 2 components the output is the scalar a"
---

# Wedge

<span class="stride-badge">Loop</span> `package LinAlg::Vectors` &bull; Namespace: **`LinAlg::Vectors`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Vectors.stride#L218" target="_blank" rel="noopener" title="View source on GitHub">[Vectors.stride:218]</a>

Wedge (exterior) product of two vectors of any dimension: VecA >> Wedge(with: VecB) >> Bivector. For 2 components the output is the scalar a0 b1 - a1 b0 (the 2D cross product); for 3 components it holds the cross product components [x y z] = [w(1,2), -w(0,2), w(0,1)] of the output w; for n components it has n (n - 1) / 2 components.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» a</span> | `VectorAPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | First vector with n components. n is the size of this port |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | The n * (n - 1) / 2 components a[i] * b[j] - a[j] * b[i], one for each pair of axes i < j, in lexicographic order: (0,1), (0,2), ..., (1,2), ... The size of this port must be n * (n - 1) / 2 |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ with</span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Second vector, with the same size as the first |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import LinAlg::Vectors as Vectors;

Signal >> Vectors::Wedge(with: ...) >> Output;
```
