---
title: Debounce
description: "Suppresses mechanical switch bounce: RawButton >> Debounce(samples: 10) >> CleanButton."
---

# Debounce

<span class="stride-badge">Module</span> `package Sensors::Conditioning` &bull; Namespace: **`Sensors::Conditioning`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Sensors/Conditioning.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Conditioning.stride:8]</a>

Suppresses mechanical switch bounce: RawButton >> Debounce(samples: 10) >> CleanButton.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Raw digital or binary input signal (0 or 1) |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Debounced output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `samples` | `signal` | `10` | — | `OutputPort.domain` | Number of consecutive stable samples required to accept state change |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Sensors::Conditioning as Conditioning;

Signal >> Conditioning::Debounce(samples: 10) >> Output;
```
