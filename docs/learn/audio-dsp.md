# Audio DSP & Synthesis in Stride

A practical guide to designing digital signal processing chains, synthesizers, and sound effects in Stride.

---

## 1. Frequency Modulation (FM) Synthesis

FM synthesis creates rich, harmonically complex spectra by modulating the frequency of a carrier oscillator with the output of a modulator oscillator:

```stride
use DesktopAudio version 1.0;

import Stride;

# Define frequency parameters
signal CarrierFreq  { default: 440.0 }
signal ModFreq      { default: 220.0 }
signal ModDepth     { default: 150.0 }

# 1. Modulator generates wave at ModFreq
# 2. Scale by ModDepth
# 3. Add to CarrierFreq
# 4. Stream into Carrier Oscillator

ModFreq 
  >> Generators::Oscillator() 
  >> Math::Multiply(value: ModDepth)
  >> [_, CarrierFreq] >> Math::Add()
  >> Generators::Oscillator(amplitude: 0.5)
  >> AudioOut;
```

---

## 2. Resonant Filter Sweeps (Subtractive Synthesis)

In subtractive synthesis, a harmonically rich waveform (such as a sawtooth wave) is carved away by time-varying resonant filters:

```stride
use DesktopAudio version 1.0;

import Stride;

# Envelope parameters for filter sweep
signal CutoffStart { default: 300.0 }
signal CutoffEnd   { default: 4500.0 }

# Band-limited sawtooth passed into a resonant 12dB/octave BiQuad filter
110.0 >> Generators::BandLimitedSaw() >> Filters::BiQuad(
    centerFrequency: 1800.0,
    resonance: 4.0
) >> AudioOut;
```

---

## 3. Polyphony & Voice Bundles

Stride's bundle syntax `[...]` enables concise expression of polyphonic voice architectures:

```stride
use DesktopAudio version 1.0;

import Stride;

# Three-note chord: Root (220 Hz), Major Third (277.18 Hz), Fifth (329.63 Hz)
[220.0, 277.18, 329.63]
  >> Generators::Oscillator(amplitude: 0.25)
  >> Math::Sum()
  >> Filters::LowPass(cutoff: 3000.0)
  >> AudioOut;
```
