---
title: RandomInt
description: "A random whole number from min to max, both included: RandomInt(min: 1 max: 6) >> Die;"
---

# RandomInt

<span class="stride-badge">Reaction</span> Global Prelude &bull; Group: **Random (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Random.stride#L5" target="_blank" rel="noopener" title="View source on GitHub">[Random.stride:5]</a>

A random whole number from min to max, both included: RandomInt(min: 1 max: 6) >> Die;

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `ValuePort` | `Int` | — | — | — |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `min` | `Int` | `0` | — | — | — |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `max` | `Int` | `1` | — | — | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> RandomInt(min: 0, max: 1) >> Output;
```
