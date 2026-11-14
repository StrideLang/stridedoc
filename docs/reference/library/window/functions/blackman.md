---
title: Blackman
description: "Blackman window function: Index >> Blackman(size: 512) >> Weight."
---

# Blackman

<span class="stride-badge">Module</span> `package Window::Functions` &bull; Namespace: **`Window::Functions`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Window/Functions.stride#L112" target="_blank" rel="noopener" title="View source on GitHub">[Functions.stride:112]</a>

Blackman window function: Index >> Blackman(size: 512) >> Weight.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `IndexPort` | `WeightPort.type` | `WeightPort.rate` | `WeightPort.domain` | Sample index n (0 to size - 1) |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `WeightPort` | `WeightPort.type` | `WeightPort.rate` | `WeightPort.domain` | Window coefficient w[n] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `size` | `WeightPort.type` | `512.0` | — | `WeightPort.domain` | Window size / length N |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Window::Functions as Functions;

Signal >> Functions::Blackman(size: 512.0) >> Output;
```
