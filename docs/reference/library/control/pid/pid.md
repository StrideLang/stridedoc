---
title: Pid
description: "Proportional-Integral-Derivative controller with anti-windup clamping: Error >> Pid(kp: 1.0 ki: 0.05 kd: 0.1) >> Output. ki (per second) and"
---

# Pid

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Pid.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Pid.stride:7]</a>

Proportional-Integral-Derivative controller with anti-windup clamping: Error >> Pid(kp: 1.0 ki: 0.05 kd: 0.1) >> Output. ki (per second) and kd (seconds) are converted against the rate of the output, so tuning does not change with the sample rate. Type must be floating point.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Error signal (Setpoint - ProcessVariable) |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Control variable output signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ kp</span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Proportional gain, in output units per error unit (default 1.0) |
| <span class="port-badge prop-in">↓ ki</span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Integral gain, in output units per error unit per second (default 0.0) |
| <span class="port-badge prop-in">↓ kd</span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Derivative gain, in output units per error unit per second of change, i.e. kd is a time in seconds (default 0.0) |
| <span class="port-badge prop-in">↓ min</span> <span class="prop-default">= <code>-1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Minimum saturation limit for integrator and output (default -1.0) |
| <span class="port-badge prop-in">↓ max</span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Maximum saturation limit for integrator and output (default 1.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import Control;

Signal >> Pid(kp: 1.0, ki: 0.0, kd: 0.0) >> Output;
```
