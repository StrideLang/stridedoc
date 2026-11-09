# Why Stride?

**Stride** is a modern domain-specific language designed from the ground up for **reactive signal processing**, **embedded digital signal processing (DSP)**, and **state machine coordination**.

Whether you are designing polyphonic synthesizers, real-time motor control loops, sensor fusion algorithms, or DSP filters, Stride provides the expressiveness of functional reactive stream programming combined with the raw performance and predictability of bare-metal C and LLVM machine code.

---

## The Core Philosophy

Traditional embedded DSP and real-time audio development often forces developers to choose between two undesirable extremes:

1. **High-Level Visual / Dynamic Languages** (e.g. Max/MSP, PureData, SuperCollider, Python):
   - Fast to prototype and intuitive for signal graphs.
   - Heavy runtimes, garbage collection pauses, dynamic typing overhead, and poor portability to microcontrollers.
2. **Low-Level C / C++**:
   - Highly performant and deployable to bare-metal microcontrollers (RP2040, STM32, Cortex-M).
   - High boilerplate: managing circular buffers, manual rate conversions, sample-by-sample loops, pointer arithmetic, and cross-core synchronization.

**Stride bridges this gap:**
- **Declarative Stream Syntax**: Routing audio and control signals is as clean as writing `Signal >> Filter >> Output`.
- **Compile-Time Determinism**: Buffer sizes, execution schedules, and rate lowerings are computed at compile time.
- **Zero Runtime Overhead**: Compiles Ahead-Of-Time (AOT) to native machine object code (`.o`) or clean C99/C++ headers without garbage collection or dynamic memory allocation.

---

## Key Pillars of Stride

### 1. First-Class Stream Pipelines
Signals, constants, filters, and mathematical functions connect using dataflow stream operators (`>>` and `->`). Multichannel signals and parallel stream bundles are first-class:

```stride
# Stereo panning and filtering
Input >> Filters::LowPass(cutoff: 800.0) >> [PanLeft, PanRight] >> [AudioOut[0], AudioOut[1]];
```

### 2. Multi-Rate Domains & Execution Isolation
Real-time embedded systems rarely run at a single clock rate:
- Audio DSP loops might run at **48 kHz** or **96 kHz** with hard real-time latency deadlines.
- Sensor polling and button debouncing run at **1 kHz**.
- Network communication, GUI updates, and MIDI handling run asynchronously.

In Stride, code is partitioned into **Domains**. Each domain runs under its own clock rate, platform core, or execution priority. Crossing between domains is handled declaratively using thread-safe channels, semaphores, and double-buffered token hand-offs.

### 3. Native Embedded & Microcontroller Targets
Stride is not restricted to host desktops. The `stridec` compiler targets:
- **Raspberry Pi Pico / RP2040 / RP2350** (dual Cortex-M0+ / Cortex-M33, RISC-V Hazard3).
- **STMicroelectronics STM32** (Cortex-M0+, Cortex-M4, Cortex-M7).
- **WebAssembly** (`wasm32-unknown-wasi`).
- **Arduino** libraries and bare-metal environments.

### 4. Seamless Toolchain Integration
Stride compiles directly into:
- Native `.o` object files ready to link into C/C++ firmware.
- Standalone static libraries (`.a`) or Arduino `.zip` libraries.
- Clean C99 header files (`.h`) declaring clean `<Domain>_init()` and `<Domain>_process()` hooks.
- First-class build system rules for **CMake**, **Bazel**, and **Google Pigweed**.
