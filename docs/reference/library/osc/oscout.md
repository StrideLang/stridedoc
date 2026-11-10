---
title: OSCOut
description: "OSCOut module definition."
---

# OSCOut

<span class="stride-badge">Module</span> `package Stride::Osc`

*Module declared in `library\1.0\Osc\OSC.stride`.*

## Ports & Properties

| Name | Type | Target Signal | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `input` | Input Stream | — | — | — |
| `address` | Property In | `Address` | — | The OSC address |
| `ip` | Property In | `IP` | — | The IP address to send to. |
| `port` | Property In | `Port` | — | The Network port to send the data to. |

## Signals & Attributes

| Signal | Type | Default | Rate / Domain | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Address` | `signal` | `/Stride` | — | — |
| `IP` | `signal` | `127.0.0.1` | — | — |
| `Port` | `signal` | `9010` | — | — |
| `Input` | `signal` | — | Domain: } | Sends OSC messages. |
| `Address` | `signal` | `/Stride` | — | — |
| `IP` | `signal` | `127.0.0.1` | — | — |
| `Port` | `signal` | `9011` | — | — |

## Usage

```stride
import Stride;

# Access via Osc category:
Signal >> Osc::OSCOut(address: ..., ip: ..., port: ...) >> Output;
```
