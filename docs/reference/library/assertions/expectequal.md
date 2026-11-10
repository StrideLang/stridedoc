---
title: ExpectEqual
description: "Equality assertion module. Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectEqual

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Assertions** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L3" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:3]</a>

Equality assertion module. Declared for schema validation; handled with special treatment in the testing framework.

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `input` | `signal` | — | — | Two-element input list with values expected to be equal: [Actual, Expected] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectEqual() >> Output;
```
