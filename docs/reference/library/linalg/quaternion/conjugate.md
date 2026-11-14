---
title: Conjugate
description: "Quaternion conjugate: Q >> Conjugate() >> QConjugate."
---

# Conjugate

<span class="stride-badge">Module</span> `package LinAlg::Quaternion` &bull; Namespace: **`LinAlg::Quaternion`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/LinAlg/Quaternion.stride#L44" target="_blank" rel="noopener" title="View source on GitHub">[Quaternion.stride:44]</a>

Quaternion conjugate: Q >> Conjugate() >> QConjugate.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» q</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Input quaternion [w, x, y, z] |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Conjugated quaternion [w, -x, -y, -z] |

## Usage

```stride
import LinAlg::Quaternion as Quaternion;

Signal >> Quaternion::Conjugate() >> Output;
```
