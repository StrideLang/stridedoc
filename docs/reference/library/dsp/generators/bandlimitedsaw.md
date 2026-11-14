---
title: BandLimitedSaw
description: "Band-limited sawtooth generator (differentiated parabolic wave, DPW): Saw(frequency: 220.0) >> Out. Output in [-1, 1). The frequency is in H"
---

# BandLimitedSaw

<span class="stride-badge">Module</span> `package Dsp::Generators` &bull; Namespace: **`Dsp::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Generators/BandLimitedSaw.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[BandLimitedSaw.stride:7]</a>

Band-limited sawtooth generator (differentiated parabolic wave, DPW): Saw(frequency: 220.0) >> Out. Output in [-1, 1). The frequency is in Hz and is converted against the rate of the output.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span></div> | The module's primary output port. |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ frequency</span> <span class="prop-default">= <code>220.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge prop-in">↓ frequency</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge prop-in">↓ frequency</span></span></div> | The frequency of the oscillator in Hz. |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Generators as Generators;

Signal >> Generators::BandLimitedSaw(frequency: 220.0) >> Output;
```
