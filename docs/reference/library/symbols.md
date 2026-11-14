---
title: Standard Library Symbol Index (A–Z)
description: Complete alphabetical index of all modules, stream processors, reactions, and constants in the Stride standard library.
---

# Standard Library Symbol Index

Complete alphabetical directory of all **201 definitions** in the Stride standard library.

<div class="symbol-alpha-bar">[A](#a) &bull; [B](#b) &bull; [C](#c) &bull; [D](#d) &bull; [E](#e) &bull; [F](#f) &bull; [G](#g) &bull; [H](#h) &bull; [I](#i) &bull; [L](#l) &bull; [M](#m) &bull; [N](#n) &bull; [O](#o) &bull; [P](#p) &bull; [R](#r) &bull; [S](#s) &bull; [T](#t) &bull; [U](#u) &bull; [W](#w) &bull; [X](#x)</div>

## A

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`A0`](/reference/library/dsp/units/a0) | `Dsp::Units` | Constant | Note A0 frequency in Hz |
| [`A1`](/reference/library/dsp/units/a1) | `Dsp::Units` | Constant | Note A1 frequency in Hz |
| [`A2`](/reference/library/dsp/units/a2) | `Dsp::Units` | Constant | Note A2 frequency in Hz |
| [`A3`](/reference/library/dsp/units/a3) | `Dsp::Units` | Constant | Note A3 frequency in Hz |
| [`A4`](/reference/library/dsp/units/a4) | `Dsp::Units` | Constant | Concert Pitch A4 frequency in Hz |
| [`A5`](/reference/library/dsp/units/a5) | `Dsp::Units` | Constant | Note A5 frequency in Hz |
| [`A6`](/reference/library/dsp/units/a6) | `Dsp::Units` | Constant | Note A6 frequency in Hz |
| [`Abs`](/reference/library/math/abs) | *(Global Prelude)* | Module | Returns the absolute value of the input signal. |
| [`Accurate`](/reference/library/qualitypolicy/accurate) | *(Global Prelude)* | Constant | Prioritizes numerical precision and exact behavior over speed |
| [`AD`](/reference/library/dsp/generators/ad) | `Dsp::Generators` | Module | Attack-Decay envelope generator. |
| [`AllOff`](/reference/library/comparisons/alloff) | *(Global Prelude)* | Loop | Outputs on if all switches in the input array are off: Input >> AllOff() >> Output. |
| [`AllOn`](/reference/library/comparisons/allon) | *(Global Prelude)* | Loop | Outputs on if all switches in the input array are on: Input >> AllOn() >> Output. |
| [`AllPass`](/reference/library/dsp/filters/allpass) | `Dsp::Filters` | Module | Second-order all-pass filter: Input >> AllPass(frequency: 1000.0) >> Output. A BiQuad with FilterDesign::ModeAllPass. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point. |
| [`And`](/reference/library/logic/and) | *(Global Prelude)* | Module | Logical AND operation on switch inputs: [A, B] >> And() >> Out. |
| [`AssertInRange`](/reference/library/test/assertions/assertinrange) | `Test::Assertions` | Module | Inline runtime assertion verifying signal remains within bounds: AudioIn >> AssertInRange(min: -1.0 max: 1.0) >> CleanAudio. |
| [`Average`](/reference/library/basicoperations/average) | *(Global Prelude)* | Module | Computes the arithmetic mean of all signals in the input array: Input >> Average() >> Output. |

## B

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`B0`](/reference/library/dsp/units/b0) | `Dsp::Units` | Constant | Note B0 frequency in Hz |
| [`B1`](/reference/library/dsp/units/b1) | `Dsp::Units` | Constant | Note B1 frequency in Hz |
| [`B2`](/reference/library/dsp/units/b2) | `Dsp::Units` | Constant | Note B2 frequency in Hz |
| [`B3`](/reference/library/dsp/units/b3) | `Dsp::Units` | Constant | Note B3 frequency in Hz |
| [`B4`](/reference/library/dsp/units/b4) | `Dsp::Units` | Constant | Note B4 frequency in Hz |
| [`B5`](/reference/library/dsp/units/b5) | `Dsp::Units` | Constant | Note B5 frequency in Hz |
| [`B6`](/reference/library/dsp/units/b6) | `Dsp::Units` | Constant | Note B6 frequency in Hz |
| [`BandLimitedSaw`](/reference/library/dsp/generators/bandlimitedsaw) | `Dsp::Generators` | Module | Band-limited sawtooth generator (differentiated parabolic wave, DPW): Saw(frequency: 220.0) >> Out. Output in [-1, 1). The frequency is in Hz and is converted against the rate of the output. |
| [`BandPass`](/reference/library/dsp/filters/bandpass) | `Dsp::Filters` | Module | Second-order band-pass filter: Input >> BandPass(frequency: 1000.0 q: 2.0) >> Output. A BiQuad with FilterDesign::ModeBandPass. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point. |
| [`BiQuad`](/reference/library/dsp/filters/biquad) | `Dsp::Filters` | Module | Second-order IIR filter with a selectable response (RBJ Audio EQ Cookbook): Input >> BiQuad(mode: FilterDesign::ModeLowPass frequency: 800.0 q: 0.7071) >> Output. LowPass, HighPass, BandPass, Notch, AllPass and PeakingEq are shortcuts for the common modes. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point. |
| [`Blackman`](/reference/library/window/functions/blackman) | `Window::Functions` | Module | Blackman window function: Index >> Blackman(size: 512) >> Weight. |

