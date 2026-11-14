---
title: ExpectNear
description: "Approximate equality assertion within epsilon tolerance. Declared for schema validation; handled with special treatment in the testing frame"
---

# ExpectNear

<span class="stride-badge">Module</span> Global Prelude &bull; Group: **Assertions (Group)** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Assertions.stride#L19" target="_blank" rel="noopener" title="View source on GitHub">[Assertions.stride:19]</a>

Approximate equality assertion within epsilon tolerance. Declared for schema validation; handled with special treatment in the testing framework.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | — | — | Two-element input list with values expected to be close: [Actual, Expected] |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `epsilon` | `signal` | `0.0001` | — | — | Tolerance threshold for approximate comparison |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
# Available in global prelude without import:
Signal >> ExpectNear(epsilon: 0.0001) >> Output;
```
