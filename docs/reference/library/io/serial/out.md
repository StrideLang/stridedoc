---
title: Out
description: "Writes signal values to platform serial output stream."
---

# Out

<span class="stride-badge">Module</span> `package IO::Serial` &bull; Namespace: **`IO::Serial`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Serial.stride#L27" target="_blank" rel="noopener" title="View source on GitHub">[Serial.stride:27]</a>

Writes signal values to platform serial output stream.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-in">» In</span></span></div> | Input signal to write to serial output stream |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ channel</span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Serial channel index (default 0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import IO::Serial as Serial;

Signal >> Serial::Out(channel: 0) >> Output;
```
