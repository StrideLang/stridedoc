---
title: InverseClarke
description: "Inverse Clarke transform: [Valpha, Vbeta] >> InverseClarke() >> [Va, Vb, Vc]."
---

# InverseClarke

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Foc.stride#L147" target="_blank" rel="noopener" title="View source on GitHub">[Foc.stride:147]</a>

Inverse Clarke transform: [Valpha, Vbeta] >> InverseClarke() >> [Va, Vb, Vc].

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `ValphabetaPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>VabcPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>VabcPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>VabcPort.domain</code></span></div> | Stationary frame voltages [Valpha, Vbeta] |
| <span class="port-badge stream-out">» Out</span> | `VabcPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>VabcPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>VabcPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>VabcPort.domain</code></span></div> | 3-phase voltages [Va, Vb, Vc] |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Control;

Signal >> InverseClarke() >> Output;
```
