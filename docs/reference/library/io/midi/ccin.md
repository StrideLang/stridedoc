---
title: CcIn
description: "Receives MIDI Continuous Controller (CC) messages."
---

# CcIn

<span class="stride-badge">Module</span> `package IO::Midi` &bull; Namespace: **`IO::Midi`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Midi.stride#L77" target="_blank" rel="noopener" title="View source on GitHub">[Midi.stride:77]</a>

Receives MIDI Continuous Controller (CC) messages.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» value</span> | `ValuePort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» value</span></span></div> | Continuous controller value normalized to [0.0, 1.0] |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ controller</span> <span class="prop-default">= <code>1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | MIDI CC number [0-127] |
| <span class="port-badge prop-in">↓ channel</span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | MIDI channel (1-16, 0 for all channels) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import IO::Midi as Midi;

Signal >> Midi::CcIn(controller: 1, channel: 0) >> Output;
```
