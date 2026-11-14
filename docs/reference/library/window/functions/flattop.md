---
title: FlatTop
description: "Flat-top measurement window function: Index >> FlatTop(size: 512) >> Weight."
---

# FlatTop

<span class="stride-badge">Module</span> `package Window::Functions` &bull; Namespace: **`Window::Functions`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Window/Functions.stride#L169" target="_blank" rel="noopener" title="View source on GitHub">[Functions.stride:169]</a>

Flat-top measurement window function: Index >> FlatTop(size: 512) >> Weight.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» index</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» weight</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» weight</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» weight</span></span></div> | Sample index n (0 to size - 1) |
| <span class="port-badge stream-out">» weight</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» weight</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» weight</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» weight</span></span></div> | Window coefficient w[n] |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ size</span> <span class="prop-default">= <code>512.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» weight</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» weight</span></span></div> | Window size / length N |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import Window::Functions as Functions;

Signal >> Functions::FlatTop(size: 512.0) >> Output;
```
