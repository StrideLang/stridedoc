---
title: Counter
description: "A discrete step counter that increments per tick and rolls over to startValue upon exceeding stopValue."
---

# Counter

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Counter (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Counter.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[Counter.stride:4]</a>

A discrete step counter that increments per tick and rolls over to startValue upon exceeding stopValue.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Counter output signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ startValue</span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | The starting value of the counter, which is also the first output value. |
| <span class="port-badge prop-in">↓ stopValue</span> <span class="prop-default">= <code>100</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | The roll value of the counter. The maximum value before resetting to startValue. |
| <span class="port-badge prop-in">↓ increment</span> <span class="prop-default">= <code>1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | The step value added per tick. |
| <span class="port-badge prop-in">↓ reset</span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>trigger</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | The counter is reset to startValue when a trigger arrives at the reset port. |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Counter(startValue: 0, stopValue: 100, increment: 1) >> Output;
```
