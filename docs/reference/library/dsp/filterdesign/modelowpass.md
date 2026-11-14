---
title: ModeLowPass
description: "Second order low-pass: passes frequencies below `frequency`, -12 dB/octave above"
---

# ModeLowPass

<span class="stride-badge">Constant</span> `package Dsp::FilterDesign` &bull; Namespace: **`Dsp::FilterDesign`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/FilterDesign.stride#L26" target="_blank" rel="noopener" title="View source on GitHub">[FilterDesign.stride:26]</a>

Second order low-pass: passes frequencies below `frequency`, -12 dB/octave above

## Value

```stride
constant ModeLowPass = 0
```

## Usage

```stride
import Dsp::FilterDesign as FilterDesign;

Signal * FilterDesign::ModeLowPass >> Output;
```
