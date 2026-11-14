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
| <span class="port-badge stream-in">» vdq</span> | `VdqPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» valphabeta</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» valphabeta</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» valphabeta</span></span></div> | Rotating direct-quadrature frame voltages [Vd, Vq] |
| <span class="port-badge stream-out">» valphabeta</span> | `ValphabetaPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» valphabeta</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» valphabeta</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» valphabeta</span></span></div> | Stationary frame voltages [Valpha, Vbeta] |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ angle</span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» valphabeta</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» valphabeta</span></span></div> | Electrical rotor angle in radians |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import Control;

Signal >> InversePark(angle: 0.0) >> Output;
```
