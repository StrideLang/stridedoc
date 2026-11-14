---
title: Xor
description: "Logical exclusive OR (XOR) operation on switch inputs: [A, B] >> Xor() >> Out."
---

# Xor

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Logic (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Logic.stride#L106" target="_blank" rel="noopener" title="View source on GitHub">[Logic.stride:106]</a>

Logical exclusive OR (XOR) operation on switch inputs: [A, B] >> Xor() >> Out.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>switch</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Two-element switch list: [A, B] |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>switch</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Switch output of A XOR B |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> Xor() >> Output;
```
