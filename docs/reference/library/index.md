---
title: Standard Library Reference
description: Specification of modules, stream processors, filters, generators, and arithmetic operations in the Stride standard library.
---

# Standard Library Reference

The Stride standard library provides verified primitives for signal flow, multi-rate digital signal processing (DSP), mathematical operations, and IO communications.

## Source Repository & Versioning

- **Upstream Repository**: [`StrideLang/strideroot`](https://github.com/StrideLang/strideroot)

- **Active Ref**: `main` (unambiguous source line links are embedded in each definition)

## Architectural Layers & Namespace Organization

The Stride standard library is organized across defined architectural layers:

### 1. Global Prelude (Auto-Imported)

Foundational primitives loaded automatically into the root namespace of every file (`strideroot/library/1.0/*.stride`). These modules and operations are called bare in global scope without imports (e.g. `Sin()`, `Sum()`, `Equal()`, `Select()`):

- **Assertions (Group)** (10 definitions): [`ExpectEqual`](/reference/library/assertions/expectequal), [`ExpectFalse`](/reference/library/assertions/expectfalse), [`ExpectGe`](/reference/library/assertions/expectge), [`ExpectGt`](/reference/library/assertions/expectgt), [`ExpectLe`](/reference/library/assertions/expectle), [`ExpectLt`](/reference/library/assertions/expectlt)...
- **BasicOperations (Group)** (3 definitions): [`Average`](/reference/library/basicoperations/average), [`Clip`](/reference/library/basicoperations/clip), [`Sum`](/reference/library/basicoperations/sum)
- **Comparisons (Group)** (8 definitions): [`AllOff`](/reference/library/comparisons/alloff), [`AllOn`](/reference/library/comparisons/allon), [`Equal`](/reference/library/comparisons/equal), [`Greater`](/reference/library/comparisons/greater), [`GreaterOrEqual`](/reference/library/comparisons/greaterorequal), [`Less`](/reference/library/comparisons/less)...
- **Control (Group)** (5 definitions): [`FallingEdge`](/reference/library/control/fallingedge), [`Latch`](/reference/library/control/latch), [`OnChange`](/reference/library/control/onchange), [`RisingEdge`](/reference/library/control/risingedge), [`Smooth`](/reference/library/control/smooth)
- **Counter (Group)** (1 definitions): [`Counter`](/reference/library/counter/counter)
- **Debug (Group)** (4 definitions): [`DebugPrint`](/reference/library/debug/debugprint), [`Error`](/reference/library/debug/error), [`Probe`](/reference/library/debug/probe), [`Watch`](/reference/library/debug/watch)
- **Domain (Group)** (1 definitions): [`Exit`](/reference/library/domain/exit)
- **Logic (Group)** (7 definitions): [`And`](/reference/library/logic/and), [`Nand`](/reference/library/logic/nand), [`Nor`](/reference/library/logic/nor), [`Not`](/reference/library/logic/not), [`Or`](/reference/library/logic/or), [`Select`](/reference/library/logic/select)...
- **Math (Group)** (21 definitions): [`Abs`](/reference/library/math/abs), [`C1`](/reference/library/math/c1), [`C2`](/reference/library/math/c2), [`C3`](/reference/library/math/c3), [`C4`](/reference/library/math/c4), [`Clamp`](/reference/library/math/clamp)...
- **QualityPolicy (Group)** (4 definitions): [`Accurate`](/reference/library/qualitypolicy/accurate), [`Compact`](/reference/library/qualitypolicy/compact), [`Fast`](/reference/library/qualitypolicy/fast), [`Optimal`](/reference/library/qualitypolicy/optimal)

### 2. Standard Library Packages (Explicitly Imported)

Cohesive, domain-specific modules organized under namespaced packages. In user code, they are imported via package statements (e.g. `import Dsp::Generators as Generators;`):


#### Package `Dsp` (`package Dsp`)

- **`Dsp (Root)`** (2 definitions): [`Level`](/reference/library/dsp/level), [`Pan`](/reference/library/dsp/pan)
- **`Dsp::FilterDesign`** (2 definitions): [`HighPassCoefficients`](/reference/library/dsp/filterdesign/highpasscoefficients), [`LowPassCoefficients`](/reference/library/dsp/filterdesign/lowpasscoefficients)
- **`Dsp::Routing`** (3 definitions): [`Crossfade`](/reference/library/dsp/routing/crossfade), [`Level`](/reference/library/dsp/routing/level), [`Pan`](/reference/library/dsp/routing/pan)
- **`Dsp::Units`** (51 definitions): [`A0`](/reference/library/dsp/units/a0), [`A1`](/reference/library/dsp/units/a1), [`A2`](/reference/library/dsp/units/a2), [`A3`](/reference/library/dsp/units/a3), [`A4`](/reference/library/dsp/units/a4), [`A5`](/reference/library/dsp/units/a5)...
- **`Dsp::Filters`** (4 definitions): [`BandPass`](/reference/library/dsp/filters/bandpass), [`BiQuad`](/reference/library/dsp/filters/biquad), [`LowPass`](/reference/library/dsp/filters/lowpass), [`Rectify`](/reference/library/dsp/filters/rectify)
- **`Dsp::Generators`** (6 definitions): [`AD`](/reference/library/dsp/generators/ad), [`BandLimitedSaw`](/reference/library/dsp/generators/bandlimitedsaw), [`Impulse`](/reference/library/dsp/generators/impulse), [`Oscillator`](/reference/library/dsp/generators/oscillator), [`Sequencer`](/reference/library/dsp/generators/sequencer), [`TableOscillator`](/reference/library/dsp/generators/tableoscillator)

#### Package `IO` (`package IO`)

- **`IO::Console`** (3 definitions): [`Log`](/reference/library/io/console/log), [`Print`](/reference/library/io/console/print), [`Println`](/reference/library/io/console/println)
- **`IO::Framing`** (5 definitions): [`CobsDelimiter`](/reference/library/io/framing/cobsdelimiter), [`SlipEnd`](/reference/library/io/framing/slipend), [`SlipEsc`](/reference/library/io/framing/slipesc), [`SlipEscEnd`](/reference/library/io/framing/slipescend), [`SlipEscEsc`](/reference/library/io/framing/slipescesc)
- **`IO::Midi`** (4 definitions): [`CcIn`](/reference/library/io/midi/ccin), [`CcOut`](/reference/library/io/midi/ccout), [`NoteIn`](/reference/library/io/midi/notein), [`NoteOut`](/reference/library/io/midi/noteout)
- **`IO::Osc`** (2 definitions): [`In`](/reference/library/io/osc/in), [`Out`](/reference/library/io/osc/out)
- **`IO::Serial`** (3 definitions): [`In`](/reference/library/io/serial/in), [`Out`](/reference/library/io/serial/out), [`Print`](/reference/library/io/serial/print)

#### Package `Math` (`package Math`)

- **`Math::Constants`** (3 definitions): [`E`](/reference/library/math/constants/e), [`Pi`](/reference/library/math/constants/pi), [`TwoPi`](/reference/library/math/constants/twopi)

