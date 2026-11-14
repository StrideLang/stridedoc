---
title: Pan
description: "Linear stereo panner splitting a mono signal into stereo left [0] and right [1]."
---

# Pan

<span class="stride-badge">Module</span> `package Dsp::Routing` &bull; Namespace: **`Dsp::Routing`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Routing.stride#L60" target="_blank" rel="noopener" title="View source on GitHub">[Routing.stride:60]</a>

Linear stereo panner splitting a mono signal into stereo left [0] and right [1].

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Mono input signal |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Stereo output signal array [left, right] |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ position</span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Sets the stereo panning position in range [-1.0, 1.0]: -1 is full left, 0 is centre and 1 is full right (default 0.0). |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import Dsp::Routing as Routing;

Signal >> Routing::Pan(position: 0.0) >> Output;
```
