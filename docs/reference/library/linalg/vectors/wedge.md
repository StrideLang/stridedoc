---
title: Wedge
description: "Wedge (exterior) product of two vectors of any dimension: VecA >> Wedge(with: VecB) >> Bivector. For 2 components the output is the scalar a"
---

# Wedge

<span class="stride-badge">Loop</span> `package LinAlg::Vectors` &bull; Namespace: **`LinAlg::Vectors`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Vectors.stride#L218" target="_blank" rel="noopener" title="View source on GitHub">[Vectors.stride:218]</a>

Wedge (exterior) product of two vectors of any dimension: VecA >> Wedge(with: VecB) >> Bivector. For 2 components the output is the scalar a0 b1 - a1 b0 (the 2D cross product); for 3 components it holds the cross product components [x y z] = [w(1,2), -w(0,2), w(0,1)] of the output w; for n components it has n (n - 1) / 2 components.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorAPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | First vector with n components. n is the size of this port |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | The n * (n - 1) / 2 components a[i] * b[j] - a[j] * b[i], one for each pair of axes i < j, in lexicographic order: (0,1), (0,2), ..., (1,2), ... The size of this port must be n * (n - 1) / 2 |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `with` | `OutputPort.type` | — | — | `OutputPort.domain` | Second vector, with the same size as the first |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Vectors as Vectors;

Signal >> Vectors::Wedge(with: ...) >> Output;
```
