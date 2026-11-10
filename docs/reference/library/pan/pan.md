---
title: Pan
description: "Stereo panner."
---

# Pan

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Pan** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Pan.stride#L2" target="_blank" rel="noopener" title="View source on GitHub">[Pan.stride:2]</a>

Stereo panner.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | — | — |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | — | — | — |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `position` | `signal` | — | — | — | Sets the panning position with range [-1, 1]. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Pan(position: ...) >> Output;
```
