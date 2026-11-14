---
title: ModeNotch
description: "Notch (band-reject): removes a narrow band around `frequency`"
---

# ModeNotch

<span class="stride-badge">Constant</span> `package Dsp::FilterDesign` &bull; Namespace: **`Dsp::FilterDesign`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/FilterDesign.stride#L29" target="_blank" rel="noopener" title="View source on GitHub">[FilterDesign.stride:29]</a>

Notch (band-reject): removes a narrow band around `frequency`

## Value

```stride
constant ModeNotch = 3
```

## Usage

```stride
import Dsp::FilterDesign as FilterDesign;

Signal * FilterDesign::ModeNotch >> Output;
```
