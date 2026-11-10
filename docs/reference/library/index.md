---
title: Standard Library Reference
description: Specification of modules, stream processors, filters, generators, and arithmetic operations in the Stride standard library.
---

# Standard Library Reference

The Stride standard library provides the foundational primitives for signal routing, multi-rate audio digital signal processing (DSP), mathematical operations, and state machine transitions.

## Namespace Organization

- **`package Stride` (Core Library)**: Primitives located in the root of the standard library (`Math`, `Logic`, `BasicOperations`, `Comparisons`, etc.) belong to the root `Stride` package. They are imported automatically or via `import Stride`, and are available directly in global scope (e.g. `Sin()`, `Sum()`, `Abs()`).
- **Sub-packages (`Stride::<Category>`)**: Components residing in subdirectories (`Generators`, `Filters`, `Serial`, `Osc`) form categorized sub-packages. When using `import Stride`, they are referenced via category qualification (e.g. `Generators::Oscillator`, `Filters::BiQuad`), or directly via category import (`import Stride::Generators`).

## Package Modules

### Stride (Core Library) (102 definitions)

[`Abs`](/reference/library/core/abs), [`Accurate`](/reference/library/core/accurate), [`Compact`](/reference/library/core/compact), [`Counter`](/reference/library/core/counter), [`DebugPrint`](/reference/library/core/debugprint), [`Error`](/reference/library/core/error), [`Exit`](/reference/library/core/exit), [`ExpectEqual`](/reference/library/core/expectequal)...


### Stride::Filters (5 definitions)

[`BandPass`](/reference/library/filters/bandpass), [`BiQuad`](/reference/library/filters/biquad), [`LowPass`](/reference/library/filters/lowpass), [`Mix`](/reference/library/filters/mix), [`Rectify`](/reference/library/filters/rectify)


### Stride::Generators (5 definitions)

[`AD`](/reference/library/generators/ad), [`BandLimitedSaw`](/reference/library/generators/bandlimitedsaw), [`Oscillator`](/reference/library/generators/oscillator), [`Sequencer`](/reference/library/generators/sequencer), [`TableOscillator`](/reference/library/generators/tableoscillator)


### Stride::Notes (4 definitions)

[`C4`](/reference/library/notes/c4), [`C5`](/reference/library/notes/c5), [`E4`](/reference/library/notes/e4), [`G4`](/reference/library/notes/g4)


### Stride::Osc (1 definitions)

[`OSCOut`](/reference/library/osc/oscout)


### Stride::Serial (1 definitions)

[`SerialPrint`](/reference/library/serial/serialprint)

