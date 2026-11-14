---
title: Log
description: "Logs structured timestamped telemetry messages."
---

# Log

<span class="stride-badge">Module</span> `package IO::Console` &bull; Namespace: **`IO::Console`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/IO/Console.stride#L49" target="_blank" rel="noopener" title="View source on GitHub">[Console.stride:49]</a>

Logs structured timestamped telemetry messages.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `ValuePort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>ValuePort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>ValuePort.domain</code></span></div> | Value to log with structured telemetry timestamp |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>tag</code></span> <span class="prop-default">= <code>INFO</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>signal</code></span></div> | Log category tag |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import IO::Console as Console;

Signal >> Console::Log(tag: INFO) >> Output;
```
