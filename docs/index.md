---
layout: home

hero:
  name: Stride
  text: Dataflow Streams. Digital Signal Processing. Embedded Targets.
  tagline: A domain-specific programming language for reactive signal processing, multi-rate streams, and bare-metal embedded systems.
  image:
    src: /logo.svg
    alt: Stride Language Logo
  actions:
    - theme: brand
      text: Documentation
      link: /learn/getting-started
    - theme: alt
      text: Language Tour
      link: /learn/language-tour
    - theme: alt
      text: Standard Library
      link: /reference/library/

features:
  - title: Deterministic Dataflow Streams
    details: Statically scheduled pipeline operators (<code>&gt;&gt;</code> and <code>-&gt;</code>) connect signal generators, filters, and mathematical lowerings with explicit rate semantics.
  - title: Ahead-Of-Time Native Compilation
    details: Compiles via LLVM directly into relocatable machine object files (.o), static archives (.a), or ISO C99/C++ API headers. No runtime garbage collection.
  - title: Microcontroller & Platform Targets
    details: Architected for bare-metal targets including Raspberry Pi Pico (RP2040 / RP2350), ARM Cortex-M (STM32), WebAssembly, and host systems.
  - title: Multi-Rate Domain Isolation
    details: Formal domain semantics decouple high-rate synchronous audio processing from asynchronous control events using bounded queues and counting semaphores.
---

<div class="stride-home-preview" style="margin-top: 3.5rem; max-width: 820px; margin-left: auto; margin-right: auto;">

### Signal Processing Example

The following example defines an audio synthesis pipeline incorporating frequency modulation, arithmetic scaling, and resonant biquad filtering:

```stride
use DesktopAudio version 1.0;

import Dsp::Generators as Generators;
import Dsp::Filters as Filters;

# 1. Modulating oscillator operating at 110 Hz
# 2. Additive offset applied to carrier center frequency (440 Hz)
# 3. Carrier oscillator passed through a resonant low-pass filter
110.0 
  >> Generators::Oscillator() 
  >> [_, 150.0] >> Multiply()
  >> [_, 440.0] >> Sum()
  >> Generators::Oscillator(amplitude: 0.7) 
  >> Filters::BiQuad(mode: 0, frequency: 1200.0, q: 2.5) 
  >> AudioOut;
```

</div>
