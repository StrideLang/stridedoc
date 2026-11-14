---
title: ComplementaryFilter
description: "IMU sensor fusion blending gyro rate and accelerometer tilt: GyroRate >> ComplementaryFilter(accelAngle: AccelTilt timeConstant: 0.5) >> Fus"
---

# ComplementaryFilter

<span class="stride-badge">Module</span> `package Sensors::Conditioning` &bull; Namespace: **`Sensors::Conditioning`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Sensors/Conditioning.stride#L217" target="_blank" rel="noopener" title="View source on GitHub">[Conditioning.stride:217]</a>

IMU sensor fusion blending gyro rate and accelerometer tilt: GyroRate >> ComplementaryFilter(accelAngle: AccelTilt timeConstant: 0.5) >> FusedAngle. The sample interval and the blend factor are derived from the rate of the output; the type must be floating point.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `GyroPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>AnglePort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>AnglePort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>AnglePort.domain</code></span></div> | Angular velocity from gyroscope in angle units per second (e.g. rad/s) |
| <span class="port-badge stream-out">» Out</span> | `AnglePort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>AnglePort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>AnglePort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>AnglePort.domain</code></span></div> | Fused estimated angle |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>accelAngle</code></span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>AnglePort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>AnglePort.domain</code></span></div> | Static tilt angle from accelerometer, in the same angle unit |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>timeConstant</code></span> <span class="prop-default">= <code>0.5</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>AnglePort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>AnglePort.domain</code></span></div> | Crossover time in seconds: for changes slower than this the accelerometer is trusted, for faster changes the gyroscope (default 0.5) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Sensors::Conditioning as Conditioning;

Signal >> Conditioning::ComplementaryFilter(accelAngle: 0.0, timeConstant: 0.5) >> Output;
```
