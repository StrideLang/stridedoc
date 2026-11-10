# Digital Signal Processing

This document outlines standard DSP design patterns and synthesis structures formulated in Stride.

---

## 1. Frequency Modulation (FM) Synthesis

In frequency modulation synthesis, the instantaneous frequency of a carrier oscillator is varied according to the output of a modulation oscillator:

$$\omega_c(t) = \omega_0 + I \cdot \sin(\omega_m t)$$

Where:
- $\omega_0$ represents the unmodulated carrier angular frequency.
- $\omega_m$ is the modulator angular frequency.
- $I$ denotes the modulation depth (index).

```stride
use DesktopAudio version 1.0;

import Dsp::Generators as Generators;

# Parameter definitions
signal CarrierFreq { default: 440.0 }
signal ModFreq     { default: 220.0 }
signal ModDepth    { default: 150.0 }

# Modulator computes instantaneous offset:
ModFreq 
  >> Generators::Oscillator() 
  >> Multiply(value: ModDepth)
  >> [_, CarrierFreq] >> Add()
  >> Generators::Oscillator(amplitude: 0.5)
  >> AudioOut;
```

---

## 2. Biquad Digital Filtering

The standard second-order infinite impulse response (IIR) biquad transfer function is expressed in the Z-domain as:

$$H(z) = \frac{b_0 + b_1 z^{-1} + b_2 z^{-2}}{a_0 + a_1 z^{-1} + a_2 z^{-2}}$$

The `Dsp::Filters::BiQuad` module implements this standard Direct Form topology:

```stride
use DesktopAudio version 1.0;

import Dsp::Generators as Generators;
import Dsp::Filters as Filters;

# Band-limited sawtooth passed into a resonant 12 dB/octave biquad filter:
110.0 
  >> Generators::BandLimitedSaw() 
  >> Filters::BiQuad(centerFrequency: 1800.0, resonance: 4.0) 
  >> AudioOut;
```

---

## 3. Parallel Processing & Channel Bundles

Multichannel signal paths and polyphonic voice banks are evaluated using bundle notation `[...]`:

```stride
use DesktopAudio version 1.0;

import Dsp::Generators as Generators;
import Dsp::Filters as Filters;

# Multi-frequency triad: Root (220 Hz), Major Third (277.18 Hz), Fifth (329.63 Hz)
[220.0, 277.18, 329.63]
  >> Generators::Oscillator(amplitude: 0.25)
  >> Sum()
  >> Filters::LowPass(frequency: 3000.0)
  >> AudioOut;
```
