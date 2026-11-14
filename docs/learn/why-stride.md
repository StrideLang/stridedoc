# Design Rationale & Objectives

Stride is a domain-specific programming language designed for **declarative dataflow streams**, **finite state machines (FSMs)**, and **deterministic multi-rate reactive systems**.

---

## 1. Background & Technical Motivation

Building real-time reactive systems—spanning continuous signal streams, sensor loops, embedded controllers, and discrete state transitions—presents engineering challenges that general-purpose languages are not specialized to resolve:

1. **High-Level Dataflow & Reactive Environments**:
   - Provide intuitive visual or declarative routing for streams and events.
   - Suffer from non-deterministic execution times, garbage collection pauses, dynamic typing overhead, and heavyweight runtime interpreters unsuitable for bare-metal microcontrollers without an operating system.

2. **Systems Languages (C and C++)**:
   - Provide direct hardware access, zero runtime overhead, and optimal code density.
   - Demand significant manual boilerplate: managing circular ring buffers, state synchronization across interrupt boundaries, sample rate conversions, and manual vectorization.
   - Lack language-level abstractions for multi-rate domains, stream pipelines, and first-class state machines.

**Stride formalizes dataflow streams and state machines into a statically checked language**:
- **Declarative Stream Syntax**: Direct representation of signal graphs using forward stream routing (`>>`) and connection operators.
- **Finite State Machines**: First-class language constructs for states, guarded transitions, and atomic reactions.
- **Static Rate Analysis**: Signal rates (high-rate streams, control periods, asynchronous event triggers) and buffer capacities are evaluated at compile time.
- **Zero Runtime Overhead**: The compilation pipeline lowers Stride AST representations directly to LLVM IR, emitting optimized native machine code (`.o`) and standard C interface headers without requiring a runtime interpreter or dynamic heap allocation in execution loops.

---

## 2. Core Architectural Pillars

### Deterministic Scheduling & Static Allocation
In real-time systems, non-deterministic latency spikes cause buffer underruns and dropped events. Stride requires that all signal buffers, block delays, and domain memory limits be fully resolvable at compile time. Memory layouts for active domains are allocated statically in contiguous SRAM or zero-latency scratchpad memory (zpad).

### Multi-Rate Domain Isolation
Reactive systems frequently operate across heterogeneous clock domains and execution models:
- **High-Rate Synchronous Streams**: Strict sample-synchronous deadlines (e.g., audio DSP, RF processing, high-speed ADC sampling).
- **Control Loops & Telemetry**: Medium-rate discrete-time loops (e.g., 1 kHz robotics, PID, motor control).
- **Discrete State Machines & Events**: Asynchronous event handlers, protocol framing, and discrete logic.

Stride partitions execution into **Domains**. Each domain corresponds to an isolated thread of execution, microcontroller core, or hardware timer interrupt. Streams crossing domain boundaries are governed by formal synchronization protocols (counting semaphores, double-buffered ping-pong buffers, or bounded lock-free FIFOs), preventing race conditions and sample tearing.

### Finite State Machines & Discrete Logic
Beyond continuous streams, Stride natively represents discrete state transitions through formal **Finite State Machines (FSMs)**. States, transitions, guards, and transition actions are declarative language constructs rather than imperative ad-hoc control flow.

This allows Stride to cleanly model both continuous physical transducers and discrete symbolic systems. For example, Stride can describe **board games**, which are naturally modeled as finite state machines: player turns, board topologies, legal move guards, piece supplies, and win conditions are expressed as states and guarded transitions that compile into high-performance native code.

### Audio & Signal Processing as a Demanding Use Case
Digital audio processing and sound synthesis represent a prominent and demanding use case for Stride. Because real-time audio streams require strict, sample-synchronous deadlines (e.g., 44.1 kHz or 48 kHz without jitter or buffer underruns), audio serves as an effective demonstration of Stride's zero-overhead static scheduling, multi-rate domain isolation, and deterministic memory layout. The same mechanisms apply across industrial control, sensor conditioning, and robotics.

### Heterogeneous Multi-Core Compilation
Modern microcontrollers (such as the RP2040, RP2350, and STM32 series) feature asymmetric or dual-core configurations (e.g., dual Cortex-M33, Cortex-M0+, or coupled RISC-V cores). Stride's `system` and `platform` definitions allow different domains within the same application to target distinct processing cores and hardware peripherals simultaneously.

### Native Toolchain Integration
Stride compiles directly into standard compilation units:
- Native machine object files (`.o`) relocatable across ARM, RISC-V, and x86 architectures.
- Clean ISO C99 headers (`.h`) declaring standardized lifecycle entry points: `<Domain>_init(void)` and `<Domain>_process(...)`.
- Direct integration into build systems including **CMake**, **Bazel**, and **Google Pigweed**.

