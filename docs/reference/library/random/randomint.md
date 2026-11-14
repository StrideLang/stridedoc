---
title: RandomInt
description: "A random whole number from min to max, both included: RandomInt(min: 1 max: 6) >> Die;"
---

# RandomInt

<span class="stride-badge">Reaction</span> Global Prelude &bull; Group: **Random (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Random.stride#L5" target="_blank" rel="noopener" title="View source on GitHub">[Random.stride:5]</a>

A random whole number from min to max, both included: RandomInt(min: 1 max: 6) >> Die;

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» Out</span> | `ValuePort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>Int</code></span></div> | — |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>min</code></span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>Int</code></span></div> | — |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>max</code></span> <span class="prop-default">= <code>1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>Int</code></span></div> | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> RandomInt(min: 0, max: 1) >> Output;
```
