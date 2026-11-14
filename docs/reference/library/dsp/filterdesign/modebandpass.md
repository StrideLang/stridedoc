---
title: ModeBandPass
description: "Second order band-pass with constant 0 dB peak gain at `frequency`; `q` sets the narrowness"
---

# ModeBandPass

<span class="stride-badge">Constant</span> `package Dsp::FilterDesign` &bull; Namespace: **`Dsp::FilterDesign`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/FilterDesign.stride#L28" target="_blank" rel="noopener" title="View source on GitHub">[FilterDesign.stride:28]</a>

Second order band-pass with constant 0 dB peak gain at `frequency`; `q` sets the narrowness

## Value

```stride
constant ModeBandPass = 2
```

## Usage

```stride
import Dsp::FilterDesign as FilterDesign;

Signal * FilterDesign::ModeBandPass >> Output;
```
