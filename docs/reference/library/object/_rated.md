---
title: _Rated
description: "Declarations without a rate are reactive: they take the rate of whatever writes to them"
---

# _Rated

<span class="stride-badge">Type</span> `package Stride::Object`

Declarations without a rate are reactive: they take the rate of whatever writes to them

## Usage Example

```stride
import Stride;

# Access via Object category:
Signal >> Object::_Rated() >> Output;
```
