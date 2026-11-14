---
title: TableOscillator
description: "Table read oscillator."
---

# TableOscillator

<span class="stride-badge">Module</span> `package Dsp::Generators` &bull; Namespace: **`Dsp::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Generators/TableOscillator.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[TableOscillator.stride:7]</a>

Table read oscillator.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span></div> | — |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>frequency</code></span> <span class="prop-default">= <code>440.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span></div> | The frequency of the oscillator. |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>amplitude</code></span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span></div> | The amplitude of the oscillator. |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>phase</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span></div> | The starting phase of the oscillator. |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>reset</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span></div> | Resets the oscillator to the starting phase. |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Generators as Generators;

Signal >> Generators::TableOscillator(frequency: 440.0, amplitude: 1.0, phase: ...) >> Output;
```
