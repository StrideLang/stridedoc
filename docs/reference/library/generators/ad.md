---
title: AD
description: "AD module definition."
---

# AD

<span class="stride-badge">Module</span> `package Stride::Generators` &bull; Namespace: **`Stride::Generators`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Generators/Envelope.stride#L1" target="_blank" rel="noopener" title="View source on GitHub">[Envelope.stride:1]</a>

## Streams

| | Stream | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `output` | `signal` | — | — | The module's primary output port. |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `output` | `trigger` | — | `OutputPort.domain` | Triggers the envelope |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `attack` | `signal` | `0.2` | — | — | Attack time in seconds |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `decay` | `signal` | `3.0` | — | — | Decay time in seconds |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::AD(attack: 0.2, decay: 3.0) >> Output;
```
