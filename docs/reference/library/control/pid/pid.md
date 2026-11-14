---
title: Pid
description: "Proportional-Integral-Derivative controller with anti-windup clamping: Error >> Pid(kp: 1.0 ki: 0.05 kd: 0.1) >> Output. ki (per second) and"
---

# Pid

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Pid.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Pid.stride:7]</a>

Proportional-Integral-Derivative controller with anti-windup clamping: Error >> Pid(kp: 1.0 ki: 0.05 kd: 0.1) >> Output. ki (per second) and kd (seconds) are converted against the rate of the output, so tuning does not change with the sample rate. Type must be floating point.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `ErrorPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Error signal (Setpoint - ProcessVariable) |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Control variable output signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>kp</code></span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Proportional gain, in output units per error unit (default 1.0) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>ki</code></span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Integral gain, in output units per error unit per second (default 0.0) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>kd</code></span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Derivative gain, in output units per error unit per second of change, i.e. kd is a time in seconds (default 0.0) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>min</code></span> <span class="prop-default">= <code>-1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Minimum saturation limit for integrator and output (default -1.0) |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>max</code></span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Maximum saturation limit for integrator and output (default 1.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Control;

Signal >> Pid(kp: 1.0, ki: 0.0, kd: 0.0) >> Output;
```
