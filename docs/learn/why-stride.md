# Design Rationale

Stride is a domain-specific programming language designed for **declarative dataflow streams**, **finite state machines**, and **deterministic multi-rate reactive systems**.

---

## Technical Motivation

Real-time reactive systems—combining continuous signal streams, sensor loops, embedded controllers, and discrete state transitions—face a fundamental trade-off:

1. **High-Level Dataflow & Reactive Environments**: Provide intuitive stream routing and event handling, but introduce garbage collection pauses, dynamic typing overhead, and heavyweight runtime interpreters unsuitable for bare-metal microcontrollers.
2. **Systems Languages (C and C++)**: Deliver bare-metal access, zero runtime overhead, and optimal code density, but require substantial manual boilerplate for ring buffers, rate conversions, cross-interrupt synchronization, and state machine state tracking.

**Stride resolves this trade-off through compile-time analysis**:
- **Declarative Streams**: Direct representation of signal graphs using forward stream routing (`>>`) and parallel evaluation bundles (`[...]`).
- **First-Class State Machines**: Native syntax for states, transitions, guard conditions, and reaction handlers.
- **Static Rate Inference**: Multi-rate stream alignment, automatic up/downsampling, and buffer sizing validated at compile time.
- **Zero Runtime Overhead**: The compilation pipeline lowers the AST via LLVM directly into native machine code (`.o`, `.a`) and standard C99 interface headers (`.h`), with zero dynamic heap allocation in execution loops.

---

## Core Architectural Pillars

### Deterministic Scheduling & Static Allocation
Hard real-time systems cannot tolerate unpredictable latency spikes or memory fragmentation. Stride requires that all buffer capacities, delay lines, and domain state sizes be resolved at compile time. Domain memory layouts are statically allocated in contiguous SRAM or scratchpad memory, eliminating heap allocation during execution.

### Multi-Rate Domain Isolation
Reactive systems operate across distinct temporal scales:
- **Synchronous Streams**: Strict sample-synchronous deadlines (e.g., audio DSP, sensor sampling).
- **Periodic Control Loops**: Medium-rate discrete-time loops (e.g., 1 kHz robotics, PID controllers).
- **Asynchronous Events**: Event triggers, protocol framing, and discrete state transitions.

Stride partitions execution into **Domains**, mapping each to an OS thread, CPU core, or hardware timer interrupt. Cross-domain streams use formal synchronization (bounded lock-free FIFOs, double-buffer ping-pong DMA, or semaphores) to eliminate race conditions and sample tearing.

### First-Class State Machines & Discrete Logic
Continuous dataflow streams and discrete state machines coexist natively. States, transitions, guards, and transition actions are explicit language constructs rather than imperative control flow. This cleanly models hybrid systems—from signal processors with operational modes to discrete state machines such as communication protocols, sequencers, and board games.

### Audio & Signal Processing as a Reference Domain
Digital audio processing serves as a primary benchmark for Stride. Sample-synchronous deadlines (44.1 kHz / 48 kHz) demand zero-jitter execution, low latency, and zero tolerance for dropouts. The static scheduling, multi-rate inference, and deterministic memory layouts proven in audio apply directly to motor control, sensor telemetry, and embedded robotics.

### Heterogeneous & Multi-Core Targets
Modern microcontrollers (such as the RP2040, RP2350, and STM32 series) feature asymmetric or multi-core architectures. Stride's `platform` and `system` declarations allow different domains within a single application to target separate cores and peripheral buses simultaneously.

### Native Toolchain Integration
Stride integrates directly into standard C and C++ workflows:
- Compiles to native object files (`.o`, `.a`) across ARM Cortex-M, RISC-V, WebAssembly, and host x86_64/AArch64 targets.
- Emits clean ISO C99 headers declaring lifecycle entry points (`<Domain>_init(void)` and `<Domain>_process(...)`).
- Integrates into build pipelines via standard **CMake** modules (`find_package(Stride)` and `stride_target_sources()`).
