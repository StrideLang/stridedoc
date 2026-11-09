---
title: Counter
description: "Counter module reference."
---

# Counter

<span class="stride-badge">Module</span> `package Stride::Counter`

*Module defined in `library\1.0\Counter.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `OutputPort` | Output Stream | `Output` | — | Counter output signal |
| `startValue` | Property In | `StartValue` | — | The starting value of the counter, which is also the first output value. |
| `stopValue` | Property In | `StopValue` | — | The roll value of the counter. The maximum value before resetting to startValue. |
| `increment` | Property In | `Increment` | — | The step value added per tick. |
| `reset` | Property In | `Reset` | — | The counter is reset to startValue when a trigger arrives at the reset port. |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `StartValue` | `signal` | `0` | Domain: reset | A discrete step counter that increments per tick and rolls over to startValue upon exceeding stopValue. |

## Usage Example

```stride
import Stride;

# Access via Counter category:
Signal >> Counter::Counter(startValue: ..., stopValue: ..., increment: ...) >> Output;
```
