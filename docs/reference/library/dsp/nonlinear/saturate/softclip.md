---
title: SoftClip
description: "Cubic polynomial soft saturator: AudioIn >> Saturate::SoftClip() >> Out."
---

# SoftClip

<span class="stride-badge">Module</span> `package Dsp::Nonlinear::Saturate` &bull; Namespace: **`Dsp::Nonlinear::Saturate`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Nonlinear/Saturate.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Saturate.stride:8]</a>

Cubic polynomial soft saturator: AudioIn >> Saturate::SoftClip() >> Out.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input audio signal stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Soft-saturated output signal stream |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
import Dsp::Nonlinear::Saturate as Saturate;

Signal >> Saturate::SoftClip() >> Output;
```
