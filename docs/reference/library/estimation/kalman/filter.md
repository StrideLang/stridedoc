---
title: Filter
description: "1D recursive Kalman filter: NoisySignal >> Kalman::Filter(q: 0.01 r: 0.1) >> FilteredSignal."
---

# Filter

<span class="stride-badge">Module</span> `package Estimation::Kalman` &bull; Namespace: **`Estimation::Kalman`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Estimation/Kalman.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Kalman.stride:8]</a>

1D recursive Kalman filter: NoisySignal >> Kalman::Filter(q: 0.01 r: 0.1) >> FilteredSignal.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Noisy sensor measurement stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Optimal filtered state estimate |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `q` | `signal` | `0.01` | — | `OutputPort.domain` | Process noise covariance (variance) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `r` | `signal` | `0.1` | — | `OutputPort.domain` | Measurement noise covariance (variance) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `initialX` | `signal` | `0.0` | — | `OutputPort.domain` | Initial state estimate |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `initialP` | `signal` | `1.0` | — | `OutputPort.domain` | Initial estimation error covariance |

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
