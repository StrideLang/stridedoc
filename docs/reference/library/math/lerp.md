---
title: Lerp
description: "Linearly interpolates from Input to Target based on factor: Input >> Lerp(target: Target factor: 0.5) >> Output."
---

# Lerp

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Math (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/MathPrelude.stride#L639" target="_blank" rel="noopener" title="View source on GitHub">[MathPrelude.stride:639]</a>

Linearly interpolates from Input to Target based on factor: Input >> Lerp(target: Target factor: 0.5) >> Output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Base input signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Interpolated output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `target` | `OutputPort.type` | `0.0` | `OutputPort.rate` | `OutputPort.domain` | Target signal to blend towards |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `factor` | `OutputPort.type` | `0.5` | `OutputPort.rate` | `OutputPort.domain` | Blend factor from 0.0 (Input) to 1.0 (Target) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Lerp(target: 0.0, factor: 0.5) >> Output;
```
