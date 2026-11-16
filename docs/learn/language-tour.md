# Language Tour

A technical overview of the grammar, type system, stream operators, and compilation semantics of Stride.

---

## 1. Declarations & Streams

At the language level, Stride programs are structured around two fundamental syntactical constructs:

1. **Declarations**: Define the entities of the system—signals, switches, buffers, and callables—specifying their types, rates, clock domains, and initial default values.
2. **Streams**: Define the active computation and dataflow routing using the forward stream operator `>>`, directing values from producers through transformations to consumers.

### How Declarations and Streams Interact

Declared entities serve as the sources, destinations, and control flags for streams. Streams read from declared inputs, transform values through arithmetic operators or callables, and continuously update declared outputs or state switches:

```stride
# 1. Declarations: Define stateful entities and parameters
signal SensorRaw   {}
signal SensorClean { default: 0.0 }
signal Threshold   { default: 75.0 }
switch Overheated  { default: off }

# 2. Streams: Connect, transform, and update declared entities
# Filter raw input and route into the clean signal:
SensorRaw >> LowPass(frequency: 20.0) >> SensorClean;

# Evaluate condition and update the state switch:
[ SensorClean, Threshold ] >> Greater() >> Overheated;
```

Pipelines can be connected sequentially or nested. The compiler resolves signal types and statically validates rate compatibility at each connection in the stream graph:

```stride
import Dsp::Filters as Filters;

SignalIn 
  >> Filters::BiQuad(frequency: 1000.0, q: 1.5)
  >> Clamp(min: -0.9, max: 0.9)
  >> SignalOut;
```

---

## 2. Arrays & Parallel Dataflow

Bracket syntax `[...]` designates **arrays**—ordered collections of signals evaluated in parallel:

```stride
# Fan-out: A single signal dispatched to multiple destinations
InputSignal >> [ BranchA, BranchB ];

# Fan-in: Multi-channel signals routed into a multi-port processor
[ LeftChannel, RightChannel ] >> StereoProcessor() >> [ SignalOut[0], SignalOut[1] ];
```

The underscore token `_` serves as a positional placeholder when feeding into a subset of an array's input slots:

```stride
import Dsp::Generators as Generators;

# Routes Frequency into port 0, setting port 1 to constant 0.5:
Frequency >> [_, 0.5] >> Generators::Oscillator() >> StreamOut;
```

---

## 3. Packages & Imports

Stride provides a global prelude of core mathematical and logical primitives (`Sin()`, `Clamp()`, `Abs()`, `Select()`, `Sum()`, etc.) that are automatically available everywhere without import statements:

```stride
# Global prelude primitives require no imports:
SignalIn >> Sin() >> Clamp(min: -1.0, max: 1.0) >> SignalOut;
```

Additional modules and libraries are organized into packages and brought into scope using `import`:

```stride
# Import with an alias for clean namespacing:
import Dsp::Filters as Filters;
import Dsp::Generators as Generators;
import IO::Console as Console;

# In use:
440.0 >> Generators::Oscillator() >> Filters::LowPass(frequency: 1000.0) >> SignalOut;
SignalOut >> Console::Print();
```

Source files declare their package namespace with `package Name;`.

---

## 4. Callables: Modules, Reactions, and Loops

In Stride, encapsulated units of processing logic that can be invoked inside streams are called **Callables**. Stride provides three distinct types of callables: **`module`**, **`reaction`**, and **`loop`**.

### Callables in Use

All three callables are invoked directly within stream pipelines using `>>`:

```stride
# 1. Module: Synchronous stream processing
InputSignal >> GainOffset(gain: 2.0, offset: 0.5) >> OutputSignal;

# 2. Reaction: Event-triggered or condition-driven execution
ButtonPress >> ToggleMute() >> MuteState;

# 3. Loop: Iterative evaluation within a single tick
VectorBundle >> SumArray() >> TotalReduction;
```

### Key Differences

