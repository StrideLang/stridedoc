---
title: _Buffer
description: "Current frame, oldest first. Reading it is a peek: zero-copy into reactions and loops, a copy into a block."
---

# _Buffer

<span class="stride-badge">Type</span> `package Stride`

Current frame, oldest first. Reading it is a peek: zero-copy into reactions and loops, a copy into a block.

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> _Buffer() >> Output;
```
