---
title: InverseClarke
description: "Inverse Clarke transform: [Valpha, Vbeta] >> InverseClarke() >> [Va, Vb, Vc]."
---

# InverseClarke

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Foc.stride#L147" target="_blank" rel="noopener" title="View source on GitHub">[Foc.stride:147]</a>

Inverse Clarke transform: [Valpha, Vbeta] >> InverseClarke() >> [Va, Vb, Vc].

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `ValphabetaPort` | `VabcPort.type` | `VabcPort.rate` | `VabcPort.domain` | Stationary frame voltages [Valpha, Vbeta] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `VabcPort` | `VabcPort.type` | `VabcPort.rate` | `VabcPort.domain` | 3-phase voltages [Va, Vb, Vc] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Control;

Signal >> InverseClarke() >> Output;
```
