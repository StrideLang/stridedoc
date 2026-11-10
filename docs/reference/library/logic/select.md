---
title: Select
description: "Selects between whenOn and whenOff signals based on a switch condition: Input >> Select(condition: Cond whenOn: Alt whenOff: Input) >> Outpu"
---

# Select

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Logic (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:4]</a>

Selects between whenOn and whenOff signals based on a switch condition: Input >> Select(condition: Cond whenOn: Alt whenOff: Input) >> Output.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | — | `OutputPort.domain` | Default signal flowing along the primary path |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | `OutputPort.domain` | Selected output signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `condition` | `switch` | — | — | `OutputPort.domain` | Switch condition determining which value is output |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `whenOn` | `signal` | — | — | `OutputPort.domain` | Signal produced when Condition is on |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `whenOff` | `signal` | `Input` | — | `OutputPort.domain` | Signal produced when Condition is off (defaults to Input if not specified) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Select(condition: ..., whenOn: ..., whenOff: Input) >> Output;
```
