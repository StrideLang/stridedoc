---
title: ExpectSnr
description: "Statistical Signal-to-Noise Ratio assertion for stream differential testing."
---

# ExpectSnr

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L163" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:163]</a>

Statistical Signal-to-Noise Ratio assertion for stream differential testing.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `input` | `Input` | — | Two-element input list for Signal-to-Noise Ratio comparison: [Candidate, Baseline] |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `minSnr` | `MinSnr` | — | Minimum acceptable Signal-to-Noise Ratio in dB |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `MinSnr` | `signal` | `80.0` | — | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> ExpectSnr(minSnr: ...) >> Output;
```