| Callable Type | Execution Model | Typical Use Cases |
| :--- | :--- | :--- |
| **`module`** | **Synchronous / Continuous** | Evaluates on every tick of its rate domain. Transforms streaming inputs to outputs with deterministic, sample-synchronous timing (e.g. digital filters, oscillators, scaling). |
| **`reaction`** | **Asynchronous / Event-Driven** | Executes only when triggered by an incoming event, switch edge, or buffer condition. Updates state atomically without busy-waiting (e.g. parameter updates, button handling, state changes). |
| **`loop`** | **Iterative / Multi-Step** | Iterates multiple times within a single tick until a termination condition is reached (`terminateWhen:`). Ideal for array reductions, matrix iterations, or batch operations. |

### Declaring a Callable

Callables define their external interface through **ports** (main streaming inputs/outputs and named property parameters), internal **entities** (signals, switches, or local state), and internal **streams**:

```stride
module GainOffset {
    ports: [
        mainInputPort InputPort { entity: Input }
        mainOutputPort OutputPort { entity: Output }
        propertyInputPort GainPort { name: "gain" entity: Gain default: 1.0 }
        propertyInputPort OffsetPort { name: "offset" entity: Offset default: 0.0 }
    ]
    entities: [
        signal Input {}
        signal Output {}
        signal Gain { default: 1.0 }
        signal Offset { default: 0.0 }
    ]
    streams: [
        Input * Gain + Offset >> Output;
    ]
}
```

---

## 5. Rate Typing & Domain Boundaries

Every signal in Stride is associated with a discrete rate type:
* `AudioRate`: Evaluated synchronously at high streaming rates (e.g., 44.1 kHz, 48 kHz for audio or fast sensor streams).
* `ControlRate`: Evaluated at a sub-sampled control period (e.g., 1 kHz for telemetry, PID, or motor control).
* `none`: Static constants, discrete asynchronous events, or state machine transitions.

Signals operating at distinct rates or hosted on separate processing cores cannot be directly connected through synchronous stream operators. They must be routed through formal **Domains** using explicitly declared synchronization primitives.

---

## 6. Finite State Machines & Discrete Logic

In addition to continuous dataflow streams, Stride natively represents discrete state logic through **Finite State Machines (FSMs)**. States, transitions, guards, and transition actions are declared as first-class language constructs:

```stride
# A state machine transition with guard conditions and actions
transition PlacePiece[Index in 0:8] {
    label: "Place Piece"
    guard: [ IsEmpty[Index], Not(GameOver) ] >> And()
    onTransition: [ Place(supply: PlayerPiece, location: Index); ]
    targetState: NextTurn
}
```

This allows Stride to describe not only physical signal processors, but also discrete systems such as **board games**—which can be naturally formulated as finite state machines with formal turn structures, move validation guards, and board states.

---

## 7. Buffers & Frame Processing

A **`buffer`** in Stride is a first-class entity for storing sliding or circular windows of stream data. Buffers bridge continuous sample-by-sample streams with block- or frame-based processing (such as spectral analysis, FIR filtering, or batch reductions).

### Buffer Declaration

A buffer specifies its storage capacity, and optionally a frame size and hop step:

```stride
buffer AnalysisBuffer {
    capacity: 1024
    frameSize: 256
    hop: 128
}
```

### Buffers in Streams

1. **Continuous Streaming In**: Push streaming samples into the buffer:
   ```stride
   InputStream >> AnalysisBuffer;
   ```

2. **Zero-Copy Frame Peeking**: Once accumulated, `AnalysisBuffer.frame` provides a zero-copy view of the oldest samples in the active window directly into downstream loops or reactions:
   ```stride
   AnalysisBuffer.frame >> ProcessWindow() >> SpectrumOut;
   ```

3. **Event Notification (`ready`)**: The `ready` property fires a trigger tick whenever a new frame has completed:
   ```stride
   AnalysisBuffer.ready >> reaction {
       AnalysisBuffer.frame >> ComputeFft();
   };
   ```

4. **Stream Delay Lines**: A circular buffer can also serve as a direct FIFO delay line:
   ```stride
   buffer DelayRing { capacity: 64 }

   InputStream >> DelayRing >> DelayedStream;
   ```
