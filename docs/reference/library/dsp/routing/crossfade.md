---
title: Crossfade
description: "Linear crossfade between two audio streams."
---

# Crossfade

<span class="stride-badge">Module</span> `package Dsp::Routing` &bull; Namespace: **`Dsp::Routing`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Routing.stride#L112" target="_blank" rel="noopener" title="View source on GitHub">[Routing.stride:112]</a>

Linear crossfade between two audio streams.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputAPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Primary input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Crossfaded output stream |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `with` | `OutputPort.type` | — | `OutputPort.rate` | `OutputPort.domain` | Secondary input signal to blend with |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `mix` | `OutputPort.type` | `0.5` | — | `OutputPort.domain` | Crossfade blend ratio from 0.0 (input) to 1.0 (with) (default 0.5) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Routing as Routing;

Signal >> Routing::Crossfade(with: ..., mix: 0.5) >> Output;
```
