---
title: Rotate
description: "Rotates a 3D vector by orientation quaternion: Vec3D >> Quaternion::Rotate(rotation: Quat) >> RotatedVec. Rotation in space is three dimensi"
---

# Rotate

<span class="stride-badge">Module</span> `package LinAlg::Quaternion` &bull; Namespace: **`LinAlg::Quaternion`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Quaternion.stride#L73" target="_blank" rel="noopener" title="View source on GitHub">[Quaternion.stride:73]</a>

Rotates a 3D vector by orientation quaternion: Vec3D >> Quaternion::Rotate(rotation: Quat) >> RotatedVec. Rotation in space is three dimensional, so the vector has 3 components.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» vector</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | 3D vector to rotate [x, y, z] |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Rotated 3D vector [x, y, z] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge stream-in">» In</span> Stream Input</span>
  <span class="port-legend-item"><span class="port-badge stream-out">» Out</span> Stream Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ rotation</span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Unit orientation quaternion [w, x, y, z] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import LinAlg::Quaternion as Quaternion;

Signal >> Quaternion::Rotate(rotation: ...) >> Output;
```
