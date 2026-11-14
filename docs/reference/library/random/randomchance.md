---
title: RandomChance
description: "on with the given chance, in percent: RandomChance(percent: 25) >> Lucky;"
---

# RandomChance

<span class="stride-badge">Reaction</span> Global Prelude &bull; Group: **Random (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Random.stride#L22" target="_blank" rel="noopener" title="View source on GitHub">[Random.stride:22]</a>

on with the given chance, in percent: RandomChance(percent: 25) >> Lucky;

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» ResultPort</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>switch</code></span></div> | — |

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
| <span class="port-badge prop-in">↓ percent</span> <span class="prop-default">= <code>50</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>Int</code></span></div> | — |

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
Signal >> RandomChance(percent: 50) >> Output;
```
