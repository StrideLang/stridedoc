# Stride Language Tour

A guided tour of the fundamental concepts, syntax, and idioms in Stride.

---

## 1. Streams & The Stream Operator (`>>`)

In Stride, computation is expressed as data flowing through streams:

```stride
Source >> Transform >> Destination;
```

Streams can chain multiple processing stages linearly:

```stride
import Stride;

AudioIn 
  >> Filters::BiQuad(centerFrequency: 1000.0, resonance: 1.5)
  >> Math::Clip(min: -0.9, max: 0.9)
  >> AudioOut;
```

---

## 2. Bundles & Parallel Streams

Brackets `[...]` declare **stream bundles** (multichannel streams or parallel operations):

```stride
# Fan-out: Sending one signal into two parallel paths
Signal >> [ PathA, PathB ];

# Fan-in: Combining multiple signals into a dual-input block
[ SignalLeft, SignalRight ] >> StereoProcessor() >> [ AudioOut[0], AudioOut[1] ];
```

You can use the placeholder `_` to position inputs into specific argument slots:

```stride
# Feeds Frequency into slot 0, keeping Amplitude at 0.5
Frequency >> [_, 0.5] >> Generators::Oscillator() >> AudioOut;
```

---

## 3. Packages and Imports

Stride organizes modular components into sealed packages:

### Canonical Package Declarations
Files declare their logical namespace using the `package` keyword:

```stride
package Stride::Generators;
```

### The 3-Tier Import Convention

1. **Import the whole library**:
   ```stride
   import Stride;

   # Access modules with category qualification:
   Generators::Oscillator() >> Filters::LowPass() >> AudioOut;
   ```

2. **Import a specific category**:
   ```stride
   import Stride::Generators;

   # Access modules directly:
   Oscillator(frequency: 440.0) >> AudioOut;
   ```

3. **Import with an alias**:
   ```stride
   import Stride::Generators as Gen;

   Gen::Oscillator(frequency: 440.0) >> AudioOut;
   ```

---

## 4. Modules, Ports, and Properties

A **Module** encapsulates signals, inner state, and processing streams. Its external interface is defined by **Ports**:

```stride
module Tremolo {
    ports: [
        mainInputPort InputPort {
            entity: Input
            meta: "Audio signal to modulate"
        },
        mainOutputPort OutputPort {
            entity: Output
            meta: "Tremolo-modulated audio stream"
        },
        propertyInputPort RateProperty {
            name: "rate"
            entity: LfoRate
            default: 5.0
            meta: "LFO modulation speed in Hz"
        }
    ]
    entities: [
        signal Input {}
        signal Output {}
        signal LfoRate { default: 5.0 }
        signal LfoOut {}
    ]
    streams: [
        # Generate low-frequency modulation between 0.2 and 1.0
        LfoRate >> Generators::Oscillator() >> Math::Abs() >> LfoOut;
        Input * LfoOut >> Output;
    ]
    meta: "Applies amplitude modulation (tremolo) to the audio stream."
}
```

---

## 5. Rates and Domains

Stride signals are strongly associated with execution rates:
* `AudioRate`: High-frequency streaming rate (e.g. 48,000 samples/sec).
* `ControlRate`: Sub-sampled rate for envelopes, UI parameters, and sensor readings.
* `none`: Static constants or asynchronous event triggers.

When streams flow across different execution domains or cores, Stride enforces explicit Domain declarations to guarantee thread safety and prevent sample tearing.
