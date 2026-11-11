---
title: LinearCalibration
description: "Rescales raw ADC readings to engineering units: Adc >> LinearCalibration(rawMin: 0 rawMax: 4095 calMin: 0.0 calMax: 3.3) >> Volts."
---

# LinearCalibration

<span class="stride-badge">Module</span> `package Sensors::Conditioning` &bull; Namespace: **`Sensors::Conditioning`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Sensors/Conditioning.stride#L135" target="_blank" rel="noopener" title="View source on GitHub">[Conditioning.stride:135]</a>

Rescales raw ADC readings to engineering units: Adc >> LinearCalibration(rawMin: 0 rawMax: 4095 calMin: 0.0 calMax: 3.3) >> Volts.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Raw sensor measurement (e.g., ADC integer counts) |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Calibrated physical signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `rawMin` | `signal` | `0.0` | — | `OutputPort.domain` | Minimum raw input value |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `rawMax` | `signal` | `1023.0` | — | `OutputPort.domain` | Maximum raw input value |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `calMin` | `signal` | `0.0` | — | `OutputPort.domain` | Target calibrated minimum engineering unit |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `calMax` | `signal` | `3.3` | — | `OutputPort.domain` | Target calibrated maximum engineering unit |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Sensors::Conditioning as Conditioning;

Signal >> Conditioning::LinearCalibration(rawMin: 0.0, rawMax: 1023.0, calMin: 0.0) >> Output;
```
