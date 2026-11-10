---
title: Pan
description: "Stereo panner splitting a mono signal into stereo left [0] and right [1]."
---

# Pan

<span class="stride-badge">Module</span> `package Dsp::Routing` &bull; Namespace: **`Dsp::Routing`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Routing.stride#L62" target="_blank" rel="noopener" title="View source on GitHub">[Routing.stride:62]</a>

Stereo panner splitting a mono signal into stereo left [0] and right [1].

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | — | — | Mono input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | — | Stereo output signal bundle [left, right] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `position` | `signal` | `0.0` | — | `PositionPort.domain` | Sets the stereo panning position in range [-1.0, 1.0]. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Routing as Routing;

Signal >> Routing::Pan(position: 0.0) >> Output;
```
