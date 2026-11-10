---
title: SlipEnd
description: "SLIP END marker (0xC0)"
---

# SlipEnd

<span class="stride-badge">Constant</span> `package IO::Framing` &bull; Namespace: **`IO::Framing`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Framing.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Framing.stride:8]</a>

SLIP END marker (0xC0)

## Value

```stride
constant SlipEnd = 192
```

## Usage

```stride
import IO::Framing as Framing;

Signal * Framing::SlipEnd >> Output;
```
