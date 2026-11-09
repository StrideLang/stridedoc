---
title: Sequencer
description: "Sequencer module reference."
---

# Sequencer

<span class="stride-badge">Module</span> `package Stride::Generators`

*Module defined in `library\1.0\Generators\Sequencer.stride`.*

## Ports & Properties

| Name | Kind | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | — |
| `OutputPort` | Output Stream | `Output` | — | — |
| `values` | Property In | `Values` | — | Values in the sequencer |

## Internal Signals & Defaults

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `trigger` | `0` | Domain: } | Sequencer |

## Usage Example

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::Sequencer(values: ...) >> Output;
```