## C

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`C0`](/reference/library/dsp/units/c0) | `Dsp::Units` | Constant | Note C0 frequency in Hz |
| [`C1`](/reference/library/dsp/units/c1) | `Dsp::Units` | Constant | Note C1 frequency in Hz |
| [`C2`](/reference/library/dsp/units/c2) | `Dsp::Units` | Constant | Note C2 frequency in Hz |
| [`C3`](/reference/library/dsp/units/c3) | `Dsp::Units` | Constant | Note C3 frequency in Hz |
| [`C4`](/reference/library/dsp/units/c4) | `Dsp::Units` | Constant | Note C4 (Middle C) frequency in Hz |
| [`C5`](/reference/library/dsp/units/c5) | `Dsp::Units` | Constant | Note C5 frequency in Hz |
| [`C6`](/reference/library/dsp/units/c6) | `Dsp::Units` | Constant | Note C6 frequency in Hz |
| [`CcIn`](/reference/library/io/midi/ccin) | `IO::Midi` | Module | Receives MIDI Continuous Controller (CC) messages. |
| [`CcOut`](/reference/library/io/midi/ccout) | `IO::Midi` | Module | Transmits MIDI Continuous Controller (CC) messages. |
| [`Clamp`](/reference/library/math/clamp) | *(Global Prelude)* | Module | Constrains input signal between minimum and maximum bounds: Input >> Clamp(min: 0.0 max: 1.0) >> Output. |
| [`Clarke`](/reference/library/control/foc/clarke) | `Control` | Module | Clarke transform: 3-phase currents [Ia, Ib, Ic] >> Clarke() >> [Ialpha, Ibeta]. |
| [`Clip`](/reference/library/basicoperations/clip) | *(Global Prelude)* | Module | Limits signal within minimum and maximum values: Input >> Clip(minimum: 0.0 maximum: 1.0) >> Output. |
| [`CobsDelimiter`](/reference/library/io/framing/cobsdelimiter) | `IO::Framing` | Constant | COBS packet zero delimiter |
| [`Coefficients`](/reference/library/dsp/filterdesign/coefficients) | `Dsp::FilterDesign` | Module | RBJ Audio EQ Cookbook biquad design: Frequency >> FilterDesign::Coefficients(mode: FilterDesign::ModeLowPass q: 0.7071) >> Coeffs. The sample rate is the rate of the output; Coeffs is [b0, b1, b2, a1, a2] normalised by a0. |
| [`Compact`](/reference/library/qualitypolicy/compact) | *(Global Prelude)* | Constant | Prioritizes minimal Flash/RAM memory footprint (e.g. avoids tables, uses ROM) |
| [`ComplementaryFilter`](/reference/library/sensors/conditioning/complementaryfilter) | `Sensors::Conditioning` | Module | IMU sensor fusion blending gyro rate and accelerometer tilt: GyroRate >> ComplementaryFilter(accelAngle: AccelTilt timeConstant: 0.5) >> FusedAngle. The sample interval and the blend factor are derived from the rate of the output; the type must be floating point. |
| [`Conjugate`](/reference/library/linalg/quaternion/conjugate) | `LinAlg::Quaternion` | Module | Quaternion conjugate: Q >> Conjugate() >> QConjugate. |
| [`Cos`](/reference/library/math/cos) | *(Global Prelude)* | Module | Cosine function of angle in radians. |
| [`Counter`](/reference/library/counter/counter) | *(Global Prelude)* | Module | A discrete step counter that increments per tick and rolls over to startValue upon exceeding stopValue. |
| [`Crossfade`](/reference/library/dsp/routing/crossfade) | `Dsp::Routing` | Module | Linear crossfade between two audio streams. |

