---
title: Compact
description: "Prioritizes minimal Flash/RAM memory footprint (e.g. avoids tables, uses ROM)"
---

# Compact

<span class="stride-badge">Constant</span> `package QualityPolicy`

Prioritizes minimal Flash/RAM memory footprint (e.g. avoids tables, uses ROM)

## Usage Example

```stride
import Stride;

# Access via QualityPolicy category:
Signal >> QualityPolicy::Compact() >> Output;
```
