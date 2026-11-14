---
title: Scale
description: "Scales a vector of any dimension: Vec >> Scale(factor: 2.0) >> Scaled."
---

# Scale

<span class="stride-badge">Loop</span> `package LinAlg::Vectors` &bull; Namespace: **`LinAlg::Vectors`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Vectors.stride#L77" target="_blank" rel="noopener" title="View source on GitHub">[Vectors.stride:77]</a>

Scales a vector of any dimension: Vec >> Scale(factor: 2.0) >> Scaled.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Vector of any size |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Scaled vector, with the same size as the input |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `factor` | `OutputPort.type` | `1.0` | — | `OutputPort.domain` | Scalar factor (default 1.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Vectors as Vectors;

Signal >> Vectors::Scale(factor: 1.0) >> Output;
```
