---
title: Park
description: "Park transform: [Ialpha, Ibeta] >> Park(angle: Theta) >> [Id, Iq]."
---

# Park

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Foc.stride#L41" target="_blank" rel="noopener" title="View source on GitHub">[Foc.stride:41]</a>

Park transform: [Ialpha, Ibeta] >> Park(angle: Theta) >> [Id, Iq].

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» ialphabeta</span> | `IalphabetaPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» idq</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» idq</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» idq</span></span></div> | 2-phase stationary frame currents [Ialpha, Ibeta] |
| <span class="port-badge stream-out">» idq</span> | `IdqPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» idq</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» idq</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» idq</span></span></div> | Rotating direct-quadrature frame currents [Id, Iq] |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ angle</span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» idq</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» idq</span></span></div> | Electrical rotor angle in radians |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import Control;

Signal >> Park(angle: 0.0) >> Output;
```
