---
title: ComplementaryFilter
description: "IMU sensor fusion blending gyro rate and accelerometer tilt: GyroRate >> ComplementaryFilter(accelAngle: AccelTilt timeConstant: 0.5) >> Fus"
---

# ComplementaryFilter

<span class="stride-badge">Module</span> `package Sensors::Conditioning` &bull; Namespace: **`Sensors::Conditioning`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Sensors/Conditioning.stride#L217" target="_blank" rel="noopener" title="View source on GitHub">[Conditioning.stride:217]</a>

IMU sensor fusion blending gyro rate and accelerometer tilt: GyroRate >> ComplementaryFilter(accelAngle: AccelTilt timeConstant: 0.5) >> FusedAngle. The sample interval and the blend factor are derived from the rate of the output; the type must be floating point.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `GyroPort` | `AnglePort.type` | `AnglePort.rate` | `AnglePort.domain` | Angular velocity from gyroscope in angle units per second (e.g. rad/s) |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `AnglePort` | `AnglePort.type` | `AnglePort.rate` | `AnglePort.domain` | Fused estimated angle |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `accelAngle` | `AnglePort.type` | `0.0` | — | `AnglePort.domain` | Static tilt angle from accelerometer, in the same angle unit |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `timeConstant` | `AnglePort.type` | `0.5` | — | `AnglePort.domain` | Crossover time in seconds: for changes slower than this the accelerometer is trusted, for faster changes the gyroscope (default 0.5) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Sensors::Conditioning as Conditioning;

Signal >> Conditioning::ComplementaryFilter(accelAngle: 0.0, timeConstant: 0.5) >> Output;
```
