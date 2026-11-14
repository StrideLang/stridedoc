---
title: Print
description: "Writes values formatted to the serial port."
---

# Print

<span class="stride-badge">Module</span> `package IO::Serial` &bull; Namespace: **`IO::Serial`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Serial.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Serial.stride:7]</a>

Writes values formatted to the serial port.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» value</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-in">» value</span></span></div> | Value to write to serial |

## Usage

```stride
import IO::Serial as Serial;

Signal >> Serial::Print() >> Output;
```
