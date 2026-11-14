---
title: CcOut
description: "Transmits MIDI Continuous Controller (CC) messages."
---

# CcOut

<span class="stride-badge">Module</span> `package IO::Midi` &bull; Namespace: **`IO::Midi`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Midi.stride#L106" target="_blank" rel="noopener" title="View source on GitHub">[Midi.stride:106]</a>

Transmits MIDI Continuous Controller (CC) messages.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `ValuePort` | `ValuePort.type` | — | — | Continuous controller value to send [0.0, 1.0] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `controller` | `signal` | `1` | — | — | MIDI CC number [0-127] |
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

Signal >> Midi::CcOut(controller: 1, channel: 1) >> Output;
```
