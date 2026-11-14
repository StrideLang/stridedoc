---
title: Println
description: "Prints the value of a stream to standard console output with a trailing newline."
---

# Println

<span class="stride-badge">Module</span> `package IO::Console` &bull; Namespace: **`IO::Console`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Console.stride#L28" target="_blank" rel="noopener" title="View source on GitHub">[Console.stride:28]</a>

Prints the value of a stream to standard console output with a trailing newline.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» value</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-in">» value</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-in">» value</span></span></div> | Input value to print to console followed by a newline |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge stream-in">» In</span> Stream Input</span>
  <span class="port-legend-item"><span class="port-badge stream-out">» Out</span> Stream Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import IO::Console as Console;

Signal >> Console::Println() >> Output;
```
