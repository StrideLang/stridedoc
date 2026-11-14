---
title: NoteIn
description: "Receives MIDI note on/off events."
---

# NoteIn

<span class="stride-badge">Module</span> `package IO::Midi` &bull; Namespace: **`IO::Midi`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Midi.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Midi.stride:7]</a>

Receives MIDI note on/off events.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» Out</span> | `FrequencyPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>FrequencyPort.type</code></span></div> | Note pitch converted to frequency in Hz |
| <span class="port-badge stream-out">» Out</span> | `VelocityPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>VelocityPort.type</code></span></div> | Note velocity normalized to [0.0, 1.0] |
| <span class="port-badge stream-out">» Out</span> | `GatePort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>switch</code></span></div> | Gate switch on while note is held down |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>channel</code></span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span></div> | MIDI channel (1-16, 0 for all channels) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import IO::Midi as Midi;

Signal >> Midi::NoteIn(channel: 0) >> Output;
```
