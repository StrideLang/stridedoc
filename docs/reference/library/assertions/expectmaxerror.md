---
title: ExpectMaxError
description: "Statistical maximum absolute error assertion for stream differential testing."
---

# ExpectMaxError

<span class="stride-badge">Module</span> `package Stride` &bull; Group: **Assertions** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L139" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:139]</a>

Statistical maximum absolute error assertion for stream differential testing.

## Streams

| | Stream | Type | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `input` | `signal` | — | Two-element input list for maximum absolute error comparison: [Candidate, Baseline] |

## Properties

| | Property | Type | Default | Rate / Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `maxError` | `signal` | `0.0005` | — | Maximum allowed absolute error |Candidate - Baseline| |

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
Signal >> ExpectMaxError(maxError: 0.0005) >> Output;
```
