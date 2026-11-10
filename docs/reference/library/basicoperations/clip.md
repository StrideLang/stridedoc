---
title: Clip
description: "Limits signal within minimum and maximum values: Input >> Clip(minimum: 0.0 maximum: 1.0) >> Output."
---

# Clip

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **BasicOperations (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/BasicOperations.stride#L85" target="_blank" rel="noopener" title="View source on GitHub">[BasicOperations.stride:85]</a>

Limits signal within minimum and maximum values: Input >> Clip(minimum: 0.0 maximum: 1.0) >> Output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input signal to constrain |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Clipped output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `minimum` | `OutputPort.type` | `0.0` | `OutputPort.rate` | `OutputPort.domain` | Lower bound |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `maximum` | `OutputPort.type` | `1.0` | `OutputPort.rate` | `OutputPort.domain` | Upper bound |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Clip(minimum: 0.0, maximum: 1.0) >> Output;
```
