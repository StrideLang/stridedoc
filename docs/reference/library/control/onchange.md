---
title: OnChange
description: "Detects changes in a signal: outputs on when Input differs from previous tick: Input >> OnChange() >> Trigger."
---

# OnChange

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Control (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/ControlPrelude.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[ControlPrelude.stride:4]</a>

Detects changes in a signal: outputs on when Input differs from previous tick: Input >> OnChange() >> Trigger.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `InputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Signal or switch being monitored for changes |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Switch that is on when Input changed from its previous tick value |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> OnChange() >> Output;
```
