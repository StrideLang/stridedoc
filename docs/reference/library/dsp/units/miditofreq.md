---
title: MidiToFreq
description: "Converts MIDI note number to frequency in Hertz."
---

# MidiToFreq

<span class="stride-badge">Module</span> `package Dsp::Units` &bull; Namespace: **`Dsp::Units`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Units.stride#L66" target="_blank" rel="noopener" title="View source on GitHub">[Units.stride:66]</a>

Converts MIDI note number to frequency in Hertz.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `NotePort` | `FrequencyPort.type` | — | `NotePort.domain` | MIDI note number [0-127] where 69 = A4 (440Hz) |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `FrequencyPort` | `FrequencyPort.type` | — | `FrequencyPort.domain` | Frequency in Hertz |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Dsp::Units as Units;

Signal >> Units::MidiToFreq() >> Output;
```
