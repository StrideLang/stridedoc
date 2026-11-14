---
title: CcIn
description: "Receives MIDI Continuous Controller (CC) messages."
---

# CcIn

<span class="stride-badge">Module</span> `package IO::Midi` &bull; Namespace: **`IO::Midi`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Midi.stride#L77" target="_blank" rel="noopener" title="View source on GitHub">[Midi.stride:77]</a>

Receives MIDI Continuous Controller (CC) messages.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `ValuePort` | `ValuePort.type` | — | — | Continuous controller value normalized to [0.0, 1.0] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `controller` | `signal` | `1` | — | — | MIDI CC number [0-127] |
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

Signal >> Midi::CcIn(controller: 1, channel: 0) >> Output;
```
