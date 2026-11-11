---
title: Clarke
description: "Clarke transform: 3-phase currents [Ia, Ib, Ic] >> Clarke() >> [Ialpha, Ibeta]."
---

# Clarke

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Foc.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Foc.stride:8]</a>

Clarke transform: 3-phase currents [Ia, Ib, Ic] >> Clarke() >> [Ialpha, Ibeta].

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `IabcPort` | `signal` | `IalphabetaPort.rate` | `IalphabetaPort.domain` | 3-phase input currents [Ia, Ib, Ic] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `IalphabetaPort` | `signal` | `IalphabetaPort.rate` | `IalphabetaPort.domain` | 2-phase stationary frame currents [Ialpha, Ibeta] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Control;

Signal >> Clarke() >> Output;
```
