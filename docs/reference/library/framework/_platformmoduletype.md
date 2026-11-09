---
title: _PlatformModuleType
description: "on when the result depends only on the inputs and the program's definition (no state, no side effects), so the compiler may call it while co"
---

# _PlatformModuleType

<span class="stride-badge">Type</span> `package Stride::Framework`

on when the result depends only on the inputs and the program's definition (no state, no side effects), so the compiler may call it while compiling, for example to fill constants

## Usage Example

```stride
import Stride;

# Access via Framework category:
Signal >> Framework::_PlatformModuleType() >> Output;
```
