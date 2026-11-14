---
title: Filter
description: "1D recursive Kalman filter: NoisySignal >> Kalman::Filter(q: 0.01 r: 0.1) >> FilteredSignal. q is a variance per second and is converted aga"
---

# Filter

<span class="stride-badge">Module</span> `package Estimation::Kalman` &bull; Namespace: **`Estimation::Kalman`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Estimation/Kalman.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Kalman.stride:8]</a>

1D recursive Kalman filter: NoisySignal >> Kalman::Filter(q: 0.01 r: 0.1) >> FilteredSignal. q is a variance per second and is converted against the rate of the output, so the filter behaves the same at any sample rate. Type must be floating point.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Noisy sensor measurement stream |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Optimal filtered state estimate |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ q</span> <span class="prop-default">= <code>0.01</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Process noise: the variance the state gains per second (default 0.01). Converted to a per-tick variance with the rate of the output |
| <span class="port-badge prop-in">↓ r</span> <span class="prop-default">= <code>0.1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Measurement noise variance of every sample (default 0.1) |
| <span class="port-badge prop-in">↓ initialX</span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Initial state estimate (default 0.0) |
| <span class="port-badge prop-in">↓ initialP</span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Initial estimation error covariance (default 1.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import Estimation::Kalman as Kalman;

Signal >> Kalman::Filter(q: 0.01, r: 0.1, initialX: 0.0) >> Output;
```
