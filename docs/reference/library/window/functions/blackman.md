---
title: Blackman
description: "Blackman window function: Index >> Blackman(size: 512) >> Weight."
---

# Blackman

<span class="stride-badge">Module</span> `package Window::Functions` &bull; Namespace: **`Window::Functions`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Window/Functions.stride#L112" target="_blank" rel="noopener" title="View source on GitHub">[Functions.stride:112]</a>

Blackman window function: Index >> Blackman(size: 512) >> Weight.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `IndexPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>WeightPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>WeightPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>WeightPort.domain</code></span></div> | Sample index n (0 to size - 1) |
| <span class="port-badge stream-out">» Out</span> | `WeightPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>WeightPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>WeightPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>WeightPort.domain</code></span></div> | Window coefficient w[n] |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>size</code></span> <span class="prop-default">= <code>512.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>WeightPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>WeightPort.domain</code></span></div> | Window size / length N |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Window::Functions as Functions;

Signal >> Functions::Blackman(size: 512.0) >> Output;
```
