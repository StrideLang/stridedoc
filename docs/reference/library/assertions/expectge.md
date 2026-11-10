---
title: ExpectGe
description: "Greater-than-or-equal assertion module (Actual >= Expected). Declared for schema validation; handled with special treatment in the testing f"
---

# ExpectGe

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L91" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:91]</a>

Greater-than-or-equal assertion module (Actual >= Expected). Declared for schema validation; handled with special treatment in the testing framework.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `input` | `Input` | — | Two-element input list for greater-than-or-equal comparison: [Actual, Expected] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectGe() >> Output;
```
