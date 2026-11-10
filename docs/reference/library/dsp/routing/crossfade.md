---
title: Crossfade
description: "Linear crossfade between two audio streams."
---

# Crossfade

<span class="stride-badge">Module</span> `package Dsp::Routing` &bull; Namespace: **`Dsp::Routing`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Routing.stride#L96" target="_blank" rel="noopener" title="View source on GitHub">[Routing.stride:96]</a>

Linear crossfade between two audio streams.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputAPort` | `signal` | — | `InputAPort.domain` | Primary input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | `OutputPort.domain` | Crossfaded output stream |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `with` | `signal` | — | — | `WithPort.domain` | Secondary input signal to blend with |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `mix` | `signal` | `0.5` | — | `MixPort.domain` | Crossfade blend ratio from 0.0 (input) to 1.0 (with) |

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
