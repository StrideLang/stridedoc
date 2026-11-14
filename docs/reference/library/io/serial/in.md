---
title: In
description: "Reads signal values from platform serial input stream."
---

# In

<span class="stride-badge">Module</span> `package IO::Serial` &bull; Namespace: **`IO::Serial`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Serial.stride#L50" target="_blank" rel="noopener" title="View source on GitHub">[Serial.stride:50]</a>

Reads signal values from platform serial input stream.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Serial input signal stream |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ channel</span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Serial channel index (default 0) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import IO::Serial as Serial;

Signal >> Serial::In(channel: 0) >> Output;
```
