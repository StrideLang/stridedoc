# Getting Started with Stride

Get up and running with the Stride language, the `stridec` compiler, and editor tooling.

---

## 1. Prerequisites

Stride builds on standard C++17 compilers and CMake:
* **CMake** (>= 3.15)
* **C++17 Compiler** (Clang 10+, GCC 9+, or MSVC 2019/2022)
* **LLVM** (14.x recommended, for JIT and native AOT code emission)

---

## 2. Installing the Toolchain (`stridelang`)

Clone the central development repository:

```bash
git clone --recursive https://github.com/StrideLang/Stride.git
cd Stride
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release
```

The build produces two core command-line tools:
- **`stride`**: Interactive execution runner and JIT environment.
- **`stridec`**: Ahead-Of-Time (AOT) compiler targeting host CPUs and embedded microcontrollers.

---

## 3. Editor Support: VS Code Extension

For syntax highlighting, auto-completion, and error diagnostics, install the official Stride Visual Studio Code extension:

1. Clone or download [`vscode-stride-lang`](https://github.com/StrideLang/vscode-stride-lang).
2. Install the `.vsix` package:
   ```bash
   code --install-extension stride-language-0.1.0.vsix
   ```
3. Any file ending in `.stride` now features full syntax highlighting and language semantics.

---

## 4. Your First Stride Program

Create a new file named `sine_synth.stride`:

```stride
use DesktopAudio version 1.0;

import Stride;

# Generate a 440 Hz concert pitch tone with 0.2 amplitude
440.0 >> Generators::Oscillator(amplitude: 0.2) >> AudioOut;
```

### Running with JIT:
To test and listen to the audio output immediately on your desktop speakers:

```bash
stride sine_synth.stride
```

### Compiling to an Embedded Object File:
To compile this DSP graph for a Raspberry Pi Pico (RP2040):

```bash
stridec --target=thumbv6m-none-eabi -mcpu=cortex-m0plus -O3 \
        --emit-header=sine_synth.h \
        -o sine_synth.o \
        sine_synth.stride
```

This emits:
1. `sine_synth.o`: Optimized bare-metal ARM machine code.
2. `sine_synth.h`: A C header you can include directly in your C/C++ firmware:
   ```c
   #include "sine_synth.h"

   int main(void) {
       sine_synth_init();
       while (1) {
           sine_synth_process();
       }
   }
   ```
