---
title: RandomInt
description: "A random whole number from min to max, both included: RandomInt(min: 1 max: 6) >> Die;"
---

# RandomInt

<span class="stride-badge">Reaction</span> Global Prelude &bull; Group: **Random (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Random.stride#L5" target="_blank" rel="noopener" title="View source on GitHub">[Random.stride:5]</a>

A random whole number from min to max, both included: RandomInt(min: 1 max: 6) >> Die;

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» ValuePort</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>Int</code></span></div> | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge stream-in">» In</span> Stream Input</span>
  <span class="port-legend-item"><span class="port-badge stream-out">» Out</span> Stream Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ min</span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>Int</code></span></div> | — |
| <span class="port-badge prop-in">↓ max</span> <span class="prop-default">= <code>1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>Int</code></span></div> | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> RandomInt(min: 0, max: 1) >> Output;
```
