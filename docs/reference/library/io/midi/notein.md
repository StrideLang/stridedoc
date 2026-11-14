---
title: NoteIn
description: "Receives MIDI note on/off events."
---

# NoteIn

<span class="stride-badge">Module</span> `package IO::Midi` &bull; Namespace: **`IO::Midi`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Midi.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Midi.stride:7]</a>

Receives MIDI note on/off events.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» frequency</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» frequency</span></span></div> | Note pitch converted to frequency in Hz |
| <span class="port-badge stream-out">» velocity</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» velocity</span></span></div> | Note velocity normalized to [0.0, 1.0] |
| <span class="port-badge stream-out">» gate</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>switch</code></span></div> | Gate switch on while note is held down |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ channel</span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | MIDI channel (1-16, 0 for all channels) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import IO::Midi as Midi;

Signal >> Midi::NoteIn(channel: 0) >> Output;
```
