---
title: Smooth
description: "Applies first-order exponential smoothing to Input: Input >> Smooth(coefficient: 0.95) >> Output."
---

# Smooth

<span class="stride-badge">Module</span> `package Stride` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control.stride#L160" target="_blank" rel="noopener" title="View source on GitHub">[Control.stride:160]</a>

Applies first-order exponential smoothing to Input: Input >> Smooth(coefficient: 0.95) >> Output.

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | Signal to be smoothed |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | Smoothed output signal |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `coefficient` | `Coeff` | — | Smoothing coefficient between 0.0 (no smoothing) and 1.0 (freeze) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Output` | `signal` | — | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Coeff` | `signal` | `0.95` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |
| `Prev` | `signal` | `0.0` | Rate: OutputPort.rate, Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> Smooth(coefficient: ...) >> Output;
```
