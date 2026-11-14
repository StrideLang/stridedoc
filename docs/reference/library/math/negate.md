---
title: Negate
description: "Negates (changes the sign of) an input value: -Input. Input >> Negate() >> Output. (For the multiplicative inverse use 1.0 / Input.)"
---

# Negate

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Math (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/MathPrelude.stride#L317" target="_blank" rel="noopener" title="View source on GitHub">[MathPrelude.stride:317]</a>

Negates (changes the sign of) an input value: -Input. Input >> Negate() >> Output. (For the multiplicative inverse use 1.0 / Input.)

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Value to negate |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | The negated value |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Negate() >> Output;
```
