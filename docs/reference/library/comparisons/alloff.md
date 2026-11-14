---
title: AllOff
description: "Outputs on if all switches in the input array are off: Input >> AllOff() >> Output."
---

# AllOff

<span class="stride-badge">Loop</span> Global Prelude &bull; Group: **Comparisons (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Comparisons.stride#L216" target="_blank" rel="noopener" title="View source on GitHub">[Comparisons.stride:216]</a>

Outputs on if all switches in the input array are off: Input >> AllOff() >> Output.

## Streams

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Array of switches to be checked |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Switch that is on only if all input switches are off |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> AllOff() >> Output;
```
