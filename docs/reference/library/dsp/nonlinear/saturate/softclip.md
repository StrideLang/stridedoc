---
title: SoftClip
description: "Cubic polynomial soft saturator: AudioIn >> Saturate::SoftClip() >> Out."
---

# SoftClip

<span class="stride-badge">Module</span> `package Dsp::Nonlinear::Saturate` &bull; Namespace: **`Dsp::Nonlinear::Saturate`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Nonlinear/Saturate.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[Saturate.stride:8]</a>

Cubic polynomial soft saturator: AudioIn >> Saturate::SoftClip() >> Out.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Input audio signal stream |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Soft-saturated output signal stream |

## Usage

```stride
import Dsp::Nonlinear::Saturate as Saturate;

Signal >> Saturate::SoftClip() >> Output;
```
