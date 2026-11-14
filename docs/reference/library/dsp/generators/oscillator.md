---
title: Oscillator
description: "Bipolar output [-1.0, 1.0] scaled by amplitude."
---

# Oscillator

<span class="stride-badge">Module</span> `package Dsp::Generators` &bull; Namespace: **`Dsp::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Generators/Oscillator.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Oscillator.stride:7]</a>

Bipolar output [-1.0, 1.0] scaled by amplitude.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | — |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ frequency</span> <span class="prop-default">= <code>440.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span></div> | The frequency of the oscillator. |
| <span class="port-badge prop-in">↓ amplitude</span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span></div> | The amplitude of the oscillator. |
| <span class="port-badge prop-in">↓ phase</span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | The starting phase of the oscillator. |
| <span class="port-badge prop-in">↓ reset</span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Resets the oscillator to the starting phase. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import Dsp::Generators as Generators;

Signal >> Generators::Oscillator(frequency: 440.0, amplitude: 1.0, phase: ...) >> Output;
```
