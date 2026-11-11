---
title: Detector
description: "Detects local peaks exceeding a minimum threshold: Signal >> PeakDetector::Detector(threshold: 0.5) >> Peaks."
---

# Detector

<span class="stride-badge">Module</span> `package Estimation::PeakDetector` &bull; Namespace: **`Estimation::PeakDetector`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Estimation/PeakDetector.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[PeakDetector.stride:8]</a>

Detects local peaks exceeding a minimum threshold: Signal >> PeakDetector::Detector(threshold: 0.5) >> Peaks.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Input signal stream to monitor for peaks |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Binary impulse (1.0 upon peak detection, 0.0 otherwise) |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `threshold` | `signal` | `0.5` | — | `OutputPort.domain` | Minimum peak amplitude threshold |

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
