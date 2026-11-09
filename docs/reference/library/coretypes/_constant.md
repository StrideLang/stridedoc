---
title: _Constant
description: "Holds a constant value. Without a value it is written once, by the first stream that writes it (a table filled at setup), and needs a type."
---

# _Constant

<span class="stride-badge">Type</span> `package Stride::CoreTypes`

Holds a constant value. Without a value it is written once, by the first stream that writes it (a table filled at setup), and needs a type.

## Usage Example

```stride
import Stride;

# Access via CoreTypes category:
Signal >> CoreTypes::_Constant() >> Output;
```
