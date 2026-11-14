---
title: OutOfRange
description: "A value or index lies outside what is allowed: a number too big for Int, a pin the board does not have"
---

# OutOfRange

<span class="stride-badge">Constant</span> `package Status` &bull; Namespace: **`Status`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Status.stride#L33" target="_blank" rel="noopener" title="View source on GitHub">[Status.stride:33]</a>

A value or index lies outside what is allowed: a number too big for Int, a pin the board does not have

## Value

```stride
constant OutOfRange = 4
```

## Usage

```stride
import Status;

Signal * Status::OutOfRange >> Output;
```
