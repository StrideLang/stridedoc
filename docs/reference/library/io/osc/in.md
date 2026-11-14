---
title: In
description: "Receives OSC messages from a UDP network port."
---

# In

<span class="stride-badge">Module</span> `package IO::Osc` &bull; Namespace: **`IO::Osc`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Osc.stride#L42" target="_blank" rel="noopener" title="View source on GitHub">[Osc.stride:42]</a>

Receives OSC messages from a UDP network port.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Received OSC signal values |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ address</span> <span class="prop-default">= <code>/Stride</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | The OSC address filter |
| <span class="port-badge prop-in">↓ host</span> <span class="prop-default">= <code>127.0.0.1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Network interface or IP to listen on |
| <span class="port-badge prop-in">↓ port</span> <span class="prop-default">= <code>9011</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><code>signal</code></span></div> | Local UDP network port number to bind |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import IO::Osc as Osc;

Signal >> Osc::In(address: /Stride, host: 127.0.0.1, port: 9011) >> Output;
```
