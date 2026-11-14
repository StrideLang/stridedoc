---
title: MidiToFreq
description: "Converts MIDI note number to frequency in Hertz."
---

# MidiToFreq

<span class="stride-badge">Module</span> `package Dsp::Units` &bull; Namespace: **`Dsp::Units`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Units.stride#L66" target="_blank" rel="noopener" title="View source on GitHub">[Units.stride:66]</a>

Converts MIDI note number to frequency in Hertz.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» note</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» frequency</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-in">» note</span></span></div> | MIDI note number [0-127] where 69 = A4 (440Hz) |
| <span class="port-badge stream-out">» frequency</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» frequency</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» frequency</span></span></div> | Frequency in Hertz |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge stream-in">» In</span> Stream Input</span>
  <span class="port-legend-item"><span class="port-badge stream-out">» Out</span> Stream Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Units as Units;

Signal >> Units::MidiToFreq() >> Output;
```
