---
title: Print
description: "Prints the value of a stream to standard console output."
---

# Print

<span class="stride-badge">Module</span> `package IO::Console` &bull; Namespace: **`IO::Console`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Console.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Console.stride:7]</a>

Prints the value of a stream to standard console output.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `ValuePort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>ValuePort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>ValuePort.domain</code></span></div> | Input value to print to console |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import IO::Console as Console;

Signal >> Console::Print() >> Output;
```
