---
title: ModeHighPass
description: "Second order high-pass: passes frequencies above `frequency`, -12 dB/octave below"
---

# ModeHighPass

<span class="stride-badge">Constant</span> `package Dsp::FilterDesign` &bull; Namespace: **`Dsp::FilterDesign`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/FilterDesign.stride#L27" target="_blank" rel="noopener" title="View source on GitHub">[FilterDesign.stride:27]</a>

Second order high-pass: passes frequencies above `frequency`, -12 dB/octave below

## Value

```stride
constant ModeHighPass = 1
```

## Usage

```stride
import Dsp::FilterDesign as FilterDesign;

Signal * FilterDesign::ModeHighPass >> Output;
```