## D

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`D0`](/reference/library/dsp/units/d0) | `Dsp::Units` | Constant | Note D0 frequency in Hz |
| [`D1`](/reference/library/dsp/units/d1) | `Dsp::Units` | Constant | Note D1 frequency in Hz |
| [`D2`](/reference/library/dsp/units/d2) | `Dsp::Units` | Constant | Note D2 frequency in Hz |
| [`D3`](/reference/library/dsp/units/d3) | `Dsp::Units` | Constant | Note D3 frequency in Hz |
| [`D4`](/reference/library/dsp/units/d4) | `Dsp::Units` | Constant | Note D4 frequency in Hz |
| [`D5`](/reference/library/dsp/units/d5) | `Dsp::Units` | Constant | Note D5 frequency in Hz |
| [`D6`](/reference/library/dsp/units/d6) | `Dsp::Units` | Constant | Note D6 frequency in Hz |
| [`DbToLinear`](/reference/library/dsp/units/dbtolinear) | `Dsp::Units` | Module | Converts decibels (dB) to linear amplitude ratio. |
| [`Deadband`](/reference/library/sensors/conditioning/deadband) | `Sensors::Conditioning` | Module | Suppresses near-zero sensor jitter with smooth linear rescaling: Joystick >> Deadband(threshold: 0.05) >> Output. |
| [`Debounce`](/reference/library/sensors/conditioning/debounce) | `Sensors::Conditioning` | Module | Suppresses mechanical switch bounce: RawButton >> Debounce(time: 0.01) >> CleanButton. The output follows the input once it has been different for the given time in seconds, converted against the rate of the output. |
| [`DebugPrint`](/reference/library/debug/debugprint) | *(Global Prelude)* | Module | — |
| [`Decimator2`](/reference/library/dsp/filters/cic/decimator2) | `Dsp::Filters::Cic` | Module | 2nd-order multiplierless Cascaded Integrator-Comb (CIC) filter: HighRateIn >> Cic::Decimator2() >> Out. |
| [`Detector`](/reference/library/dsp/spectral/goertzel/detector) | `Dsp::Spectral::Goertzel` | Module | Goertzel single-frequency power detector: AudioIn >> Goertzel::Detector(frequency: 440.0) >> TonePower. The frequency is in Hz and is converted against the rate of the output (the sample rate). Type must be floating point. |
| [`Detector`](/reference/library/estimation/peakdetector/detector) | `Estimation::PeakDetector` | Module | Real-time local maximum detector with a switch output: Input >> PeakDetector::Detector(threshold: 0.5) >> Peak. |
| [`Device`](/reference/library/dsp/dynamics/compressor/device) | `Dsp::Dynamics::Compressor` | Module | Feedforward dynamic range compressor: AudioIn >> Compressor::Device(threshold: 0.5 ratio: 4.0 makeup: 1.2 attack: 0.01 release: 0.1) >> Out. Attack and release are times in seconds, converted against the rate of the output. |
| [`Divide`](/reference/library/math/divide) | *(Global Prelude)* | Module | Divides Input[0] by Input[1]. |
| [`Dot`](/reference/library/linalg/vectors/dot) | `LinAlg::Vectors` | Loop | Dot product of two vectors of any dimension: VecA >> Dot(with: VecB) >> Result. The dimension is the size of the input. |

## E

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`E`](/reference/library/math/constants/e) | `Math::Constants` | Constant | Euler's number (base of natural logarithm) |
| [`E0`](/reference/library/dsp/units/e0) | `Dsp::Units` | Constant | Note E0 frequency in Hz |
| [`E1`](/reference/library/dsp/units/e1) | `Dsp::Units` | Constant | Note E1 frequency in Hz |
| [`E2`](/reference/library/dsp/units/e2) | `Dsp::Units` | Constant | Note E2 frequency in Hz |
| [`E3`](/reference/library/dsp/units/e3) | `Dsp::Units` | Constant | Note E3 frequency in Hz |
| [`E4`](/reference/library/dsp/units/e4) | `Dsp::Units` | Constant | Note E4 frequency in Hz |
| [`E5`](/reference/library/dsp/units/e5) | `Dsp::Units` | Constant | Note E5 frequency in Hz |
| [`E6`](/reference/library/dsp/units/e6) | `Dsp::Units` | Constant | Note E6 frequency in Hz |
| [`Equal`](/reference/library/comparisons/equal) | *(Global Prelude)* | Module | Compares two input values: outputs on if Input[0] == Input[1], else off. |
| [`Error`](/reference/library/debug/error) | *(Global Prelude)* | Module | — |
| [`Exit`](/reference/library/domain/exit) | *(Global Prelude)* | Module | When input is true, the current domain terminates without executing any further. |
| [`Exp`](/reference/library/math/exp) | *(Global Prelude)* | Module | Computes the natural exponential: exp(Input). |
| [`ExpectEqual`](/reference/library/assertions/expectequal) | *(Global Prelude)* | Module | Equality assertion module. Declared for schema validation; handled with special treatment in the testing framework. |
| [`ExpectFalse`](/reference/library/assertions/expectfalse) | *(Global Prelude)* | Module | Condition assertion (false). Declared for schema validation; handled with special treatment in the testing framework. |
| [`ExpectGe`](/reference/library/assertions/expectge) | *(Global Prelude)* | Module | Greater-than-or-equal assertion module (Actual >= Expected). Declared for schema validation; handled with special treatment in the testing framework. |
| [`ExpectGt`](/reference/library/assertions/expectgt) | *(Global Prelude)* | Module | Greater-than assertion module (Actual > Expected). Declared for schema validation; handled with special treatment in the testing framework. |
| [`ExpectLe`](/reference/library/assertions/expectle) | *(Global Prelude)* | Module | Less-than-or-equal assertion module (Actual <= Expected). Declared for schema validation; handled with special treatment in the testing framework. |
| [`ExpectLt`](/reference/library/assertions/expectlt) | *(Global Prelude)* | Module | Less-than-or-equal assertion module (Actual < Expected). Declared for schema validation; handled with special treatment in the testing framework. |
| [`ExpectMaxError`](/reference/library/assertions/expectmaxerror) | *(Global Prelude)* | Module | Statistical maximum absolute error assertion for stream differential testing. |
| [`ExpectNear`](/reference/library/assertions/expectnear) | *(Global Prelude)* | Module | Approximate equality assertion within epsilon tolerance. Declared for schema validation; handled with special treatment in the testing framework. |
| [`ExpectSnr`](/reference/library/assertions/expectsnr) | *(Global Prelude)* | Module | Statistical Signal-to-Noise Ratio assertion for stream differential testing. |
| [`ExpectTrue`](/reference/library/assertions/expecttrue) | *(Global Prelude)* | Module | Condition assertion (true). Declared for schema validation; handled with special treatment in the testing framework. |

