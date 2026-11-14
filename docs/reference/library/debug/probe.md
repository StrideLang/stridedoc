---
title: Probe
description: "Lightweight signal probe that non-intrusively monitors a stream while passing it through"
---

# Probe

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Debug (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Debug.stride#L41" target="_blank" rel="noopener" title="View source on GitHub">[Debug.stride:41]</a>

Lightweight signal probe that non-intrusively monitors a stream while passing it through

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | — | — | Signal to be probed and passed through |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | — | — | Pass-through of the input signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `label` | `signal` | — | — | — | Label identifier for the probe |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Probe(label: ...) >> Output;
```
