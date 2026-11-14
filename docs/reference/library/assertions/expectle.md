---
title: ExpectLe
description: "Less-than-or-equal assertion module (Actual <= Expected). Declared for schema validation; handled with special treatment in the testing fram"
---

# ExpectLe

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Assertions (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L123" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:123]</a>

Less-than-or-equal assertion module (Actual <= Expected). Declared for schema validation; handled with special treatment in the testing framework.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Two-element input list for less-than-or-equal comparison: [Actual, Expected] |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge stream-in">» In</span> Stream Input</span>
  <span class="port-legend-item"><span class="port-badge stream-out">» Out</span> Stream Output</span>
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> ExpectLe() >> Output;
```
