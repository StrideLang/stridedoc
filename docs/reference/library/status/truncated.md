---
title: Truncated
description: "The result did not fit where it had to go and part of it was dropped: a string past its maxSize, a value past a buffer"
---

# Truncated

<span class="stride-badge">Constant</span> `package Status` &bull; Namespace: **`Status`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Status.stride#L23" target="_blank" rel="noopener" title="View source on GitHub">[Status.stride:23]</a>

The result did not fit where it had to go and part of it was dropped: a string past its maxSize, a value past a buffer

## Value

```stride
constant Truncated = 1
```

## Usage

```stride
import Status;

Signal * Status::Truncated >> Output;
```
