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
import Stride;

AudioIn 
  >> Filters::BiQuad(centerFrequency: 1000.0, resonance: 1.5)
  >> Math::Clamp(min: -0.9, max: 0.9)
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
# Routes Frequency into port 0, setting port 1 to constant 0.5:
Frequency >> [_, 0.5] >> Generators::Oscillator() >> AudioOut;
```

---

## 3. Package Structure & Namespace Resolution

Stride organizes source components into modular, sealed packages.

### Package Declarations
Files declare their package namespace explicitly:

```stride
package Stride::Generators;
```

When no package is declared, components placed directly at the root of the standard library reside in the top-level **`Stride`** namespace.

### Import Semantics

1. **Top-Level Library Import**:
   ```stride
   import Stride;

   # Standard root library operations are in immediate scope:
   Input >> Sin() >> Output;

   # Sub-packages are referenced via category qualification:
   Input >> Filters::LowPass(cutoff: 1000.0) >> Output;
   ```

2. **Categorical Sub-package Import**:
   ```stride
   import Stride::Generators;

   # Generator definitions become available without qualification:
   440.0 >> Oscillator() >> AudioOut;
   ```

3. **Aliased Import**:
   ```stride
   import Stride::Filters as Flt;

   Input >> Flt::BiQuad() >> Output;
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
        ModulationRate >> Generators::Oscillator() >> Math::Abs() >> LfoSignal;
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
