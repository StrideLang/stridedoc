---
title: DbToLinear
description: "Converts decibels (dB) to linear amplitude ratio."
---

# DbToLinear

<span class="stride-badge">Module</span> `package Dsp::Units` &bull; Namespace: **`Dsp::Units`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Units.stride#L91" target="_blank" rel="noopener" title="View source on GitHub">[Units.stride:91]</a>

Converts decibels (dB) to linear amplitude ratio.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» db</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» linear</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-in">» db</span></span></div> | Amplitude in decibels (dB) |
| <span class="port-badge stream-out">» linear</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» linear</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» linear</span></span></div> | Linear amplitude ratio |

## Usage

```stride
import Dsp::Units as Units;

Signal >> Units::DbToLinear() >> Output;
```
