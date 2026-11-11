---
title: Multiply
description: "Quaternion Hamilton product: Q1 >> Multiply(with: Q2) >> QProduct."
---

# Multiply

<span class="stride-badge">Module</span> `package LinAlg::Quaternion` &bull; Namespace: **`LinAlg::Quaternion`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Quaternion.stride#L9" target="_blank" rel="noopener" title="View source on GitHub">[Quaternion.stride:9]</a>

Quaternion Hamilton product: Q1 >> Multiply(with: Q2) >> QProduct.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `Q1Port` | `signal` | `OutputPort.rate` | `OutputPort.domain` | First quaternion [w1, x1, y1, z1] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Product quaternion [w, x, y, z] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `with` | `signal` | — | — | `OutputPort.domain` | Second quaternion [w2, x2, y2, z2] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Quaternion as Quaternion;

Signal >> Quaternion::Multiply(with: ...) >> Output;
```
