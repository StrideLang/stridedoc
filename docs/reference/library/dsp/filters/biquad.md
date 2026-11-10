---
title: BiQuad
description: "Direct Form II Transposed 2nd-order IIR BiQuad filter."
---

# BiQuad

<span class="stride-badge">Module</span> `package Dsp::Filters` &bull; Namespace: **`Dsp::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/BiQuad.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[BiQuad.stride:7]</a>

Direct Form II Transposed 2nd-order IIR BiQuad filter.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `MainInputPort` | `signal` | — | `MainInputPort.domain` | — |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | `OutputPort.domain` | — |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `centerFrequency` | `signal` | — | — | — | The center frequency of the filter. |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `resonance` | `signal` | `50` | — | — | Resonance (Q) amount. Should be greater than or equal to 1.0. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Filters as Filters;

Signal >> Filters::BiQuad(centerFrequency: ..., resonance: 50) >> Output;
```
