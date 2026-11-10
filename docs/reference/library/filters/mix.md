---
title: Mix
description: "Mix module definition."
---

# Mix

<span class="stride-badge">Module</span> `package Stride::Filters` <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Filters/Mix.stride#L1" target="_blank" rel="noopener" title="View source on GitHub">[Mix.stride:1]</a>

## Ports & Properties

| | Port | Target | Default | Description |
| :-: | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Port">»</span> | `output` | `Output` | — | The module's primary output port. |
| <span class="port-icon stream-in" title="Port">»</span> | `input` | `Input` | — | The module's primary output port. |
| <span class="port-icon stream-in" title="Port">»</span> | `gain` | `Gain` | — | Gain applied to channel. |
| <span class="port-icon stream-in" title="Port">»</span> | `bias` | `Bias` | — | Bias applied to channel. |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Gain[InputPortSize]` | `signal` | `[ 1.0 , 1 ]` | — | — |
| `Bias[InputPortSize]` | `signal` | `[ 0.0 , 0 ]` | — | — |
| `ComputeMix_Index` | `signal` | `1` | Rate: none, Domain: OutputPortDomain | — |

## Usage

```stride
import Stride;

# Access via Filters category:
Signal >> Filters::Mix() >> Output;
```