## F

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`F0`](/reference/library/dsp/units/f0) | `Dsp::Units` | Constant | Note F0 frequency in Hz |
| [`F1`](/reference/library/dsp/units/f1) | `Dsp::Units` | Constant | Note F1 frequency in Hz |
| [`F2`](/reference/library/dsp/units/f2) | `Dsp::Units` | Constant | Note F2 frequency in Hz |
| [`F3`](/reference/library/dsp/units/f3) | `Dsp::Units` | Constant | Note F3 frequency in Hz |
| [`F4`](/reference/library/dsp/units/f4) | `Dsp::Units` | Constant | Note F4 frequency in Hz |
| [`F5`](/reference/library/dsp/units/f5) | `Dsp::Units` | Constant | Note F5 frequency in Hz |
| [`F6`](/reference/library/dsp/units/f6) | `Dsp::Units` | Constant | Note F6 frequency in Hz |
| [`FallingEdge`](/reference/library/control/fallingedge) | *(Global Prelude)* | Module | Detects falling edge (on -> off): Input >> FallingEdge() >> Trigger. |
| [`Fast`](/reference/library/qualitypolicy/fast) | *(Global Prelude)* | Constant | Prioritizes execution speed and low cycle count over algorithmic precision |
| [`Fast`](/reference/library/dsp/dynamics/limiter/fast) | `Dsp::Dynamics::Limiter` | Module | Hard peak clamping limiter: AudioIn >> Limiter::Fast(threshold: 0.95) >> Out. |
| [`Filter`](/reference/library/estimation/kalman/filter) | `Estimation::Kalman` | Module | 1D recursive Kalman filter: NoisySignal >> Kalman::Filter(q: 0.01 r: 0.1) >> FilteredSignal. q is a variance per second and is converted against the rate of the output, so the filter behaves the same at any sample rate. Type must be floating point. |
| [`Fir7`](/reference/library/dsp/filters/halfband/fir7) | `Dsp::Filters::Halfband` | Module | Efficient 7-tap halfband FIR filter with 50% zero-tap reduction: AudioIn >> Halfband::Fir7() >> Out. |
| [`FlatTop`](/reference/library/window/functions/flattop) | `Window::Functions` | Module | Flat-top measurement window function: Index >> FlatTop(size: 512) >> Weight. |
| [`Floor`](/reference/library/math/floor) | *(Global Prelude)* | Module | Returns input value rounded down to the nearest integer. |
| [`Follower`](/reference/library/dsp/dynamics/envelopefollower/follower) | `Dsp::Dynamics::EnvelopeFollower` | Module | Peak envelope follower with attack and release times in seconds: AudioIn >> EnvelopeFollower::Follower(attack: 0.01 release: 0.1) >> Envelope. Times are converted against the rate of the output, so the behaviour does not depend on the sample rate. |

