---
title: ExpectFalse
description: "Condition assertion (false). Declared for schema validation; handled with special treatment in the testing framework."
---

# ExpectFalse

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Assertions (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L59" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:59]</a>

Condition assertion (false). Declared for schema validation; handled with special treatment in the testing framework.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>switch</code></span></div> | Condition value expected to be false (off) |

## Usage

```stride
# Available in global prelude without import:
Signal >> ExpectFalse() >> Output;
```
