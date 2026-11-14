---
title: Detector
description: "Real-time local maximum detector with a switch output: Input >> PeakDetector::Detector(threshold: 0.5) >> Peak."
---

# Detector

<span class="stride-badge">Module</span> `package Estimation::PeakDetector` &bull; Namespace: **`Estimation::PeakDetector`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Estimation/PeakDetector.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[PeakDetector.stride:8]</a>

Real-time local maximum detector with a switch output: Input >> PeakDetector::Detector(threshold: 0.5) >> Peak.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-in">» In</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Input signal stream to monitor for peaks |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>switch</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Switch that is on for one tick when a peak was detected. The detection is made one tick late, as a peak can only be confirmed by the sample that follows it |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ threshold</span> <span class="prop-default">= <code>0.5</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-in">» In</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Minimum peak amplitude threshold (default 0.5) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import Estimation::PeakDetector as PeakDetector;

Signal >> PeakDetector::Detector(threshold: 0.5) >> Output;
```
