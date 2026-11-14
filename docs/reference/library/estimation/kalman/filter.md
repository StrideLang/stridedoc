---
title: Filter
description: "1D recursive Kalman filter: NoisySignal >> Kalman::Filter(q: 0.01 r: 0.1) >> FilteredSignal. q is a variance per second and is converted aga"
---

# Filter

<span class="stride-badge">Module</span> `package Estimation::Kalman` &bull; Namespace: **`Estimation::Kalman`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Estimation/Kalman.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Kalman.stride:8]</a>

1D recursive Kalman filter: NoisySignal >> Kalman::Filter(q: 0.01 r: 0.1) >> FilteredSignal. q is a variance per second and is converted against the rate of the output, so the filter behaves the same at any sample rate. Type must be floating point.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Noisy sensor measurement stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Optimal filtered state estimate |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `q` | `OutputPort.type` | `0.01` | — | `OutputPort.domain` | Process noise: the variance the state gains per second (default 0.01). Converted to a per-tick variance with the rate of the output |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `r` | `OutputPort.type` | `0.1` | — | `OutputPort.domain` | Measurement noise variance of every sample (default 0.1) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `initialX` | `OutputPort.type` | `0.0` | — | `OutputPort.domain` | Initial state estimate (default 0.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `initialP` | `OutputPort.type` | `1.0` | — | `OutputPort.domain` | Initial estimation error covariance (default 1.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Estimation::Kalman as Kalman;

Signal >> Kalman::Filter(q: 0.01, r: 0.1, initialX: 0.0) >> Output;
```
