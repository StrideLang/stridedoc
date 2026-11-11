---
title: AssertInRange
description: "Inline runtime assertion verifying signal remains within bounds: AudioIn >> AssertInRange(min: -1.0 max: 1.0) >> CleanAudio."
---

# AssertInRange

<span class="stride-badge">Module</span> `package Test::Assertions` &bull; Namespace: **`Test::Assertions`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Test/Assertions.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:8]</a>

Inline runtime assertion verifying signal remains within bounds: AudioIn >> AssertInRange(min: -1.0 max: 1.0) >> CleanAudio.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Signal stream to monitor |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Passthrough of input signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `min` | `signal` | `-1.0` | — | `OutputPort.domain` | Minimum acceptable value |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `max` | `signal` | `1.0` | — | `OutputPort.domain` | Maximum acceptable value |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Test::Assertions as Assertions;

Signal >> Assertions::AssertInRange(min: -1.0, max: 1.0) >> Output;
```
