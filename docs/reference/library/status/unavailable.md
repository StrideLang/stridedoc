---
title: Unavailable
description: "The resource cannot be used right now: a full transmit buffer, a peripheral that is not ready"
---

# Unavailable

<span class="stride-badge">Constant</span> `package Status` &bull; Namespace: **`Status`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Status.stride#L38" target="_blank" rel="noopener" title="View source on GitHub">[Status.stride:38]</a>

The resource cannot be used right now: a full transmit buffer, a peripheral that is not ready

## Value

```stride
constant Unavailable = 8
```

## Usage

```stride
import Status;

Signal * Status::Unavailable >> Output;
```
