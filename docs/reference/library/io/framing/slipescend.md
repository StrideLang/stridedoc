---
title: SlipEscEnd
description: "SLIP ESC_END byte (0xDC)"
---

# SlipEscEnd

<span class="stride-badge">Constant</span> `package IO::Framing` &bull; Namespace: **`IO::Framing`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Framing.stride#L10" target="_blank" rel="noopener" title="View source on GitHub">[Framing.stride:10]</a>

SLIP ESC_END byte (0xDC)

## Value

```stride
constant SlipEscEnd = 220
```

## Usage

```stride
import IO::Framing as Framing;

Signal * Framing::SlipEscEnd >> Output;
```
