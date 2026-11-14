---
title: Out
description: "Transmits OSC messages over UDP to a network host."
---

# Out

<span class="stride-badge">Module</span> `package IO::Osc` &bull; Namespace: **`IO::Osc`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Osc.stride#L7" target="_blank" rel="noopener" title="View source on GitHub">[Osc.stride:7]</a>

Transmits OSC messages over UDP to a network host.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-in">» In</span></span></div> | Signal data to send via OSC |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ address</span> <span class="prop-default">= <code>/Stride</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | The OSC address string (default /Stride) |
| <span class="port-badge prop-in">↓ host</span> <span class="prop-default">= <code>127.0.0.1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Destination hostname or IP address |
| <span class="port-badge prop-in">↓ port</span> <span class="prop-default">= <code>9010</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Destination UDP network port number |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">type</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">rate</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">domain</span> Domain</span>
</div>

## Usage

```stride
import IO::Osc as Osc;

Signal >> Osc::Out(address: /Stride, host: 127.0.0.1, port: 9010) >> Output;
```
