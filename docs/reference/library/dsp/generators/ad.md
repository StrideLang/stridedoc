---
title: AD
description: "Attack-Decay envelope generator."
---

# AD

<span class="stride-badge">Module</span> `package Dsp::Generators` &bull; Namespace: **`Dsp::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Generators/Envelope.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Envelope.stride:7]</a>

Attack-Decay envelope generator.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | — | — | The module's primary output port. |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `trigger` | — | `OutputPort.domain` | Triggers the envelope |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `attack` | `OutputPort.type` | `0.2` | — | — | Attack time in seconds |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `decay` | `OutputPort.type` | `3.0` | — | — | Decay time in seconds |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Generators as Generators;

Signal >> Generators::AD(attack: 0.2, decay: 3.0) >> Output;
```
