---
title: Fast
description: "Hard peak clamping limiter: AudioIn >> Limiter::Fast(threshold: 0.95) >> Out."
---

# Fast

<span class="stride-badge">Module</span> `package Dsp::Dynamics::Limiter` &bull; Namespace: **`Dsp::Dynamics::Limiter`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Dynamics/Limiter.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Limiter.stride:8]</a>

Hard peak clamping limiter: AudioIn >> Limiter::Fast(threshold: 0.95) >> Out.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input audio signal stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Peak-limited audio signal stream |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `threshold` | `OutputPort.type` | `0.95` | — | `OutputPort.domain` | Maximum peak ceiling amplitude (default 0.95) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Dynamics::Limiter as Limiter;

Signal >> Limiter::Fast(threshold: 0.95) >> Output;
```
