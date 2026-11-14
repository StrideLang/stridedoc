---
title: CcOut
description: "Transmits MIDI Continuous Controller (CC) messages."
---

# CcOut

<span class="stride-badge">Module</span> `package IO::Midi` &bull; Namespace: **`IO::Midi`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Midi.stride#L106" target="_blank" rel="noopener" title="View source on GitHub">[Midi.stride:106]</a>

Transmits MIDI Continuous Controller (CC) messages.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» value</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-in">» value</span></span></div> | Continuous controller value to send [0.0, 1.0] |

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
| <span class="port-badge prop-in">↓ controller</span> <span class="prop-default">= <code>1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | MIDI CC number [0-127] |
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

Signal >> Midi::CcOut(controller: 1, channel: 1) >> Output;
```
