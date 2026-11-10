---
title: Mix
description: "Mix module definition."
---

# Mix

<span class="stride-badge">Module</span> `package Stride::Filters` &bull; Namespace: **`Stride::Filters`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Filters/Mix.stride#L1" target="_blank" rel="noopener" title="View source on GitHub">[Mix.stride:1]</a>

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Port">»</span> | `output` | `signal` | — | The module's primary output port. |
| <span class="port-icon stream-in" title="Port">»</span> | `input` | `signal` | — | The module's primary output port. |
| <span class="port-icon stream-in" title="Port">»</span> | `gain` | `signal` | — | Gain applied to channel. |
| <span class="port-icon stream-in" title="Port">»</span> | `bias` | `signal` | — | Bias applied to channel. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Stride;

# Access via Filters category:
Signal >> Filters::Mix() >> Output;
```
