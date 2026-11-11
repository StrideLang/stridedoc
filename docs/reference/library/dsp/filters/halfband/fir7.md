---
title: Fir7
description: "Efficient 7-tap halfband FIR filter with 50% zero-tap reduction: AudioIn >> Halfband::Fir7() >> Out."
---

# Fir7

<span class="stride-badge">Module</span> `package Dsp::Filters::Halfband` &bull; Namespace: **`Dsp::Filters::Halfband`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Filters/Halfband.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Halfband.stride:8]</a>

Efficient 7-tap halfband FIR filter with 50% zero-tap reduction: AudioIn >> Halfband::Fir7() >> Out.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Input audio signal stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Filtered halfband audio signal stream |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Dsp::Filters::Halfband as Halfband;

Signal >> Halfband::Fir7() >> Output;
```
