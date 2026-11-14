# Getting Started

This guide details the procedure for building the Stride toolchain, configuring developer tooling, and compiling your first Stride program.

---

## 1. System Requirements

Building the Stride compiler and runtime toolchain requires:
* **CMake** (version 3.15 or later)
* **ISO C++17 Compiler** (Clang 10+, GCC 9+, or MSVC 2019/2022)
* **LLVM** (version 14.x, required for code generation and JIT execution)
* **Flex & Bison** (required for lexical analysis and parser generation)

---

## 2. Toolchain Compilation (`stridelang`)

Clone the central development repository recursively:

```bash
git clone --recursive https://github.com/StrideLang/Stride.git
cd Stride
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release
```

The build process produces two core executables:
- **`stride`**: Interactive execution driver and JIT compilation runtime.
- **`stridec`**: Ahead-Of-Time (AOT) compiler driver supporting host and cross-compilation targets.

---

## 3. Editor Configuration

Language support, diagnostics, and syntax highlighting are available via the official Visual Studio Code extension:

1. Obtain the extension package from [`vscode-stride-lang`](https://github.com/StrideLang/vscode-stride-lang).
2. Install via the CLI:
   ```bash
   code --install-extension stride-language-0.1.0.vsix
   ```
3. Source files with the `.stride` extension will activate the language server and syntax highlighting.

---

## 4. Writing and Compiling a Program

To demonstrate Stride's stream syntax and compilation flow, consider a continuous signal generator pipeline. While Stride is used across embedded control systems, sensor processing, and discrete finite state machines, streaming to a host audio output provides a convenient, immediate way to verify real-time execution on a desktop machine:

Create a source file named `oscillator.stride`:

```stride
use DesktopAudio version 1.0;

import Dsp::Generators as Generators;

# Connect a 440 Hz generator to the primary stream output:
440.0 >> Generators::Oscillator(amplitude: 0.2) >> AudioOut;
```

### JIT Execution (Desktop Host)
To execute the pipeline immediately using the local desktop runtime:

```bash
stride oscillator.stride
```

### Cross-Compilation (Bare-Metal Embedded)
To compile the pipeline for an ARM Cortex-M0+ microcontroller (e.g. Raspberry Pi Pico RP2040):

```bash
stridec --target=thumbv6m-none-eabi -mcpu=cortex-m0plus -O3 \
        --emit-header=oscillator.h \
        -o oscillator.o \
        oscillator.stride
```

This compilation step emits:
1. `oscillator.o`: An ELF object file containing native machine code.
2. `oscillator.h`: A C interface header exposing lifecycle functions:
   ```c
   #ifndef OSCILLATOR_H
   #define OSCILLATOR_H

   #ifdef __cplusplus
   extern "C" {
   #endif

   void oscillator_init(void);
   void oscillator_process(void);

   #ifdef __cplusplus
   }
   #endif

   #endif /* OSCILLATOR_H */
   ```
