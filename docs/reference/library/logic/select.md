---
title: Select
description: "Selects between whenOn and whenOff signals based on a switch condition: Input >> Select(condition: Cond whenOn: Alt whenOff: Input) >> Outpu"
---

# Select

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Logic (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L4" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:4]</a>

Selects between whenOn and whenOff signals based on a switch condition: Input >> Select(condition: Cond whenOn: Alt whenOff: Input) >> Output.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Default signal flowing along the primary path |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Selected output signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ condition</span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>switch</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Switch condition determining which value is output |
| <span class="port-badge prop-in">↓ whenOn</span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Signal produced when Condition is on |
| <span class="port-badge prop-in">↓ whenOff</span> <span class="prop-default">= <code>Input</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Signal produced when Condition is off (defaults to Input if not specified) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Select(condition: ..., whenOn: ..., whenOff: Input) >> Output;
```
