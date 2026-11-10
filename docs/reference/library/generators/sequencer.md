---
title: Sequencer
description: "Sequencer"
---

# Sequencer

<span class="stride-badge">Module</span> `package Stride::Generators` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Generators/Sequencer.stride#L2" target="_blank" rel="noopener" title="View source on GitHub">[Sequencer.stride:2]</a>

Sequencer

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `Input` | — | — |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `Output` | — | — |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `values` | `Values` | — | Values in the sequencer |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Counter` | `signal` | `0` | Domain: InputPort.domain | — |

## Usage

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::Sequencer(values: ...) >> Output;
```
