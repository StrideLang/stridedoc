---
title: Nor
description: "Logical NOR operation on switch inputs: [A, B] >> Nor() >> Out."
---

# Nor

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Logic (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L148" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:148]</a>

Logical NOR operation on switch inputs: [A, B] >> Nor() >> Out.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `switch` | — | `OutputPort.domain` | Two-element switch list: [A, B] |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `switch` | — | `OutputPort.domain` | Switch output of A NOR B |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Nor() >> Output;
```
