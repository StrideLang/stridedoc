---
layout: home

hero:
  name: Stride
  text: Streams. Audio DSP. Microcontrollers.
  tagline: A modern domain-specific language for reactive signal processing, state machines, and bare-metal embedded targets.
  image:
    src: /logo.svg
    alt: Stride Language Logo
  actions:
    - theme: brand
      text: Get Started
      link: /learn/getting-started
    - theme: alt
      text: Standard Library
      link: /reference/library/
    - theme: alt
      text: Language Tour
      link: /learn/language-tour

features:
  - icon: 🌊
    title: Reactive Stream Pipelines
    details: Connect oscillators, filters, and mathematical operators with expressive stream routing (<code>&gt;&gt;</code> and <code>-&gt;</code>) running at distinct sample rates.
  - icon: ⚡
    title: Ahead-Of-Time Native Compilation
    details: Compiles directly via LLVM to native machine code (.o), static libraries, or clean C99/C++ API headers with zero runtime overhead.
  - icon: 🎛️
    title: Embedded & MCU First-Class
    details: First-class targets for Raspberry Pi Pico (RP2040 / RP2350), STM32 Cortex-M, Arduino, and bare-metal RTOS environments.
  - icon: 🔄
    title: Multi-Rate Domains & Safety
    details: Isolate real-time DSP from asynchronous control logic using formal Domain boundaries, semaphores, and sealed package namespaces.
---

<div class="stride-home-preview" style="margin-top: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">

### A Taste of Stride

```stride
use DesktopAudio version 1.0;

import Stride;

# Generate an FM-modulated synthesizer voice:
# 1. Modulator oscillator at 110 Hz
# 2. Scale modulation depth and add to carrier frequency (440 Hz)
# 3. Stream carrier output through a resonant BiQuad filter into audio output

[110.0, 150.0] 
  >> Generators::Oscillator() 
  >> [_, 440.0] >> Add()
  >> Generators::Oscillator(amplitude: 0.7) 
  >> Filters::BiQuad(centerFrequency: 1200.0, resonance: 2.5) 
  >> AudioOut;
```

</div>
