---
title: _PortAttributes
description: "Port attributes are populated by the compiler from stream connections. They are read only (e.g. InputPort.type). Ports have no type or defau"
---

# _PortAttributes

<span class="stride-badge">Type</span> `package Stride`

Port attributes are populated by the compiler from stream connections. They are read only (e.g. InputPort.type). Ports have no type or default: these come from the declaration of the bound entity.

## Usage

```stride
import Stride;

# Available in root namespace:
Signal >> _PortAttributes() >> Output;
```
