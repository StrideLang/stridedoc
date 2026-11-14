---
title: Hysteresis
description: "Dual-threshold hysteresis comparator (Schmitt trigger) with a switch output: Input >> Hysteresis(low: 0.2 high: 0.8) >> Output. The output k"
---

# Hysteresis

<span class="stride-badge">Module</span> `package Control` &bull; Namespace: **`Control`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Control/Hysteresis.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Hysteresis.stride:7]</a>

Dual-threshold hysteresis comparator (Schmitt trigger) with a switch output: Input >> Hysteresis(low: 0.2 high: 0.8) >> Output. The output keeps its state while the input is between the two thresholds.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-in">» In</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Input signal to evaluate |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>switch</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Switch: turns on when the input reaches the high threshold and off when it falls to the low threshold |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ low</span> <span class="prop-default">= <code>0.2</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-in">» In</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Lower switching threshold (default 0.2) |
| <span class="port-badge prop-in">↓ high</span> <span class="prop-default">= <code>0.8</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-in">» In</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Upper switching threshold (default 0.8) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import Control;

Signal >> Hysteresis(low: 0.2, high: 0.8) >> Output;
```
