---
layout: home

hero:
  name: Stride
  text: Declarative Dataflow & Reactive Architecture
  tagline: A domain-specific programming language for declarative dataflow streams, finite state machines, and multi-rate reactive systems.
  actions:
    - theme: brand
      text: Get Started
      link: /learn/getting-started
    - theme: alt
      text: Language Tour
      link: /learn/language-tour
    - theme: alt
      text: Standard Library
      link: /reference/library/

features:
  - title: Dataflow Stream Syntax
    details: Programs are directed graphs of synchronous and asynchronous streams connected via <code>&gt;&gt;</code>. Stride is a code generator, not a dynamic graph interpreter.
  - title: Multi-Rate Evaluation
    details: Signals declare or inherit discrete evaluation rates. Clock domains, sample-rate transitions, and event decoupling are verified at compile time.
  - title: Hardware Independence
    details: Declarative platform and system abstractions isolate computation topologies from microcontrollers (ARM Cortex-M, AVR, RISC-V), hardware peripherals, and host runtime environments.
  - title: Native Code Generation
    details: Lowers via LLVM directly into ISO C99 interface headers, static libraries, and relocatable machine object files (.o). Zero garbage collection and zero heap allocation in signal loops.
---

<div class="showcase-grid">

  <div class="showcase-card">
    <h4>1. Continuous Stream Processing</h4>
    <p>Connecting signal producers, scaling operations, and multi-rate filters into a stream pipeline (e.g., audio DSP, sensor conditioning, or telemetry):</p>

```stride
use DesktopAudio version 1.0;

import Dsp::Generators as Generators;
import Dsp::Filters as Filters;

# 110 Hz carrier modulated into a resonant biquad filter
110.0 
  >> Generators::Oscillator() 
  >> [_, 150.0] >> Multiply()
  >> [_, 440.0] >> Sum()
  >> Generators::Oscillator(amplitude: 0.7) 
  >> Filters::BiQuad(mode: 0, frequency: 1200.0, q: 2.5) 
  >> AudioOut;
```
  </div>

  <div class="showcase-card">
    <h4>2. Multi-Rate Domain & Event Reactions</h4>
    <p>Decoupling asynchronous hardware triggers from deterministic high-rate signal streams:</p>

```stride
# Asynchronous button input triggers an atomic parameter change
# without locking or interrupting the high-rate processing domain
reaction ToggleMute {
    ports: [
        propertyInputPort TriggerPort { name: "trigger" entity: MuteTrigger }
        mainOutputPort StatePort { entity: MuteState }
    ]
    entities: [
        switch MuteTrigger {}
        switch MuteState { default: off }
    ]
    streams: [
        MuteTrigger >> Not() >> MuteState;
    ]
}
```
  </div>

  <div class="showcase-card">
    <h4>3. State Machines & Discrete Logic</h4>
    <p>Stride can also describe discrete systems such as board games, which are modeled as finite state machines with turn rules and transition guards:</p>

```stride
# Finite state machine transition for a turn-based board game
transition PlacePiece[Index in 0:8] {
    label: "Place Piece"
    guard: [ IsEmpty[Index], Not(GameOver) ] >> And()
    onTransition: [ Place(supply: PlayerPiece, location: Index); ]
    targetState: NextTurn
}
```
  </div>

  <div class="showcase-card">
    <h4>4. Direct Native Compilation</h4>
    <p>Compiling the same Stride algorithm directly for an ARM Cortex-M0+ microcontroller (Raspberry Pi Pico RP2040):</p>

```bash
# Compiles Stride source to relocatable machine object code and C99 interface header
stridec --target=thumbv6m-none-eabi -mcpu=cortex-m0plus -O3 \
        --emit-header=system.h \
        -o system.o \
        system.stride
```
  </div>

</div>

<div class="citation-block">
  <h4>Academic Provenance & Publications</h4>
  <p>
    Stride was designed and developed by Andrés Cabrera and Joseph Tilbian at the University of California, Santa Barbara.
  </p>
  <p>
    • J. Tilbian and A. Cabrera. <em>Stride: A declarative and reactive language for sound synthesis and beyond.</em> In Proceedings of the International Computer Music Conference (ICMC), Utrecht, 2016.<br>
    • J. Tilbian and A. Cabrera. <em>Stride for Interactive Musical Instrument Design.</em> In Proceedings of the International Conference on New Interfaces for Musical Expression (NIME), Copenhagen, 2017.<br>
    • J. Tilbian, A. Cabrera, S. Martin, and L. Olczyk. <em>Stride on Saturn M7 for Interactive Musical Instrument Design.</em> In Proceedings of the International Conference on New Interfaces for Musical Expression (NIME), Copenhagen, 2017.
  </p>
  <p style="margin-top: 0.75rem; font-size: 0.8rem;">
    Licensed under the terms of the 3-Clause BSD License.
  </p>
</div>
