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
| <span class="port-badge stream-in">» gyroRate</span> | `GyroPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» angle</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» angle</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» angle</span></span></div> | Angular velocity from gyroscope in angle units per second (e.g. rad/s) |
| <span class="port-badge stream-out">» angle</span> | `AnglePort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» angle</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» angle</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» angle</span></span></div> | Fused estimated angle |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ accelAngle</span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» angle</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» angle</span></span></div> | Static tilt angle from accelerometer, in the same angle unit |
| <span class="port-badge prop-in">↓ timeConstant</span> <span class="prop-default">= <code>0.5</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» angle</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» angle</span></span></div> | Crossover time in seconds: for changes slower than this the accelerometer is trusted, for faster changes the gyroscope (default 0.5) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import Sensors::Conditioning as Conditioning;

Signal >> Conditioning::ComplementaryFilter(accelAngle: 0.0, timeConstant: 0.5) >> Output;
```