## G

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`G0`](/reference/library/dsp/units/g0) | `Dsp::Units` | Constant | Note G0 frequency in Hz |
| [`G1`](/reference/library/dsp/units/g1) | `Dsp::Units` | Constant | Note G1 frequency in Hz |
| [`G2`](/reference/library/dsp/units/g2) | `Dsp::Units` | Constant | Note G2 frequency in Hz |
| [`G3`](/reference/library/dsp/units/g3) | `Dsp::Units` | Constant | Note G3 frequency in Hz |
| [`G4`](/reference/library/dsp/units/g4) | `Dsp::Units` | Constant | Note G4 frequency in Hz |
| [`G5`](/reference/library/dsp/units/g5) | `Dsp::Units` | Constant | Note G5 frequency in Hz |
| [`G6`](/reference/library/dsp/units/g6) | `Dsp::Units` | Constant | Note G6 frequency in Hz |
| [`Greater`](/reference/library/comparisons/greater) | *(Global Prelude)* | Module | Compares two input values: outputs on if Input[0] > Input[1], else off. |
| [`GreaterOrEqual`](/reference/library/comparisons/greaterorequal) | *(Global Prelude)* | Module | Compares two input values: outputs on if Input[0] >= Input[1], else off. |

## H

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Hamming`](/reference/library/window/functions/hamming) | `Window::Functions` | Module | Hamming window function: Index >> Hamming(size: 512) >> Weight. |
| [`Hann`](/reference/library/window/functions/hann) | `Window::Functions` | Module | Hann window function: Index >> Hann(size: 512) >> Weight. |
| [`HighPass`](/reference/library/dsp/filters/highpass) | `Dsp::Filters` | Module | Second-order high-pass filter: Input >> HighPass(frequency: 80.0 q: 0.7071) >> Output. A BiQuad with FilterDesign::ModeHighPass. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point. |
| [`Hysteresis`](/reference/library/control/hysteresis/hysteresis) | `Control` | Module | Dual-threshold hysteresis comparator (Schmitt trigger) with a switch output: Input >> Hysteresis(low: 0.2 high: 0.8) >> Output. The output keeps its state while the input is between the two thresholds. |

## I

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Impulse`](/reference/library/dsp/generators/impulse) | `Dsp::Generators` | Module | Impulse train generator. |
| [`In`](/reference/library/io/osc/in) | `IO::Osc` | Module | Receives OSC messages from a UDP network port. |
| [`In`](/reference/library/io/serial/in) | `IO::Serial` | Module | Reads signal values from platform serial input stream. |
| [`Invalid`](/reference/library/status/invalid) | `Status` | Constant | The input cannot be used: text with no number in it, a bad template |
| [`InverseClarke`](/reference/library/control/foc/inverseclarke) | `Control` | Module | Inverse Clarke transform: [Valpha, Vbeta] >> InverseClarke() >> [Va, Vb, Vc]. |
| [`InversePark`](/reference/library/control/foc/inversepark) | `Control` | Module | Inverse Park transform: [Vd, Vq] >> InversePark(angle: Theta) >> [Valpha, Vbeta]. |

