---
title: _GroupType
description: "Groups signals for block processing. Guarantees that all signals are processed together."
---

# _GroupType

<span class="stride-badge">Type</span> `package Stride::CoreTypes`

Groups signals for block processing. Guarantees that all signals are processed together.

## Usage Example

```stride
import Stride;

# Access via CoreTypes category:
Signal >> CoreTypes::_GroupType() >> Output;
```
