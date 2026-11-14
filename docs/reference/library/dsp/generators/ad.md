---
title: AD
description: "Attack-Decay envelope generator."
---

# AD

<span class="stride-badge">Module</span> `package Dsp::Generators` &bull; Namespace: **`Dsp::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Generators/Envelope.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Envelope.stride:7]</a>

Attack-Decay envelope generator.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span></div> | The module's primary output port. |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>trigger</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Triggers the envelope |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>attack</code></span> <span class="prop-default">= <code>0.2</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span></div> | Attack time in seconds |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>decay</code></span> <span class="prop-default">= <code>3.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span></div> | Decay time in seconds |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Generators as Generators;

Signal >> Generators::AD(attack: 0.2, decay: 3.0) >> Output;
```
