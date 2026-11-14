---
title: NoteIn
description: "Receives MIDI note on/off events."
---

# NoteIn

<span class="stride-badge">Module</span> `package IO::Midi` &bull; Namespace: **`IO::Midi`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Midi.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Midi.stride:7]</a>

Receives MIDI note on/off events.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `FrequencyPort` | `FrequencyPort.type` | — | — | Note pitch converted to frequency in Hz |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `VelocityPort` | `VelocityPort.type` | — | — | Note velocity normalized to [0.0, 1.0] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `GatePort` | `switch` | — | — | Gate switch on while note is held down |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `channel` | `signal` | `0` | — | — | MIDI channel (1-16, 0 for all channels) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import IO::Midi as Midi;

Signal >> Midi::NoteIn(channel: 0) >> Output;
```
