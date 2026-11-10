# Language Tour

A technical overview of the grammar, type system, stream operators, and compilation semantics of Stride.

---

## 1. Stream Operations & Dataflow

Computation in Stride is formulated as directed dataflow graphs. The forward stream operator `>>` routes signal values from producers to consumers:

```stride
Source >> Transform >> Destination;
```

Pipelines can be connected sequentially. The compiler resolves signal types and validates rate compatibility at each connection:

```stride
import Dsp::Filters as Filters;

AudioIn 
  >> Filters::BiQuad(centerFrequency: 1000.0, resonance: 1.5)
  >> Clamp(min: -0.9, max: 0.9)
  >> AudioOut;
```

---

## 2. Bundles & Parallel Dataflow

Bracket syntax `[...]` designates **bundles**—ordered collections of signals evaluated in parallel:

```stride
# Fan-out: A single signal dispatched to multiple destinations
InputSignal >> [ BranchA, BranchB ];

# Fan-in: Multi-channel signals routed into a multi-port processor
[ LeftChannel, RightChannel ] >> StereoProcessor() >> [ AudioOut[0], AudioOut[1] ];
```

The underscore token `_` serves as a positional placeholder when feeding into a subset of a bundle's input slots:

```stride
import Dsp::Generators as Generators;

# Routes Frequency into port 0, setting port 1 to constant 0.5:
Frequency >> [_, 0.5] >> Generators::Oscillator() >> AudioOut;
```

---

## 3. Package Structure & Namespace Resolution

Stride organizes source components across defined architectural layers:

### 1. Global Prelude (Auto-Imported)
Foundational primitives (`Sin()`, `Abs()`, `Floor()`, `Clamp()`, `Equal()`, `Select()`, `Sum()`, `OnChange()`) reside in the root prelude (`strideroot/library/1.0/*.stride`) and are available in every file without import statements:

```stride
# Calling Global Prelude primitives directly:
Input >> Sin() >> Clamp(min: -1.0, max: 1.0) >> Output;
```

### 2. Standard Library Packages
Domain-specific modules are grouped into explicit packages:
- **`package Dsp`**: Digital signal processing, audio filters, synthesis generators, and routing.
- **`package IO`**: Console telemetry, serial communication, OSC networking, and MIDI events.
- **`package Math`**: Mathematical constants (`Math::Pi`, `Math::TwoPi`, `Math::E`).

### Package Declarations
Files declare their logical package explicitly:

```stride
package Dsp::Generators;
```

### Import Semantics

1. **Sub-package Import with Alias**:
   ```stride
   import Dsp::Generators as Generators;
   import Dsp::Filters as Filters;

   Input >> Generators::Oscillator(frequency: 440.0) >> Filters::LowPass(frequency: 1200.0) >> Output;
   ```

2. **Package Root Import**:
   ```stride
   import Dsp;

   # Access members via package qualification:
   Input >> Dsp::Level(gain: 0.8) >> Output;
   ```

3. **IO and Math Package Imports**:
   ```stride
   import IO::Console as Console;
   import Math;

   Signal * Math::Pi >> Console::Print();
   ```

---

## 4. Modules, Ports, and Properties

A **Module** encapsulates computational state, internal signals, and processing logic. Its external interface is defined strictly through **Ports**:

```stride
module Tremolo {
    ports: [
        mainInputPort InputPort {
            entity: Input
            meta: "Input audio signal"
        },
        mainOutputPort OutputPort {
            entity: Output
            meta: "Modulated audio stream output"
        },
        propertyInputPort RateProperty {
            name: "rate"
            entity: ModulationRate
            default: 5.0
            meta: "Modulation frequency in Hz"
        }
    ]
    entities: [
        signal Input {}
        signal Output {}
        signal ModulationRate { default: 5.0 }
        signal LfoSignal {}
    ]
    streams: [
        ModulationRate >> Generators::Oscillator() >> Abs() >> LfoSignal;
        Input * LfoSignal >> Output;
    ]
    meta: "Applies amplitude modulation to an incoming signal."
}
```

### Port Classifications
- `mainInputPort` / `mainOutputPort`: Primary synchronous streaming data paths.
- `propertyInputPort` / `propertyOutputPort`: Named configuration attributes accessible via keyword arguments (e.g., `rate: 5.0`).

---

## 5. Rate Typing & Domain Boundaries

Every signal in Stride is associated with a discrete rate type:
* `AudioRate`: Evaluated synchronously at the primary audio sampling frequency (e.g., 48 kHz).
* `ControlRate`: Evaluated at a sub-sampled control period (e.g., 1 kHz).
* `none`: Static constants or discrete asynchronous events.

Signals operating at distinct rates or hosted on separate processing cores cannot be directly connected through synchronous stream operators. They must be routed through formal **Domains** using explicitly declared synchronization primitives.