## L

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Latch`](/reference/library/control/latch) | *(Global Prelude)* | Module | Sample and hold: samples Input when trigger is on and holds the value when off: Input >> Latch(trigger: Gate) >> Output. |
| [`Lerp`](/reference/library/math/lerp) | *(Global Prelude)* | Module | Linearly interpolates from Input to Target based on factor: Input >> Lerp(target: Target factor: 0.5) >> Output. |
| [`Less`](/reference/library/comparisons/less) | *(Global Prelude)* | Module | Compares two input values: outputs on if Input[0] < Input[1], else off. |
| [`LessOrEqual`](/reference/library/comparisons/lessorequal) | *(Global Prelude)* | Module | Compares two input values: outputs on if Input[0] <= Input[1], else off. |
| [`Level`](/reference/library/dsp/routing/level) | `Dsp::Routing` | Module | Scales the input signal and applies an offset to it. |
| [`Line`](/reference/library/dsp/delay/fractionaldelay/line) | `Dsp::Delay::FractionalDelay` | Module | Ring-buffer fractional delay line with linear interpolation: AudioIn >> FractionalDelay::Line(delay: 0.0025) >> DelayedOut. The delay is in seconds, converted against the rate of the output, up to 4096 samples (4096 / rate seconds). |
| [`LinearCalibration`](/reference/library/sensors/conditioning/linearcalibration) | `Sensors::Conditioning` | Module | Rescales raw ADC readings to engineering units: Adc >> LinearCalibration(rawMin: 0 rawMax: 4095 calMin: 0.0 calMax: 3.3) >> Volts. |
| [`Log`](/reference/library/io/console/log) | `IO::Console` | Module | Logs structured timestamped telemetry messages. |
| [`LowPass`](/reference/library/dsp/filters/lowpass) | `Dsp::Filters` | Module | Second-order low-pass filter: Input >> LowPass(frequency: 800.0 q: 0.7071) >> Output. A BiQuad with FilterDesign::ModeLowPass. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point. |

## M

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Map`](/reference/library/math/map) | *(Global Prelude)* | Module | Linearly maps Input from [inMin, inMax] to [outMin, outMax]: Input >> Map(inMin: 0.0 inMax: 1.0 outMin: 100.0 outMax: 1000.0) >> Output. |
| [`MatMul`](/reference/library/linalg/matrices/matmul) | `LinAlg::Matrices` | Loop | Matrix product of any compatible shapes: MatA >> MatMul(with: MatB inner: 3 columns: 2) >> Result. All matrices are row-major. The number of rows of A comes from the size of the result. |
| [`Max`](/reference/library/math/max) | *(Global Prelude)* | Module | Returns the maximum of two input values in a list: [A, B] >> Max() >> Out. |
| [`MidiToFreq`](/reference/library/dsp/units/miditofreq) | `Dsp::Units` | Module | Converts MIDI note number to frequency in Hertz. |
| [`Min`](/reference/library/math/min) | *(Global Prelude)* | Module | Returns the minimum of two input values in a list: [A, B] >> Min() >> Out. |
| [`ModeAllPass`](/reference/library/dsp/filterdesign/modeallpass) | `Dsp::FilterDesign` | Constant | All-pass: unity magnitude at all frequencies, phase shift of 180 degrees at `frequency` |
| [`ModeBandPass`](/reference/library/dsp/filterdesign/modebandpass) | `Dsp::FilterDesign` | Constant | Second order band-pass with constant 0 dB peak gain at `frequency`; `q` sets the narrowness |
| [`ModeHighPass`](/reference/library/dsp/filterdesign/modehighpass) | `Dsp::FilterDesign` | Constant | Second order high-pass: passes frequencies above `frequency`, -12 dB/octave below |
| [`ModeLowPass`](/reference/library/dsp/filterdesign/modelowpass) | `Dsp::FilterDesign` | Constant | Second order low-pass: passes frequencies below `frequency`, -12 dB/octave above |
| [`ModeNotch`](/reference/library/dsp/filterdesign/modenotch) | `Dsp::FilterDesign` | Constant | Notch (band-reject): removes a narrow band around `frequency` |
| [`ModePeak`](/reference/library/dsp/filterdesign/modepeak) | `Dsp::FilterDesign` | Constant | Peaking equaliser: boosts or cuts a band around `frequency` by `gain` dB |
| [`Multiply`](/reference/library/math/multiply) | *(Global Prelude)* | Module | Multiplies Input[0] by Input[1]. |
| [`Multiply`](/reference/library/linalg/quaternion/multiply) | `LinAlg::Quaternion` | Module | Quaternion Hamilton product: Q1 >> Multiply(with: Q2) >> QProduct. |

## N

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Nand`](/reference/library/logic/nand) | *(Global Prelude)* | Module | Logical NAND operation on switch inputs: [A, B] >> Nand() >> Out. |
| [`Negate`](/reference/library/math/negate) | *(Global Prelude)* | Module | Negates (changes the sign of) an input value: -Input. Input >> Negate() >> Output. (For the multiplicative inverse use 1.0 / Input.) |
| [`Nor`](/reference/library/logic/nor) | *(Global Prelude)* | Module | Logical NOR operation on switch inputs: [A, B] >> Nor() >> Out. |
| [`Norm`](/reference/library/linalg/vectors/norm) | `LinAlg::Vectors` | Module | Euclidean norm of a vector of any dimension: Vec >> Norm() >> Length. This is also the norm of a quaternion. |
| [`Normalize`](/reference/library/linalg/vectors/normalize) | `LinAlg::Vectors` | Module | Normalizes a vector of any dimension to unit length: Vec >> Normalize() >> UnitVec. |
| [`Not`](/reference/library/logic/not) | *(Global Prelude)* | Module | Logical NOT operation: inverts a switch input. |
| [`Notch`](/reference/library/dsp/filters/notch) | `Dsp::Filters` | Module | Second-order notch filter: Input >> Notch(frequency: 50.0 q: 10.0) >> Output (e.g. mains hum removal). A BiQuad with FilterDesign::ModeNotch. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point. |
| [`NoteIn`](/reference/library/io/midi/notein) | `IO::Midi` | Module | Receives MIDI note on/off events. |
| [`NoteOut`](/reference/library/io/midi/noteout) | `IO::Midi` | Module | Sends MIDI note on events. |
| [`NotEqual`](/reference/library/comparisons/notequal) | *(Global Prelude)* | Module | Compares two input values: outputs on if Input[0] != Input[1], else off. |

## O

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Ok`](/reference/library/status/ok) | `Status` | Constant | Done as asked |
| [`OnChange`](/reference/library/control/onchange) | *(Global Prelude)* | Module | Detects changes in a signal: outputs on when Input differs from previous tick: Input >> OnChange() >> Trigger. |
| [`Optimal`](/reference/library/qualitypolicy/optimal) | *(Global Prelude)* | Constant | Platform optimal: selects hardware accelerators or best platform implementation |
| [`Or`](/reference/library/logic/or) | *(Global Prelude)* | Module | Logical OR operation on switch inputs: [A, B] >> Or() >> Out. |
| [`Oscillator`](/reference/library/dsp/generators/oscillator) | `Dsp::Generators` | Module | Bipolar output [-1.0, 1.0] scaled by amplitude. |
| [`Out`](/reference/library/io/osc/out) | `IO::Osc` | Module | Transmits OSC messages over UDP to a network host. |
| [`Out`](/reference/library/io/serial/out) | `IO::Serial` | Module | Writes signal values to platform serial output stream. |
| [`OutOfRange`](/reference/library/status/outofrange) | `Status` | Constant | A value or index lies outside what is allowed: a number too big for Int, a pin the board does not have |

