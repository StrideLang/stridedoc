---
title: Follower
description: "Peak envelope follower with attack and release times in seconds: AudioIn >> EnvelopeFollower::Follower(attack: 0.01 release: 0.1) >> Envelop"
---

# Follower

<span class="stride-badge">Module</span> `package Dsp::Dynamics::EnvelopeFollower` &bull; Namespace: **`Dsp::Dynamics::EnvelopeFollower`** <a class="stride-source-link" href="https://github.com/StrideLang/strideroot/blob/main/library/1.0/Dsp/Dynamics/EnvelopeFollower.stride#L8" target="_blank" rel="noopener" title="View source on GitHub">[EnvelopeFollower.stride:8]</a>

Peak envelope follower with attack and release times in seconds: AudioIn >> EnvelopeFollower::Follower(attack: 0.01 release: 0.1) >> Envelope. Times are converted against the rate of the output, so the behaviour does not depend on the sample rate.

## Stream I/O

| I/O | Port Name | Description |
| :-: | :--- | :--- |
| <span class="port-badge stream-in">» In</span> | `InputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Input audio signal stream |
| <span class="port-badge stream-out">» Out</span> | `OutputPort`<div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-rate" title="Evaluation Rate"><span class="bubble-key">R</span><code>OutputPort.rate</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Extracted unipolar envelope signal |

## Properties

| Property | Description |
| :--- | :--- |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>attack</code></span> <span class="prop-default">= <code>0.01</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Attack time constant in seconds: how fast the envelope rises (default 0.01). 0 follows rising peaks instantly |
| <span class="prop-badge prop-in"><span class="prop-arrow">↓</span> <code>release</code></span> <span class="prop-default">= <code>0.1</code></span><div class="attr-bubble-group"><span class="attr-bubble bubble-type" title="Type"><span class="bubble-key">T</span><code>OutputPort.type</code></span><span class="attr-bubble bubble-domain" title="Clock Domain"><span class="bubble-key">D</span><code>OutputPort.domain</code></span></div> | Release time constant in seconds: how fast the envelope falls (default 0.1). 0 follows falling levels instantly |

<div class="port-legend">
  <span class="port-legend-item"><span class="bubble-key type-key">T</span> Type</span>
  <span class="port-legend-item"><span class="bubble-key rate-key">R</span> Rate</span>
  <span class="port-legend-item"><span class="bubble-key domain-key">D</span> Domain</span>
</div>

## Usage

```stride
import Dsp::Dynamics::EnvelopeFollower as EnvelopeFollower;

Signal >> EnvelopeFollower::Follower(attack: 0.01, release: 0.1) >> Output;
```
