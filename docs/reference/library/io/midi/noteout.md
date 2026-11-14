---
title: NoteOut
description: "Sends MIDI note on events."
---

# NoteOut

<span class="stride-badge">Module</span> `package IO::Midi` &bull; Namespace: **`IO::Midi`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Midi.stride#L42" target="_blank" rel="noopener" title="View source on GitHub">[Midi.stride:42]</a>

Sends MIDI note on events.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `TriggerPort` | `trigger` | — | — | Trigger for note on |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `pitch` | `signal` | `60` | — | — | MIDI note number [0-127] |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `velocity` | `signal` | `100` | — | — | MIDI note velocity [0-127] |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `channel` | `signal` | `1` | — | — | MIDI channel (1-16) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import IO::Midi as Midi;

Signal >> Midi::NoteOut(pitch: 60, velocity: 100, channel: 1) >> Output;
```
