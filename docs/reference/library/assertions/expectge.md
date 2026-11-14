---
title: ExpectGe
description: "Greater-than-or-equal assertion module (Actual >= Expected). Declared for schema validation; handled with special treatment in the testing f"
---

# ExpectGe

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Assertions (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L91" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:91]</a>

Greater-than-or-equal assertion module (Actual >= Expected). Declared for schema validation; handled with special treatment in the testing framework.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span></div> | Two-element input list for greater-than-or-equal comparison: [Actual, Expected] |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> ExpectGe() >> Output;
```
