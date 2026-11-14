---
title: InversePark
description: "Inverse Park transform: [Vd, Vq] >> InversePark(angle: Theta) >> [Valpha, Vbeta]."
---

# InversePark

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Foc.stride#L94" target="_blank" rel="noopener" title="View source on GitHub">[Foc.stride:94]</a>

Inverse Park transform: [Vd, Vq] >> InversePark(angle: Theta) >> [Valpha, Vbeta].

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `VdqPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>ValphabetaPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>ValphabetaPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>ValphabetaPort.domain</code></span></div> | Rotating direct-quadrature frame voltages [Vd, Vq] |
| <span class="port-badge stream-out">» Out</span> | `ValphabetaPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>ValphabetaPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>ValphabetaPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>ValphabetaPort.domain</code></span></div> | Stationary frame voltages [Valpha, Vbeta] |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>angle</code></span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>ValphabetaPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>ValphabetaPort.domain</code></span></div> | Electrical rotor angle in radians |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Control;

Signal >> InversePark(angle: 0.0) >> Output;
```
