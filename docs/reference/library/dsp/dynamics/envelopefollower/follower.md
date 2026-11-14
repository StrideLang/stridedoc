---
title: Follower
description: "Peak envelope follower with attack and release times in seconds: AudioIn >> EnvelopeFollower::Follower(attack: 0.01 release: 0.1) >> Envelop"
---

# Follower

<span class="stride-badge">Module</span> `package Dsp::Dynamics::EnvelopeFollower` &bull; Namespace: **`Dsp::Dynamics::EnvelopeFollower`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Dynamics/EnvelopeFollower.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[EnvelopeFollower.stride:8]</a>

Peak envelope follower with attack and release times in seconds: AudioIn >> EnvelopeFollower::Follower(attack: 0.01 release: 0.1) >> Envelope. Times are converted against the rate of the output, so the behaviour does not depend on the sample rate.

## Stream I/O

| | Port Name | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Input audio signal stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `OutputPort.type` | `OutputPort.rate` | `OutputPort.domain` | Extracted unipolar envelope signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `attack` | `OutputPort.type` | `0.01` | — | `OutputPort.domain` | Attack time constant in seconds: how fast the envelope rises (default 0.01). 0 follows rising peaks instantly |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `release` | `OutputPort.type` | `0.1` | — | `OutputPort.domain` | Release time constant in seconds: how fast the envelope falls (default 0.1). 0 follows falling levels instantly |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Dynamics::EnvelopeFollower as EnvelopeFollower;

Signal >> EnvelopeFollower::Follower(attack: 0.01, release: 0.1) >> Output;
```
