---
title: Dot
description: "Dot product of two vectors of any dimension: VecA >> Dot(with: VecB) >> Result. The dimension is the size of the input."
---

# Dot

<span class="stride-badge">Loop</span> `package LinAlg::Vectors` &bull; Namespace: **`LinAlg::Vectors`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Vectors.stride#L19" target="_blank" rel="noopener" title="View source on GitHub">[Vectors.stride:19]</a>

Dot product of two vectors of any dimension: VecA >> Dot(with: VecB) >> Result. The dimension is the size of the input.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorAPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | First vector, of any size |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Scalar dot product result |

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

Signal >> Vectors::Dot(with: ...) >> Output;
```
