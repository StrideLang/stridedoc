---
title: Debounce
description: "Suppresses mechanical switch bounce: RawButton >> Debounce(time: 0.01) >> CleanButton. The output follows the input once it has been differe"
---

# Debounce

<span class="stride-badge">Module</span> `package Sensors::Conditioning` &bull; Namespace: **`Sensors::Conditioning`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Sensors/Conditioning.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Conditioning.stride:8]</a>

Suppresses mechanical switch bounce: RawButton >> Debounce(time: 0.01) >> CleanButton. The output follows the input once it has been different for the given time in seconds, converted against the rate of the output.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Raw digital input switch |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Debounced output switch |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `time` | `Real` | `0.01` | — | `OutputPort.domain` | Time in seconds the input must stay different from the output before the output follows it (default 0.01) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Sensors::Conditioning as Conditioning;

Signal >> Conditioning::Debounce(time: 0.01) >> Output;
```
