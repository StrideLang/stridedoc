---
title: _Buffer
description: "Current frame, oldest first. Reading it is a peek: zero-copy into reactions and loops, a copy into a block."
---

# _Buffer

<span class="stride-badge">Type</span> `package Stride::CoreTypes`

Current frame, oldest first. Reading it is a peek: zero-copy into reactions and loops, a copy into a block.

## Usage Example

```stride
import Stride;

# Access via CoreTypes category:
Signal >> CoreTypes::_Buffer() >> Output;
```
