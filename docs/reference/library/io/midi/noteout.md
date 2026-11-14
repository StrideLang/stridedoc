---
title: NoteOut
description: "Sends MIDI note on events."
---

# NoteOut

<span class="stride-badge">Module</span> `package IO::Midi` &bull; Namespace: **`IO::Midi`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Midi.stride#L42" target="_blank" rel="noopener" title="View source on GitHub">[Midi.stride:42]</a>

Sends MIDI note on events.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» trigger</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>trigger</code></span></div> | Trigger for note on |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge stream-in">» In</span> Stream Input</span>
  <span class="port-legend-item"><span class="port-badge stream-out">» Out</span> Stream Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ pitch</span> <span class="prop-default">= <code>60</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | MIDI note number [0-127] |
| <span class="port-badge prop-in">↓ velocity</span> <span class="prop-default">= <code>100</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | MIDI note velocity [0-127] |
| <span class="port-badge prop-in">↓ channel</span> <span class="prop-default">= <code>1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | MIDI channel (1-16) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import IO::Midi as Midi;

Signal >> Midi::NoteOut(pitch: 60, velocity: 100, channel: 1) >> Output;
```
