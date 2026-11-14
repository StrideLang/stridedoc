---
title: RisingEdge
description: "Detects rising edge (off -> on): Input >> RisingEdge() >> Trigger."
---

# RisingEdge

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Control (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/ControlPrelude.stride#L38" target="_blank" rel="noopener" title="View source on GitHub">[ControlPrelude.stride:38]</a>

Detects rising edge (off -> on): Input >> RisingEdge() >> Trigger.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Monitored switch signal |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `switch` | `OutputPort.rate` | `OutputPort.domain` | Switch that is on for one tick when Input transitions from off to on |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> RisingEdge() >> Output;
```
