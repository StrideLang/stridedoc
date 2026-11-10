---
title: Standard Library Reference
description: Specification of modules, stream processors, filters, generators, and arithmetic operations in the Stride standard library.
---

# Standard Library Reference

The Stride standard library provides verified primitives for signal flow, multi-rate digital signal processing (DSP), mathematical operations, and state machine transitions.

## Source Repository & Versioning

- **Upstream Repository**: [`StrideLang/strideroot`](https://github.com/StrideLang/strideroot)

- **Active Ref**: `main` (unambiguous source line links are embedded in each definition)

## Namespace Architecture

The Stride standard library establishes a unified hierarchy under the `Stride` namespace:

### 1. Stride (Root Namespace)

Definitions residing in the root library files belong directly to `package Stride`. They are imported automatically or via `import Stride;` and are called directly in global scope (e.g. `Sin()`, `Sum()`, `Equal()`). In documentation and navigation, they are organized into file-based groups for clarity:

- **Assertions (Group)** (10 definitions): [`ExpectEqual`](/reference/library/assertions/expectequal), [`ExpectFalse`](/reference/library/assertions/expectfalse), [`ExpectGe`](/reference/library/assertions/expectge), [`ExpectGt`](/reference/library/assertions/expectgt), [`ExpectLe`](/reference/library/assertions/expectle), [`ExpectLt`](/reference/library/assertions/expectlt)...
- **BasicOperations (Group)** (3 definitions): [`Average`](/reference/library/basicoperations/average), [`Clip`](/reference/library/basicoperations/clip), [`Sum`](/reference/library/basicoperations/sum)
- **Comparisons (Group)** (8 definitions): [`AllOff`](/reference/library/comparisons/alloff), [`AllOn`](/reference/library/comparisons/allon), [`Equal`](/reference/library/comparisons/equal), [`Greater`](/reference/library/comparisons/greater), [`GreaterOrEqual`](/reference/library/comparisons/greaterorequal), [`Less`](/reference/library/comparisons/less)...
- **Control (Group)** (5 definitions): [`FallingEdge`](/reference/library/control/fallingedge), [`Latch`](/reference/library/control/latch), [`OnChange`](/reference/library/control/onchange), [`RisingEdge`](/reference/library/control/risingedge), [`Smooth`](/reference/library/control/smooth)
- **Counter (Group)** (1 definitions): [`Counter`](/reference/library/counter/counter)
- **Debug (Group)** (4 definitions): [`DebugPrint`](/reference/library/debug/debugprint), [`Error`](/reference/library/debug/error), [`Probe`](/reference/library/debug/probe), [`Watch`](/reference/library/debug/watch)
- **Domain (Group)** (1 definitions): [`Exit`](/reference/library/domain/exit)
- **Level (Group)** (1 definitions): [`Level`](/reference/library/level/level)
- **Logic (Group)** (7 definitions): [`And`](/reference/library/logic/and), [`Nand`](/reference/library/logic/nand), [`Nor`](/reference/library/logic/nor), [`Not`](/reference/library/logic/not), [`Or`](/reference/library/logic/or), [`Select`](/reference/library/logic/select)...
- **Math (Group)** (21 definitions): [`Abs`](/reference/library/math/abs), [`C1`](/reference/library/math/c1), [`C2`](/reference/library/math/c2), [`C3`](/reference/library/math/c3), [`C4`](/reference/library/math/c4), [`Clamp`](/reference/library/math/clamp)...
- **MathConstants (Group)** (3 definitions): [`E`](/reference/library/mathconstants/e), [`Pi`](/reference/library/mathconstants/pi), [`TwoPi`](/reference/library/mathconstants/twopi)
- **Pan (Group)** (1 definitions): [`Pan`](/reference/library/pan/pan)
- **QualityPolicy (Group)** (4 definitions): [`Accurate`](/reference/library/qualitypolicy/accurate), [`Compact`](/reference/library/qualitypolicy/compact), [`Fast`](/reference/library/qualitypolicy/fast), [`Optimal`](/reference/library/qualitypolicy/optimal)

### 2. Stride Sub-packages

Components residing in library subdirectories form hierarchical sub-namespaces (`Stride::<Package>`). When imported via `import Stride;`, they are accessed via category qualification (e.g. `Generators::Oscillator`, `Filters::BiQuad`), or imported directly via `import Stride::Generators;`:

- **`Stride::Filters`** (5 definitions): [`BandPass`](/reference/library/filters/bandpass), [`BiQuad`](/reference/library/filters/biquad), [`LowPass`](/reference/library/filters/lowpass), [`Mix`](/reference/library/filters/mix), [`Rectify`](/reference/library/filters/rectify)
- **`Stride::Generators`** (6 definitions): [`AD`](/reference/library/generators/ad), [`BandLimitedSaw`](/reference/library/generators/bandlimitedsaw), [`Impulse`](/reference/library/generators/impulse), [`Oscillator`](/reference/library/generators/oscillator), [`Sequencer`](/reference/library/generators/sequencer), [`TableOscillator`](/reference/library/generators/tableoscillator)
- **`Stride::Notes`** (4 definitions): [`C4`](/reference/library/notes/c4), [`C5`](/reference/library/notes/c5), [`E4`](/reference/library/notes/e4), [`G4`](/reference/library/notes/g4)
- **`Stride::Osc`** (2 definitions): [`OSCIn`](/reference/library/osc/oscin), [`OSCOut`](/reference/library/osc/oscout)
- **`Stride::Serial`** (1 definitions): [`SerialPrint`](/reference/library/serial/serialprint)

