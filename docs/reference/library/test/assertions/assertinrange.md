---
title: AssertInRange
description: "Inline runtime assertion verifying signal remains within bounds: AudioIn >> AssertInRange(min: -1.0 max: 1.0) >> CleanAudio."
---

# AssertInRange

<span class="stride-badge">Module</span> `package Test::Assertions` &bull; Namespace: **`Test::Assertions`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Test/Assertions.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:8]</a>

Inline runtime assertion verifying signal remains within bounds: AudioIn >> AssertInRange(min: -1.0 max: 1.0) >> CleanAudio.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Signal stream to monitor |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Passthrough of input signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>min</code></span> <span class="prop-default">= <code>-1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Minimum acceptable value |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>max</code></span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Maximum acceptable value |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Test::Assertions as Assertions;

Signal >> Assertions::AssertInRange(min: -1.0, max: 1.0) >> Output;
```
