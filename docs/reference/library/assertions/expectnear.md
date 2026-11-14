---
title: ExpectNear
description: "Approximate equality assertion within epsilon tolerance. Declared for schema validation; handled with special treatment in the testing frame"
---

# ExpectNear

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Assertions (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L19" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:19]</a>

Approximate equality assertion within epsilon tolerance. Declared for schema validation; handled with special treatment in the testing framework.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Two-element input list with values expected to be close: [Actual, Expected] |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ epsilon</span> <span class="prop-default">= <code>0.0001</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Tolerance threshold for approximate comparison |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> ExpectNear(epsilon: 0.0001) >> Output;
```
