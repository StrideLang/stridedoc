---
title: Clarke
description: "Clarke transform: 3-phase currents [Ia, Ib, Ic] >> Clarke() >> [Ialpha, Ibeta]."
---

# Clarke

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Foc.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Foc.stride:8]</a>

Clarke transform: 3-phase currents [Ia, Ib, Ic] >> Clarke() >> [Ialpha, Ibeta].

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `IabcPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>IalphabetaPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>IalphabetaPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>IalphabetaPort.domain</code></span></div> | 3-phase input currents [Ia, Ib, Ic] |
| <span class="port-badge stream-out">» Out</span> | `IalphabetaPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>IalphabetaPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>IalphabetaPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>IalphabetaPort.domain</code></span></div> | 2-phase stationary frame currents [Ialpha, Ibeta] |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Control;

Signal >> Clarke() >> Output;
```
