---
title: Watch
description: "Signal watch module for non-intrusive runtime observation"
---

# Watch

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Debug** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Debug.stride#L76" target="_blank" rel="noopener" title="View source on GitHub">[Debug.stride:76]</a>

Signal watch module for non-intrusive runtime observation

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | — | — | Signal to be watched and passed through |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | — | Pass-through of the input signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `label` | `signal` | — | — | — | — |

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
Signal >> Watch(label: ...) >> Output;
```
