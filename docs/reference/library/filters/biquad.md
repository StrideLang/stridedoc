---
title: BiQuad
description: "BiQuad filter"
---

# BiQuad

<span class="stride-badge">Module</span> `package Stride::Filters` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Filters/BiQuad.stride#L2" target="_blank" rel="noopener" title="View source on GitHub">[BiQuad.stride:2]</a>

BiQuad filter

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `MainInputPort` | `Input` | — | — |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | — |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `centerFrequency` | `CenterFrequency` | — | The center frequency of the filter. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `resonance` | `Resonance` | — | Resonance (Q) amount. Should be greater than on equal to 1.0. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Resonance` | `signal` | `50` | — | — |

## Usage

```stride
import Stride;

# Access via Filters category:
Signal >> Filters::BiQuad(centerFrequency: ..., resonance: ...) >> Output;
```
