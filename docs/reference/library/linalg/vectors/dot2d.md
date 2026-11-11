---
title: Dot2D
description: "2D Vector dot product: VecA >> Dot2D(with: VecB) >> Result."
---

# Dot2D

<span class="stride-badge">Module</span> `package LinAlg::Vectors` &bull; Namespace: **`LinAlg::Vectors`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Vectors.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Vectors.stride:8]</a>

2D Vector dot product: VecA >> Dot2D(with: VecB) >> Result.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorAPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | First 2D vector [x, y] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Scalar dot product result |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `with` | `signal` | — | — | `OutputPort.domain` | Second 2D vector [x, y] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Vectors as Vectors;

Signal >> Vectors::Dot2D(with: ...) >> Output;
```
