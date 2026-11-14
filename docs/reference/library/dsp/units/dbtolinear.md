---
title: DbToLinear
description: "Converts decibels (dB) to linear amplitude ratio."
---

# DbToLinear

<span class="stride-badge">Module</span> `package Dsp::Units` &bull; Namespace: **`Dsp::Units`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Units.stride#L91" target="_blank" rel="noopener" title="View source on GitHub">[Units.stride:91]</a>

Converts decibels (dB) to linear amplitude ratio.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `DbPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>LinearPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>DbPort.domain</code></span></div> | Amplitude in decibels (dB) |
| <span class="port-badge stream-out">» Out</span> | `LinearPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>LinearPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>LinearPort.domain</code></span></div> | Linear amplitude ratio |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Units as Units;

Signal >> Units::DbToLinear() >> Output;
```
