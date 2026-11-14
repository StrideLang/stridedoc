---
title: Park
description: "Park transform: [Ialpha, Ibeta] >> Park(angle: Theta) >> [Id, Iq]."
---

# Park

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Foc.stride#L41" target="_blank" rel="noopener" title="View source on GitHub">[Foc.stride:41]</a>

Park transform: [Ialpha, Ibeta] >> Park(angle: Theta) >> [Id, Iq].

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `IalphabetaPort` | `IdqPort.type` | `IdqPort.rate` | `IdqPort.domain` | 2-phase stationary frame currents [Ialpha, Ibeta] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `IdqPort` | `IdqPort.type` | `IdqPort.rate` | `IdqPort.domain` | Rotating direct-quadrature frame currents [Id, Iq] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `angle` | `IdqPort.type` | `0.0` | — | `IdqPort.domain` | Electrical rotor angle in radians |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Control;

Signal >> Park(angle: 0.0) >> Output;
```
