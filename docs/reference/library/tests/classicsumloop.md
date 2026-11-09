---
title: ClassicSumLoop
description: "ClassicSumLoop loop reference."
---

# ClassicSumLoop

<span class="stride-badge">Loop</span> `package Stride::tests`

*Loop defined in `library\1.0\tests\CallableTest.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | — |
| `OutputPort` | Output Stream | `Output` | — | — |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input[InputPort.size]` | `signal` | `off` | Rate: -1, Domain: PipelineDomain | — |

## Usage Example

```stride
import Stride;

# Access via tests category:
Signal >> tests::ClassicSumLoop() >> Output;
```
