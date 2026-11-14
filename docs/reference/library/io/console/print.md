---
title: Print
description: "Prints the value of a stream to standard console output."
---

# Print

<span class="stride-badge">Module</span> `package IO::Console` &bull; Namespace: **`IO::Console`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Console.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Console.stride:7]</a>

Prints the value of a stream to standard console output.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» value</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-in">» value</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-in">» value</span></span></div> | Input value to print to console |

## Usage

```stride
import IO::Console as Console;

Signal >> Console::Print() >> Output;
```
