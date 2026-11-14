---
title: LinearCalibration
description: "Rescales raw ADC readings to engineering units: Adc >> LinearCalibration(rawMin: 0 rawMax: 4095 calMin: 0.0 calMax: 3.3) >> Volts."
---

# LinearCalibration

<span class="stride-badge">Module</span> `package Sensors::Conditioning` &bull; Namespace: **`Sensors::Conditioning`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Sensors/Conditioning.stride#L140" target="_blank" rel="noopener" title="View source on GitHub">[Conditioning.stride:140]</a>

Rescales raw ADC readings to engineering units: Adc >> LinearCalibration(rawMin: 0 rawMax: 4095 calMin: 0.0 calMax: 3.3) >> Volts.

## Stream I/O

| I/O | Details | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Raw sensor measurement (e.g., ADC integer counts) |
| <span class="port-badge stream-out">» Out</span> | <div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">rate</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Calibrated physical signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="port-badge prop-in">↓ rawMin</span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Minimum raw input value |
| <span class="port-badge prop-in">↓ rawMax</span> <span class="prop-default">= <code>1023.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Maximum raw input value |
| <span class="port-badge prop-in">↓ calMin</span> <span class="prop-default">= <code>0.0</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Target calibrated minimum engineering unit |
| <span class="port-badge prop-in">↓ calMax</span> <span class="prop-default">= <code>3.3</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">type</span><span class="port-badge stream-out">» Out</span></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">domain</span><span class="port-badge stream-out">» Out</span></span></div> | Target calibrated maximum engineering unit |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-badge prop-in">↓ In</span> Property Input</span>
  <span class="port-legend-item"><span class="port-badge prop-out">↑ Out</span> Property Output</span>
</div>

## Usage

```stride
import Sensors::Conditioning as Conditioning;

Signal >> Conditioning::LinearCalibration(rawMin: 0.0, rawMax: 1023.0, calMin: 0.0) >> Output;
```
