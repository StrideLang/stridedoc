---
title: In
description: "Reads signal values from platform serial input stream."
---

# In

<span class="stride-badge">Module</span> `package IO::Serial` &bull; Namespace: **`IO::Serial`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Serial.stride#L50" target="_blank" rel="noopener" title="View source on GitHub">[Serial.stride:50]</a>

Reads signal values from platform serial input stream.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Serial input signal stream |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>channel</code></span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span></div> | Serial channel index (default 0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import IO::Serial as Serial;

Signal >> Serial::In(channel: 0) >> Output;
```
