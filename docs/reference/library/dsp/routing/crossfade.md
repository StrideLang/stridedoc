---
title: Crossfade
description: "Linear crossfade between two audio streams."
---

# Crossfade

<span class="stride-badge">Module</span> `package Dsp::Routing` &bull; Namespace: **`Dsp::Routing`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Routing.stride#L112" target="_blank" rel="noopener" title="View source on GitHub">[Routing.stride:112]</a>

Linear crossfade between two audio streams.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Primary input signal |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Crossfaded output stream |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ with</span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Secondary input signal to blend with |
| <span class="port-badge prop-in">↓ mix</span> <span class="prop-default">= <code>0.5</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Crossfade blend ratio from 0.0 (input) to 1.0 (with) (default 0.5) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import Dsp::Routing as Routing;

Signal >> Routing::Crossfade(with: ..., mix: 0.5) >> Output;
```
