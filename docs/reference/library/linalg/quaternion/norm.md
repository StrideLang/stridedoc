---
title: Norm
description: "Quaternion norm: Q >> Norm() >> Magnitude."
---

# Norm

<span class="stride-badge">Module</span> `package LinAlg::Quaternion` &bull; Namespace: **`LinAlg::Quaternion`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Quaternion.stride#L69" target="_blank" rel="noopener" title="View source on GitHub">[Quaternion.stride:69]</a>

Quaternion norm: Q >> Norm() >> Magnitude.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `QPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Input quaternion [w, x, y, z] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Scalar norm (length) of quaternion |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import LinAlg::Quaternion as Quaternion;

Signal >> Quaternion::Norm() >> Output;
```
