---
title: Error
description: "Error module definition."
---

# Error

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Debug (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Debug.stride#L27" target="_blank" rel="noopener" title="View source on GitHub">[Debug.stride:27]</a>

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» TriggerPort</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | — |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ message</span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | — |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Error(message: ...) >> Output;
```
