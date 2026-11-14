---
title: Print
description: "Prints the value of a stream to standard console output."
---

# Print

<span class="stride-badge">Module</span> `package IO::Console` &bull; Namespace: **`IO::Console`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Console.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Console.stride:7]</a>

Prints the value of a stream to standard console output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `ValuePort` | `ValuePort.type` | — | `ValuePort.domain` | Input value to print to console |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import IO::Console as Console;

Signal >> Console::Print() >> Output;
```
