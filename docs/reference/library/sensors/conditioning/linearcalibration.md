---
title: LinearCalibration
description: "Rescales raw ADC readings to engineering units: Adc >> LinearCalibration(rawMin: 0 rawMax: 4095 calMin: 0.0 calMax: 3.3) >> Volts."
---

# LinearCalibration

<span class="stride-badge">Module</span> `package Sensors::Conditioning` &bull; Namespace: **`Sensors::Conditioning`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Sensors/Conditioning.stride#L140" target="_blank" rel="noopener" title="View source on GitHub">[Conditioning.stride:140]</a>

Rescales raw ADC readings to engineering units: Adc >> LinearCalibration(rawMin: 0 rawMax: 4095 calMin: 0.0 calMax: 3.3) >> Volts.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Raw sensor measurement (e.g., ADC integer counts) |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Calibrated physical signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `rawMin` | `OutputPort.type` | `0.0` | — | `OutputPort.domain` | Minimum raw input value |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `rawMax` | `OutputPort.type` | `1023.0` | — | `OutputPort.domain` | Maximum raw input value |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `calMin` | `OutputPort.type` | `0.0` | — | `OutputPort.domain` | Target calibrated minimum engineering unit |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `calMax` | `OutputPort.type` | `3.3` | — | `OutputPort.domain` | Target calibrated maximum engineering unit |

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
