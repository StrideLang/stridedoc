---
title: RotateVector3D
description: "Rotates a 3D vector by orientation quaternion: Vec3D >> RotateVector3D(rotation: Quat) >> RotatedVec."
---

# RotateVector3D

<span class="stride-badge">Module</span> `package LinAlg::Quaternion` &bull; Namespace: **`LinAlg::Quaternion`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Quaternion.stride#L95" target="_blank" rel="noopener" title="View source on GitHub">[Quaternion.stride:95]</a>

Rotates a 3D vector by orientation quaternion: Vec3D >> RotateVector3D(rotation: Quat) >> RotatedVec.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VectorPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | 3D vector to rotate [x, y, z] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Rotated 3D vector [x, y, z] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `rotation` | `signal` | — | — | `OutputPort.domain` | Unit orientation quaternion [w, x, y, z] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import LinAlg::Quaternion as Quaternion;

Signal >> Quaternion::RotateVector3D(rotation: ...) >> Output;
```
