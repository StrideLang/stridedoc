---
title: ExpectMaxError
description: "Statistical maximum absolute error assertion for stream differential testing."
---

# ExpectMaxError

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Assertions (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L139" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:139]</a>

Statistical maximum absolute error assertion for stream differential testing.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Two-element input list for maximum absolute error comparison: [Candidate, Baseline] |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ maxError</span> <span class="prop-default">= <code>0.0005</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Maximum allowed absolute error |Candidate - Baseline| |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> ExpectMaxError(maxError: 0.0005) >> Output;
```