## P

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Pan`](/reference/library/dsp/routing/pan) | `Dsp::Routing` | Module | Linear stereo panner splitting a mono signal into stereo left [0] and right [1]. |
| [`Park`](/reference/library/control/foc/park) | `Control` | Module | Park transform: [Ialpha, Ibeta] >> Park(angle: Theta) >> [Id, Iq]. |
| [`PeakingEq`](/reference/library/dsp/filters/peakingeq) | `Dsp::Filters` | Module | Second-order peaking equaliser: Input >> PeakingEq(frequency: 1000.0 q: 1.0 gain: 6.0) >> Output. A BiQuad with FilterDesign::ModePeak; gain is in dB. The frequency is in Hz and is converted against the rate of the output. The data type must be floating point. |
| [`Pi`](/reference/library/math/constants/pi) | `Math::Constants` | Constant | Mathematical constant Pi (ratio of a circle's circumference to its diameter) |
| [`Pid`](/reference/library/control/pid/pid) | `Control` | Module | Proportional-Integral-Derivative controller with anti-windup clamping: Error >> Pid(kp: 1.0 ki: 0.05 kd: 0.1) >> Output. ki (per second) and kd (seconds) are converted against the rate of the output, so tuning does not change with the sample rate. Type must be floating point. |
| [`Platform`](/reference/library/status/platform) | `Status` | Constant | A failure of the platform runtime's own |
| [`Pow`](/reference/library/math/pow) | *(Global Prelude)* | Module | Computes Base raised to the power of Exponent: pow(Input[0], Input[1]). |
| [`Print`](/reference/library/io/console/print) | `IO::Console` | Module | Prints the value of a stream to standard console output. |
| [`Print`](/reference/library/io/serial/print) | `IO::Serial` | Module | Writes values formatted to the serial port. |
| [`Println`](/reference/library/io/console/println) | `IO::Console` | Module | Prints the value of a stream to standard console output with a trailing newline. |
| [`Probe`](/reference/library/debug/probe) | *(Global Prelude)* | Module | Lightweight signal probe that non-intrusively monitors a stream while passing it through |

## R

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`RandomChance`](/reference/library/random/randomchance) | *(Global Prelude)* | Reaction | on with the given chance, in percent: RandomChance(percent: 25) >> Lucky; |
| [`RandomInt`](/reference/library/random/randomint) | *(Global Prelude)* | Reaction | A random whole number from min to max, both included: RandomInt(min: 1 max: 6) >> Die; |
| [`Rectify`](/reference/library/dsp/filters/rectify) | `Dsp::Filters` | Module | Full-wave signal rectifier. |
| [`RisingEdge`](/reference/library/control/risingedge) | *(Global Prelude)* | Module | Detects rising edge (off -> on): Input >> RisingEdge() >> Trigger. |
| [`Rotate`](/reference/library/linalg/quaternion/rotate) | `LinAlg::Quaternion` | Module | Rotates a 3D vector by orientation quaternion: Vec3D >> Quaternion::Rotate(rotation: Quat) >> RotatedVec. Rotation in space is three dimensional, so the vector has 3 components. |

## S

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Scale`](/reference/library/linalg/vectors/scale) | `LinAlg::Vectors` | Loop | Scales a vector of any dimension: Vec >> Scale(factor: 2.0) >> Scaled. |
| [`Section`](/reference/library/dsp/filters/section) | `Dsp::Filters` | Module | Second-order IIR section with explicit normalised coefficients: Input >> Section(coefficients: Coeffs) >> Output. With the default coefficients [1, 0, 0, 0, 0] the section passes the input unchanged. The data type must be floating point. |
| [`Select`](/reference/library/logic/select) | *(Global Prelude)* | Module | Selects between whenOn and whenOff signals based on a switch condition: Input >> Select(condition: Cond whenOn: Alt whenOff: Input) >> Output. |
| [`Sequencer`](/reference/library/dsp/generators/sequencer) | `Dsp::Generators` | Module | Step sequencer module. |
| [`Sign`](/reference/library/math/sign) | *(Global Prelude)* | Module | Returns 1.0 if input > 0, -1.0 if input < 0, and 0.0 if input == 0. |
| [`Sin`](/reference/library/math/sin) | *(Global Prelude)* | Module | Sine function of angle in radians. |
| [`SlewRateLimiter`](/reference/library/control/slewratelimiter/slewratelimiter) | `Control` | Module | Limits the rate of change of a signal in units per second: Input >> SlewRateLimiter(up: 2.0 down: 5.0) >> Output. The limits are converted against the rate of the output, so they do not change with the sample rate. |
| [`SlipEnd`](/reference/library/io/framing/slipend) | `IO::Framing` | Constant | SLIP END marker (0xC0) |
| [`SlipEsc`](/reference/library/io/framing/slipesc) | `IO::Framing` | Constant | SLIP ESC marker (0xDB) |
| [`SlipEscEnd`](/reference/library/io/framing/slipescend) | `IO::Framing` | Constant | SLIP ESC_END byte (0xDC) |
| [`SlipEscEsc`](/reference/library/io/framing/slipescesc) | `IO::Framing` | Constant | SLIP ESC_ESC byte (0xDD) |
| [`Smooth`](/reference/library/control/smooth) | *(Global Prelude)* | Module | Exponential (one-pole low-pass) smoothing of Input with a time constant in seconds: Input >> Smooth(time: 0.05) >> Output. The time is converted with the rate of the output, so it is independent of the sample rate. Type must be a floating point type. |
| [`SoftClip`](/reference/library/dsp/nonlinear/saturate/softclip) | `Dsp::Nonlinear::Saturate` | Module | Cubic polynomial soft saturator: AudioIn >> Saturate::SoftClip() >> Out. |
| [`Sum`](/reference/library/basicoperations/sum) | *(Global Prelude)* | Loop | Adds all signals in the input array: Input >> Sum() >> Output. |

