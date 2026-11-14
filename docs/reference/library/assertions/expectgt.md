---
title: ExpectGt
description: "Greater-than assertion module (Actual > Expected). Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectGt

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Assertions (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L75" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:75]</a>

Greater-than assertion module (Actual > Expected). Declared for schema validation; handled with special treatment in the testing framework.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Two-element input list for greater-than comparison: [Actual, Expected] |

## Usage

```stride
# Available in global prelude without import:
Signal >> ExpectGt() >> Output;
```
