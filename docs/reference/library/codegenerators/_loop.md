---
title: _Loop
description: "Switch that ends execution. It exits immediately after any stream that turns it on: the rest of the streams, and the rest of a loop iteratio"
---

# _Loop

<span class="stride-badge">Type</span> `package Stride::CodeGenerators`

Switch that ends execution. It exits immediately after any stream that turns it on: the rest of the streams, and the rest of a loop iteration, are not run.

## Usage Example

```stride
import Stride;

# Access via CodeGenerators category:
Signal >> CodeGenerators::_Loop() >> Output;
```
