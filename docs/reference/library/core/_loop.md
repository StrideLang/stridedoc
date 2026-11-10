---
title: _Loop
description: "Switch that ends execution. It exits immediately after any stream that turns it on: the rest of the streams, and the rest of a loop iteratio"
---

# _Loop

<span class="stride-badge">Type</span> `package Stride`

Switch that ends execution. It exits immediately after any stream that turns it on: the rest of the streams, and the rest of a loop iteration, are not run.

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> _Loop() >> Output;
```