## T

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`TableOscillator`](/reference/library/dsp/generators/tableoscillator) | `Dsp::Generators` | Module | Table read oscillator. |
| [`Tan`](/reference/library/math/tan) | *(Global Prelude)* | Module | Tangent function of angle in radians. |
| [`Tanh`](/reference/library/dsp/nonlinear/saturate/tanh) | `Dsp::Nonlinear::Saturate` | Module | Padé rational approximation of tanh(x) soft saturation: AudioIn >> Saturate::Tanh() >> Out. |
| [`Transform`](/reference/library/linalg/matrices/transform) | `LinAlg::Matrices` | Loop | Matrix-vector product of any dimension: Vec >> Transform(matrix: Mat) >> Out. The matrix is row-major with (size of the output) rows and (size of the input) columns. |
| [`Transpose`](/reference/library/linalg/matrices/transpose) | `LinAlg::Matrices` | Loop | Transposes a matrix of any shape: Mat >> Transpose(rows: 2 columns: 3) >> Transposed. |
| [`Truncated`](/reference/library/status/truncated) | `Status` | Constant | The result did not fit where it had to go and part of it was dropped: a string past its maxSize, a value past a buffer |
| [`TwoPi`](/reference/library/math/constants/twopi) | `Math::Constants` | Constant | Mathematical constant 2 * Pi (tau) |

## U

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Unavailable`](/reference/library/status/unavailable) | `Status` | Constant | The resource cannot be used right now: a full transmit buffer, a peripheral that is not ready |

## W

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Wedge`](/reference/library/linalg/vectors/wedge) | `LinAlg::Vectors` | Loop | Wedge (exterior) product of two vectors of any dimension: VecA >> Wedge(with: VecB) >> Bivector. For 2 components the output is the scalar a0 b1 - a1 b0 (the 2D cross product); for 3 components it holds the cross product components [x y z] = [w(1,2), -w(0,2), w(0,1)] of the output w; for n components it has n (n - 1) / 2 components. |
| [`Wrap`](/reference/library/math/wrap) | *(Global Prelude)* | Module | Periodically wraps input signal within [min, max): Input >> Wrap(min: 0.0 max: 1.0) >> Output. |

## X

| Symbol | Namespace | Kind | Description |
| :--- | :--- | :--- | :--- |
| [`Xor`](/reference/library/logic/xor) | *(Global Prelude)* | Module | Logical exclusive OR (XOR) operation on switch inputs: [A, B] >> Xor() >> Out. |
