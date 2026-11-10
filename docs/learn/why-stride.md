# Design Rationale & Objectives

Stride is a domain-specific programming language designed for **reactive stream processing**, **real-time digital signal processing (DSP)**, and **deterministic embedded control systems**.

---

## 1. Background & Technical Motivation

Real-time signal processing in constrained embedded environments presents distinct engineering challenges that general-purpose languages are not specialized to resolve:

1. **Dynamic Signal Environments** (e.g. Max/MSP, Pure Data, SuperCollider):
   - Intuitive for visual and declarative dataflow routing.
   - Suffer from non-deterministic execution times, garbage collection pauses, dynamic typing overhead, and runtime interpreters unsuitable for bare-metal microcontrollers without an operating system.

2. **Systems Languages (C and C++)**:
   - Provide direct hardware access, zero runtime overhead, and optimal code density.
   - Demand significant manual boilerplate: managing circular ring buffers, state synchronization across interrupt boundaries, sample rate conversions, and manual vectorization.
   - Lack language-level abstractions for sample rates, signal dimensions, and reactive dataflow graphs.

**Stride formalizes dataflow graphs into a statically checked language**:
- **Declarative Stream Syntax**: Direct representation of signal graphs using forward stream routing (`>>`) and connection operators.
- **Static Rate Analysis**: Signal rates (`AudioRate`, `ControlRate`, asynchronous triggers) and buffer capacities are evaluated at compile time.
- **Zero Runtime Overhead**: The compilation pipeline lowers Stride AST representations directly to LLVM IR, emitting optimized native machine code (`.o`) and standard C interface headers without requiring a runtime interpreter or dynamic heap allocation in signal loops.

---

## 2. Core Architectural Pillars

### Deterministic Scheduling & Static Allocation
In real-time signal processing, non-deterministic latency spikes cause buffer underruns and signal dropouts. Stride requires that all signal buffers, block delays, and domain memory limits be fully resolvable at compile time. Memory layouts for active domains are allocated statically in contiguous SRAM or zero-latency scratchpad memory (zpad).

### Multi-Rate Domain Isolation
Physical systems frequently operate across heterogeneous clock domains:
- **Audio & RF DSP**: Strict sample-synchronous deadlines (e.g., 48 kHz, 96 kHz).
- **Sensor Telemetry & Motor Control**: Medium-rate discrete-time loops (e.g., 1 kHz).
- **Control & Communication**: Asynchronous, event-driven interfaces (UART, SPI, USB, MIDI).

Stride partitions execution into **Domains**. Each domain corresponds to an isolated thread of execution, microcontroller core, or hardware timer interrupt. Streams crossing domain boundaries are governed by formal synchronization protocols (counting semaphores, double-buffered ping-pong buffers, or bounded lock-free FIFOs), preventing race conditions and sample tearing.

### Heterogeneous Multi-Core Compilation
Modern microcontrollers (such as the RP2040, RP2350, and STM32 series) feature asymmetric or dual-core configurations (e.g., dual Cortex-M33, Cortex-M0+, or coupled RISC-V cores). Stride's `system` and `platform` definitions allow different domains within the same application to target distinct processing cores and hardware peripherals simultaneously.

### Native Toolchain Integration
Stride compiles directly into standard compilation units:
- Native machine object files (`.o`) relocatable across ARM, RISC-V, and x86 architectures.
- Clean ISO C99 headers (`.h`) declaring standardized lifecycle entry points: `<Domain>_init(void)` and `<Domain>_process(...)`.
- Direct integration into build systems including **CMake**, **Bazel**, and **Google Pigweed**.
