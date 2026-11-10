---
title: Sequencer
description: "Sequencer module definition."
---

# Sequencer

<span class="stride-badge">Module</span> `package Stride::Generators`

*Module declared in `library\1.0\Generators\Sequencer.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InputPort` | Input Stream | `Input` | — | — |
| `OutputPort` | Output Stream | `Output` | — | — |
| `values` | Property In | `Values` | — | Values in the sequencer |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Input` | `trigger` | `0` | Domain: } | Sequencer |

## Usage

```stride
import Stride;

# Access via Generators category:
Signal >> Generators::Sequencer(values: ...) >> Output;
```
