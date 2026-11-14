---
title: Rotate
description: "Rotates a 3D vector by orientation quaternion: Vec3D >> Quaternion::Rotate(rotation: Quat) >> RotatedVec. Rotation in space is three dimensi"
---

# Rotate

<span class="stride-badge">Module</span> `package LinAlg::Quaternion` &bull; Namespace: **`LinAlg::Quaternion`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Quaternion.stride#L73" target="_blank" rel="noopener" title="View source on GitHub">[Quaternion.stride:73]</a>

Rotates a 3D vector by orientation quaternion: Vec3D >> Quaternion::Rotate(rotation: Quat) >> RotatedVec. Rotation in space is three dimensional, so the vector has 3 components.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | 3D vector to rotate [x, y, z] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Rotated 3D vector [x, y, z] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `rotation` | `OutputPort.type` | — | — | `OutputPort.domain` | Unit orientation quaternion [w, x, y, z] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Quaternion as Quaternion;

Signal >> Quaternion::Rotate(rotation: ...) >> Output;
```
