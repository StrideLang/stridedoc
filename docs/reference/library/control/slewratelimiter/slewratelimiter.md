---
title: SlewRateLimiter
description: "Limits the maximum rate of change (slope) per sample step: Input >> SlewRateLimiter(up: 0.01 down: 0.01) >> Output."
---

# SlewRateLimiter

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/SlewRateLimiter.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[SlewRateLimiter.stride:7]</a>

Limits the maximum rate of change (slope) per sample step: Input >> SlewRateLimiter(up: 0.01 down: 0.01) >> Output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Input signal to limit in slope |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Slew-limited output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `up` | `signal` | `0.01` | — | `OutputPort.domain` | Maximum positive change per sample step |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `down` | `signal` | `0.01` | — | `OutputPort.domain` | Maximum negative change per sample step (positive value) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Control;

Signal >> SlewRateLimiter(up: 0.01, down: 0.01) >> Output;
```
