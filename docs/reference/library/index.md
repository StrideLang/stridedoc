---
title: Standard Library Reference
description: Specification of modules, stream processors, filters, generators, and arithmetic operations in the Stride standard library.
---

# Standard Library Reference

The Stride standard library provides verified primitives for signal flow, multi-rate stream processing, control systems, mathematical operations, and IO communications.

## Source Repository & Versioning

- **Upstream Repository**: [`StrideLang/strideroot`](https://github.com/StrideLang/strideroot)

- **Active Ref**: `main` (unambiguous source line links are embedded in each definition)

## Architectural Layers & Namespace Organization

> **Alphabetical Directory**: Looking for a specific function, filter, or operator? Browse the [Standard Library Symbol Index (A–Z)](/reference/library/symbols).

The Stride standard library is organized across defined architectural layers:

### 1. Global Prelude (Auto-Imported)

Foundational primitives loaded automatically into the root namespace of every file (`strideroot/library/1.0/*.stride`). These modules and operations are called bare in global scope without imports (e.g. `Sin()`, `Sum()`, `Equal()`, `Select()`):

- **Assertions (Group)** (10 definitions): [`ExpectEqual`](/reference/library/assertions/expectequal), [`ExpectFalse`](/reference/library/assertions/expectfalse), [`ExpectGe`](/reference/library/assertions/expectge), [`ExpectGt`](/reference/library/assertions/expectgt), [`ExpectLe`](/reference/library/assertions/expectle), [`ExpectLt`](/reference/library/assertions/expectlt)...
- **BasicOperations (Group)** (3 definitions): [`Average`](/reference/library/basicoperations/average), [`Clip`](/reference/library/basicoperations/clip), [`Sum`](/reference/library/basicoperations/sum)
- **Comparisons (Group)** (8 definitions): [`AllOff`](/reference/library/comparisons/alloff), [`AllOn`](/reference/library/comparisons/allon), [`Equal`](/reference/library/comparisons/equal), [`Greater`](/reference/library/comparisons/greater), [`GreaterOrEqual`](/reference/library/comparisons/greaterorequal), [`Less`](/reference/library/comparisons/less)...
- **Control (Group)** (5 definitions): [`FallingEdge`](/reference/library/control/fallingedge), [`Latch`](/reference/library/control/latch), [`OnChange`](/reference/library/control/onchange), [`RisingEdge`](/reference/library/control/risingedge), [`Smooth`](/reference/library/control/smooth)
- **Counter (Group)** (1 definitions): [`Counter`](/reference/library/counter/counter)
- **Debug (Group)** (3 definitions): [`DebugPrint`](/reference/library/debug/debugprint), [`Error`](/reference/library/debug/error), [`Probe`](/reference/library/debug/probe)
- **Domain (Group)** (1 definitions): [`Exit`](/reference/library/domain/exit)
- **Logic (Group)** (7 definitions): [`And`](/reference/library/logic/and), [`Nand`](/reference/library/logic/nand), [`Nor`](/reference/library/logic/nor), [`Not`](/reference/library/logic/not), [`Or`](/reference/library/logic/or), [`Select`](/reference/library/logic/select)...
- **Math (Group)** (17 definitions): [`Abs`](/reference/library/math/abs), [`Clamp`](/reference/library/math/clamp), [`Cos`](/reference/library/math/cos), [`Divide`](/reference/library/math/divide), [`Exp`](/reference/library/math/exp), [`Floor`](/reference/library/math/floor)...
- **QualityPolicy (Group)** (4 definitions): [`Accurate`](/reference/library/qualitypolicy/accurate), [`Compact`](/reference/library/qualitypolicy/compact), [`Fast`](/reference/library/qualitypolicy/fast), [`Optimal`](/reference/library/qualitypolicy/optimal)
- **Random (Group)** (2 definitions): [`RandomChance`](/reference/library/random/randomchance), [`RandomInt`](/reference/library/random/randomint)

### 2. Standard Library Packages (Explicitly Imported)

Cohesive, domain-specific modules organized under namespaced packages. In user code, they are imported via package statements (e.g. `import Dsp::Generators as Generators;`):


#### Package Control

- **`Control`** (7 definitions): [`Clarke`](/reference/library/control/foc/clarke), [`Hysteresis`](/reference/library/control/hysteresis/hysteresis), [`InverseClarke`](/reference/library/control/foc/inverseclarke), [`InversePark`](/reference/library/control/foc/inversepark), [`Park`](/reference/library/control/foc/park), [`Pid`](/reference/library/control/pid/pid)...

#### Package Dsp

- **`Dsp::FilterDesign`** (7 definitions): [`Coefficients`](/reference/library/dsp/filterdesign/coefficients), [`ModeAllPass`](/reference/library/dsp/filterdesign/modeallpass), [`ModeBandPass`](/reference/library/dsp/filterdesign/modebandpass), [`ModeHighPass`](/reference/library/dsp/filterdesign/modehighpass), [`ModeLowPass`](/reference/library/dsp/filterdesign/modelowpass), [`ModeNotch`](/reference/library/dsp/filterdesign/modenotch)...
- **`Dsp::Routing`** (3 definitions): [`Crossfade`](/reference/library/dsp/routing/crossfade), [`Level`](/reference/library/dsp/routing/level), [`Pan`](/reference/library/dsp/routing/pan)
- **`Dsp::Units`** (51 definitions): [`A0`](/reference/library/dsp/units/a0), [`A1`](/reference/library/dsp/units/a1), [`A2`](/reference/library/dsp/units/a2), [`A3`](/reference/library/dsp/units/a3), [`A4`](/reference/library/dsp/units/a4), [`A5`](/reference/library/dsp/units/a5)...
- **`Dsp::Delay::FractionalDelay`** (1 definitions): [`Line`](/reference/library/dsp/delay/fractionaldelay/line)
- **`Dsp::Dynamics::Compressor`** (1 definitions): [`Device`](/reference/library/dsp/dynamics/compressor/device)
- **`Dsp::Dynamics::EnvelopeFollower`** (1 definitions): [`Follower`](/reference/library/dsp/dynamics/envelopefollower/follower)
- **`Dsp::Dynamics::Limiter`** (1 definitions): [`Fast`](/reference/library/dsp/dynamics/limiter/fast)
- **`Dsp::Filters`** (9 definitions): [`AllPass`](/reference/library/dsp/filters/allpass), [`BandPass`](/reference/library/dsp/filters/bandpass), [`BiQuad`](/reference/library/dsp/filters/biquad), [`HighPass`](/reference/library/dsp/filters/highpass), [`LowPass`](/reference/library/dsp/filters/lowpass), [`Notch`](/reference/library/dsp/filters/notch)...
- **`Dsp::Filters::Cic`** (1 definitions): [`Decimator2`](/reference/library/dsp/filters/cic/decimator2)
- **`Dsp::Filters::Halfband`** (1 definitions): [`Fir7`](/reference/library/dsp/filters/halfband/fir7)
- **`Dsp::Generators`** (6 definitions): [`AD`](/reference/library/dsp/generators/ad), [`BandLimitedSaw`](/reference/library/dsp/generators/bandlimitedsaw), [`Impulse`](/reference/library/dsp/generators/impulse), [`Oscillator`](/reference/library/dsp/generators/oscillator), [`Sequencer`](/reference/library/dsp/generators/sequencer), [`TableOscillator`](/reference/library/dsp/generators/tableoscillator)
- **`Dsp::Nonlinear::Saturate`** (2 definitions): [`SoftClip`](/reference/library/dsp/nonlinear/saturate/softclip), [`Tanh`](/reference/library/dsp/nonlinear/saturate/tanh)
- **`Dsp::Spectral::Goertzel`** (1 definitions): [`Detector`](/reference/library/dsp/spectral/goertzel/detector)

#### Package Estimation

- **`Estimation::Kalman`** (1 definitions): [`Filter`](/reference/library/estimation/kalman/filter)
- **`Estimation::PeakDetector`** (1 definitions): [`Detector`](/reference/library/estimation/peakdetector/detector)

#### Package IO

- **`IO::Console`** (3 definitions): [`Log`](/reference/library/io/console/log), [`Print`](/reference/library/io/console/print), [`Println`](/reference/library/io/console/println)
- **`IO::Framing`** (5 definitions): [`CobsDelimiter`](/reference/library/io/framing/cobsdelimiter), [`SlipEnd`](/reference/library/io/framing/slipend), [`SlipEsc`](/reference/library/io/framing/slipesc), [`SlipEscEnd`](/reference/library/io/framing/slipescend), [`SlipEscEsc`](/reference/library/io/framing/slipescesc)
- **`IO::Midi`** (4 definitions): [`CcIn`](/reference/library/io/midi/ccin), [`CcOut`](/reference/library/io/midi/ccout), [`NoteIn`](/reference/library/io/midi/notein), [`NoteOut`](/reference/library/io/midi/noteout)
- **`IO::Osc`** (2 definitions): [`In`](/reference/library/io/osc/in), [`Out`](/reference/library/io/osc/out)
- **`IO::Serial`** (3 definitions): [`In`](/reference/library/io/serial/in), [`Out`](/reference/library/io/serial/out), [`Print`](/reference/library/io/serial/print)

#### Package LinAlg

- **`LinAlg::Matrices`** (3 definitions): [`MatMul`](/reference/library/linalg/matrices/matmul), [`Transform`](/reference/library/linalg/matrices/transform), [`Transpose`](/reference/library/linalg/matrices/transpose)
- **`LinAlg::Quaternion`** (3 definitions): [`Conjugate`](/reference/library/linalg/quaternion/conjugate), [`Multiply`](/reference/library/linalg/quaternion/multiply), [`Rotate`](/reference/library/linalg/quaternion/rotate)
- **`LinAlg::Vectors`** (5 definitions): [`Dot`](/reference/library/linalg/vectors/dot), [`Norm`](/reference/library/linalg/vectors/norm), [`Normalize`](/reference/library/linalg/vectors/normalize), [`Scale`](/reference/library/linalg/vectors/scale), [`Wedge`](/reference/library/linalg/vectors/wedge)

#### Package Math

- **`Math::Constants`** (3 definitions): [`E`](/reference/library/math/constants/e), [`Pi`](/reference/library/math/constants/pi), [`TwoPi`](/reference/library/math/constants/twopi)

#### Package Sensors

- **`Sensors::Conditioning`** (4 definitions): [`ComplementaryFilter`](/reference/library/sensors/conditioning/complementaryfilter), [`Deadband`](/reference/library/sensors/conditioning/deadband), [`Debounce`](/reference/library/sensors/conditioning/debounce), [`LinearCalibration`](/reference/library/sensors/conditioning/linearcalibration)

#### Package Status

- **`Status (Root)`** (6 definitions): [`Invalid`](/reference/library/status/invalid), [`Ok`](/reference/library/status/ok), [`OutOfRange`](/reference/library/status/outofrange), [`Platform`](/reference/library/status/platform), [`Truncated`](/reference/library/status/truncated), [`Unavailable`](/reference/library/status/unavailable)

#### Package Test

- **`Test::Assertions`** (1 definitions): [`AssertInRange`](/reference/library/test/assertions/assertinrange)

#### Package Window

- **`Window::Functions`** (4 definitions): [`Blackman`](/reference/library/window/functions/blackman), [`FlatTop`](/reference/library/window/functions/flattop), [`Hamming`](/reference/library/window/functions/hamming), [`Hann`](/reference/library/window/functions/hann)

