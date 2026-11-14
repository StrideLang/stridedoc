---
title: NoteOut
description: "Sends MIDI note on events."
---

# NoteOut

<span class="stride-badge">Module</span> `package IO::Midi` &bull; Namespace: **`IO::Midi`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Midi.stride#L42" target="_blank" rel="noopener" title="View source on GitHub">[Midi.stride:42]</a>

Sends MIDI note on events.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `TriggerPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>trigger</code></span></div> | Trigger for note on |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>pitch</code></span> <span class="prop-default">= <code>60</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span></div> | MIDI note number [0-127] |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>velocity</code></span> <span class="prop-default">= <code>100</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span></div> | MIDI note velocity [0-127] |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>channel</code></span> <span class="prop-default">= <code>1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span></div> | MIDI channel (1-16) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import IO::Midi as Midi;

Signal >> Midi::NoteOut(pitch: 60, velocity: 100, channel: 1) >> Output;
```
