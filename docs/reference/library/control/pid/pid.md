---
title: Pid
description: "Proportional-Integral-Derivative controller with anti-windup clamping: Error >> Pid(kp: 1.0 ki: 0.05 kd: 0.1) >> Output. ki (per second) and"
---

# Pid

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Pid.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Pid.stride:7]</a>

Proportional-Integral-Derivative controller with anti-windup clamping: Error >> Pid(kp: 1.0 ki: 0.05 kd: 0.1) >> Output. ki (per second) and kd (seconds) are converted against the rate of the output, so tuning does not change with the sample rate. Type must be floating point.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `ErrorPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Error signal (Setpoint - ProcessVariable) |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Control variable output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `kp` | `OutputPort.type` | `1.0` | — | `OutputPort.domain` | Proportional gain, in output units per error unit (default 1.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `ki` | `OutputPort.type` | `0.0` | — | `OutputPort.domain` | Integral gain, in output units per error unit per second (default 0.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `kd` | `OutputPort.type` | `0.0` | — | `OutputPort.domain` | Derivative gain, in output units per error unit per second of change, i.e. kd is a time in seconds (default 0.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `min` | `OutputPort.type` | `-1.0` | — | `OutputPort.domain` | Minimum saturation limit for integrator and output (default -1.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `max` | `OutputPort.type` | `1.0` | — | `OutputPort.domain` | Maximum saturation limit for integrator and output (default 1.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Control;

Signal >> Pid(kp: 1.0, ki: 0.0, kd: 0.0) >> Output;
```
