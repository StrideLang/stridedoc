---
title: Detector
description: "Real-time local maximum detector with a switch output: Input >> PeakDetector::Detector(threshold: 0.5) >> Peak."
---

# Detector

<span class="stride-badge">Module</span> `package Estimation::PeakDetector` &bull; Namespace: **`Estimation::PeakDetector`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Estimation/PeakDetector.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[PeakDetector.stride:8]</a>

Real-time local maximum detector with a switch output: Input >> PeakDetector::Detector(threshold: 0.5) >> Peak.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `InputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal stream to monitor for peaks |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Switch that is on for one tick when a peak was detected. The detection is made one tick late, as a peak can only be confirmed by the sample that follows it |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `threshold` | `InputPort.type` | `0.5` | — | `OutputPort.domain` | Minimum peak amplitude threshold (default 0.5) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Estimation::PeakDetector as PeakDetector;

Signal >> PeakDetector::Detector(threshold: 0.5) >> Output;
```
