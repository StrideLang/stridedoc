---
title: Sequencer
description: "Step sequencer module."
---

# Sequencer

<span class="stride-badge">Module</span> `package Dsp::Generators` &bull; Namespace: **`Dsp::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Generators/Sequencer.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Sequencer.stride:7]</a>

Step sequencer module.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `trigger` | — | `InputPort.domain` | — |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | — | `OutputPort.domain` | — |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `values` | `constant` | — | — | — | Values in the sequencer |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Generators as Generators;

Signal >> Generators::Sequencer(values: ...) >> Output;
```
