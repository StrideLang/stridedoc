---
title: Follower
description: "Peak envelope follower: AudioIn >> EnvelopeFollower::Follower(attack: 0.1 release: 0.01) >> Envelope."
---

# Follower

<span class="stride-badge">Module</span> `package Dsp::Dynamics::EnvelopeFollower` &bull; Namespace: **`Dsp::Dynamics::EnvelopeFollower`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Dynamics/EnvelopeFollower.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[EnvelopeFollower.stride:8]</a>

Peak envelope follower: AudioIn >> EnvelopeFollower::Follower(attack: 0.1 release: 0.01) >> Envelope.

## Streams

| | Port identifier | Type | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon stream-in" title="Stream Input">»</span> | `InputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Input audio signal stream |
| <span class="port-icon stream-out" title="Stream Output">»</span> | `OutputPort` | `signal` | `OutputPort.rate` | `OutputPort.domain` | Extracted unipolar envelope signal |

## Properties

| | Property | Type | Default | Rate | Domain | Description |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `attack` | `signal` | `0.1` | — | `OutputPort.domain` | Attack coefficient (0.0 to 1.0, higher = faster response) |
| <span class="port-icon prop-in" title="Property Input">↓</span> | `release` | `signal` | `0.01` | — | `OutputPort.domain` | Release coefficient (0.0 to 1.0, higher = faster decay) |

<div class="port-legend">
  <span class="port-legend-item"><span class="port-icon stream-in">»</span> Stream In</span>
  <span class="port-legend-item"><span class="port-icon stream-out">»</span> Stream Out</span>
  <span class="port-legend-item"><span class="port-icon prop-in">↓</span> Property In</span>
  <span class="port-legend-item"><span class="port-icon prop-out">↑</span> Property Out</span>
</div>

## Usage

```stride
import Dsp::Dynamics::EnvelopeFollower as EnvelopeFollower;

Signal >> EnvelopeFollower::Follower(attack: 0.1, release: 0.01) >> Output;
```
