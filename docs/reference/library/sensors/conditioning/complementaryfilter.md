---
title: ComplementaryFilter
description: "IMU sensor fusion blending gyro rate and accelerometer tilt: GyroRate >> ComplementaryFilter(accelAngle: AccelTilt alpha: 0.98 dt: 0.01) >> "
---

# ComplementaryFilter

<span class="stride-badge">Module</span> `package Sensors::Conditioning` &bull; Namespace: **`Sensors::Conditioning`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Sensors/Conditioning.stride#L205" target="_blank" rel="noopener" title="View source on GitHub">[Conditioning.stride:205]</a>

IMU sensor fusion blending gyro rate and accelerometer tilt: GyroRate >> ComplementaryFilter(accelAngle: AccelTilt alpha: 0.98 dt: 0.01) >> FusedAngle.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `GyroPort` | `signal` | `AnglePort.rate` | `AnglePort.domain` | Angular velocity from gyroscope in deg/s or rad/s |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `AnglePort` | `signal` | `AnglePort.rate` | `AnglePort.domain` | Fused estimated angle |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `accelAngle` | `signal` | `0.0` | — | `AnglePort.domain` | Static tilt angle from accelerometer |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `alpha` | `signal` | `0.98` | — | `AnglePort.domain` | Filter blending weighting factor (default 0.98) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `dt` | `signal` | `0.01` | — | `AnglePort.domain` | Sample time interval in seconds (e.g., 0.01 for 100 Hz) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Sensors::Conditioning as Conditioning;

Signal >> Conditioning::ComplementaryFilter(accelAngle: 0.0, alpha: 0.98, dt: 0.01) >> Output;
```
