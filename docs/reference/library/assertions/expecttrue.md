---
title: ExpectTrue
description: "Condition assertion (true). Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectTrue

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Assertions** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L43" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:43]</a>

Condition assertion (true). Declared for schema validation; handled with special treatment in the testing framework.

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `input` | `switch` | — | — | Condition value expected to be true (on) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectTrue() >> Output;
```
