---
title: ModePeak
description: "Peaking equaliser: boosts or cuts a band around `frequency` by `gain` dB"
---

# ModePeak

<span class="stride-badge">Constant</span> `package Dsp::FilterDesign` &bull; Namespace: **`Dsp::FilterDesign`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/FilterDesign.stride#L31" target="_blank" rel="noopener" title="View source on GitHub">[FilterDesign.stride:31]</a>

Peaking equaliser: boosts or cuts a band around `frequency` by `gain` dB

## Value

```stride
constant ModePeak = 5
```

## Usage

```stride
import Dsp::FilterDesign as FilterDesign;

Signal * FilterDesign::ModePeak >> Output;
```
