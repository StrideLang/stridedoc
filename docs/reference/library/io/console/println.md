---
title: Println
description: "Prints the value of a stream to standard console output with a trailing newline."
---

# Println

<span class="stride-badge">Module</span> `package IO::Console` &bull; Namespace: **`IO::Console`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Console.stride#L27" target="_blank" rel="noopener" title="View source on GitHub">[Console.stride:27]</a>

Prints the value of a stream to standard console output with a trailing newline.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `ValuePort` | `signal` | — | `ValuePort.domain` | Input value to print to console followed by a newline |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import IO::Console as Console;

Signal >> Console::Println() >> Output;
```
