---
title: AssertInRange
description: "Inline runtime assertion verifying signal remains within bounds: AudioIn >> AssertInRange(min: -1.0 max: 1.0) >> CleanAudio."
---

# AssertInRange

<span class="stride-badge">Module</span> `package Test::Assertions` &bull; Namespace: **`Test::Assertions`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Test/Assertions.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:8]</a>

Inline runtime assertion verifying signal remains within bounds: AudioIn >> AssertInRange(min: -1.0 max: 1.0) >> CleanAudio.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Signal stream to monitor |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Passthrough of input signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ min</span> <span class="prop-default">= <code>-1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Minimum acceptable value |
| <span class="port-badge prop-in">↓ max</span> <span class="prop-default">= <code>1.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Maximum acceptable value |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import Test::Assertions as Assertions;

Signal >> Assertions::AssertInRange(min: -1.0, max: 1.0) >> Output;
```
