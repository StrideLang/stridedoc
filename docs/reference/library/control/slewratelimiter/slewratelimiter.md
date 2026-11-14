---
title: SlewRateLimiter
description: "Limits the rate of change of a signal in units per second: Input >> SlewRateLimiter(up: 2.0 down: 5.0) >> Output. The limits are converted a"
---

# SlewRateLimiter

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/SlewRateLimiter.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[SlewRateLimiter.stride:7]</a>

Limits the rate of change of a signal in units per second: Input >> SlewRateLimiter(up: 2.0 down: 5.0) >> Output. The limits are converted against the rate of the output, so they do not change with the sample rate.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Rate-limited output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `up` | `OutputPort.type` | `1.0` | — | `OutputPort.domain` | Maximum rising rate in signal units per second (default 1.0) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `down` | `OutputPort.type` | `1.0` | — | `OutputPort.domain` | Maximum falling rate in signal units per second, given as a positive number (default 1.0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Control;

Signal >> SlewRateLimiter(up: 1.0, down: 1.0) >> Output;
```
