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
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Counter output signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>startValue</code></span> <span class="prop-default">= <code>0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | The starting value of the counter, which is also the first output value. |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>stopValue</code></span> <span class="prop-default">= <code>100</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | The roll value of the counter. The maximum value before resetting to startValue. |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>increment</code></span> <span class="prop-default">= <code>1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | The step value added per tick. |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>reset</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>trigger</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | The counter is reset to startValue when a trigger arrives at the reset port. |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Counter(startValue: 0, stopValue: 100, increment: 1) >> Output;
```
