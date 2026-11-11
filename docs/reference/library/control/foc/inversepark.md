---
title: InversePark
description: "Inverse Park transform: [Vd, Vq] >> InversePark(angle: Theta) >> [Valpha, Vbeta]."
---

# InversePark

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Foc.stride#L87" target="_blank" rel="noopener" title="View source on GitHub">[Foc.stride:87]</a>

Inverse Park transform: [Vd, Vq] >> InversePark(angle: Theta) >> [Valpha, Vbeta].

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `VdqPort` | `signal` | `ValphabetaPort.rate` | `ValphabetaPort.domain` | Rotating direct-quadrature frame voltages [Vd, Vq] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `ValphabetaPort` | `signal` | `ValphabetaPort.rate` | `ValphabetaPort.domain` | Stationary frame voltages [Valpha, Vbeta] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `angle` | `signal` | `0.0` | — | `ValphabetaPort.domain` | Electrical rotor angle in radians |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Control;

Signal >> InversePark(angle: 0.0) >> Output;
```
