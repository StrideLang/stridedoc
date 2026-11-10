---
title: AD
description: "AD module definition."
---

# AD

<span class="stride-badge">Module</span> `package Stride::Generators` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Generators/Envelope.stride#L1" target="_blank" rel="noopener" title="View source on GitHub">[Envelope.stride:1]</a>

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `output` | `Output` | — | The module's primary output port. |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `output` | `TriggerEnv` | — | Triggers the envelope |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `attack` | `AttackTime` | — | Attack time in seconds |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `decay` | `DecayTime` | — | Decay time in seconds |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AttackTime` | `signal` | `0.2` | — | — |
| `DecayTime` | `signal` | `3.0` | — | — |
| `Output` | `signal` | `0.0` | — | — |
| `StageIncrements[2]` | `signal` | `0.0` | — | — |
| `Stage` | `signal` | `-1` | Domain: OutputPort.domain | — |

## Usage

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::AD(attack: ..., decay: ...) >> Output;
```
