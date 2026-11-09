---
title: Standard Library Reference
description: Complete API reference for Stride standard modules, filters, generators, and math operations.
---

# Standard Library Reference

The Stride standard library provides reactive stream processors, oscillators, filters, math constants, and control structures.

All standard packages are namespaced under `Stride::*`. You can import the entire library via `import Stride` or import individual categories (e.g. `import Stride::Generators`).

## Package Categories

### `Stride::Assertions` (10 modules)

[ExpectEqual](/reference/library/assertions/expectequal), [ExpectNear](/reference/library/assertions/expectnear), [ExpectTrue](/reference/library/assertions/expecttrue), [ExpectFalse](/reference/library/assertions/expectfalse), [ExpectGt](/reference/library/assertions/expectgt), [ExpectGe](/reference/library/assertions/expectge)...


### `Stride::BasicOperations` (1 modules)

[Sum](/reference/library/basicoperations/sum)


### `Stride::Callable` (7 modules)

[_MainInputPort](/reference/library/callable/_maininputport), [_MainOutputPort](/reference/library/callable/_mainoutputport), [_PropertyInputPort](/reference/library/callable/_propertyinputport), [_PropertyOutputPort](/reference/library/callable/_propertyoutputport), [_PortAttributes](/reference/library/callable/_portattributes), [_Port](/reference/library/callable/_port)...


### `Stride::CodeGenerators` (4 modules)

[_CodeGenerator](/reference/library/codegenerators/_codegenerator), [_Module](/reference/library/codegenerators/_module), [_Reaction](/reference/library/codegenerators/_reaction), [_Loop](/reference/library/codegenerators/_loop)


### `Stride::Comparisons` (1 modules)

[Greater](/reference/library/comparisons/greater)


### `Stride::Constants` (0 modules)




### `Stride::Control` (1 modules)

[OnChange](/reference/library/control/onchange)


### `Stride::CoreTypes` (11 modules)

[_Constant](/reference/library/coretypes/_constant), [_Switch](/reference/library/coretypes/_switch), [_Trigger](/reference/library/coretypes/_trigger), [_Signal](/reference/library/coretypes/_signal), [_Buffer](/reference/library/coretypes/_buffer), [_Table](/reference/library/coretypes/_table)...


### `Stride::Counter` (1 modules)

[Counter](/reference/library/counter/counter)


### `Stride::DataTypes` (3 modules)

[_TypeClass](/reference/library/datatypes/_typeclass), [_TypeClassConversion](/reference/library/datatypes/_typeclassconversion), [_Variadic](/reference/library/datatypes/_variadic)


### `Stride::Debug` (4 modules)

[DebugPrint](/reference/library/debug/debugprint), [Error](/reference/library/debug/error), [Probe](/reference/library/debug/probe), [Watch](/reference/library/debug/watch)


### `Stride::Domain` (2 modules)

[_DomainDefinition](/reference/library/domain/_domaindefinition), [Exit](/reference/library/domain/exit)


### `Stride::Filters` (5 modules)

[BandPass](/reference/library/filters/bandpass), [BiQuad](/reference/library/filters/biquad), [LowPass](/reference/library/filters/lowpass), [Mix](/reference/library/filters/mix), [Rectify](/reference/library/filters/rectify)


### `Stride::Framework` (9 modules)

[_PlatformModulePortType](/reference/library/framework/_platformmoduleporttype), [_PlatformCodeType](/reference/library/framework/_platformcodetype), [_PlatformModuleType](/reference/library/framework/_platformmoduletype), [_PlatformEntityType](/reference/library/framework/_platformentitytype), [_PlatformType](/reference/library/framework/_platformtype), [_FrameworkDescriptionType](/reference/library/framework/_frameworkdescriptiontype)...


### `Stride::FrameworkDataTypes` (4 modules)

[_FrameworkTypeClass](/reference/library/frameworkdatatypes/_frameworktypeclass), [_FrameworkDataType](/reference/library/frameworkdatatypes/_frameworkdatatype), [_TableType](/reference/library/frameworkdatatypes/_tabletype), [_BufferType](/reference/library/frameworkdatatypes/_buffertype)


### `Stride::FunctionTest` (1 modules)

[_FunctionTest](/reference/library/functiontest/_functiontest)


### `Stride::Generators` (5 modules)

[BandLimitedSaw](/reference/library/generators/bandlimitedsaw), [AD](/reference/library/generators/ad), [Oscillator](/reference/library/generators/oscillator), [Sequencer](/reference/library/generators/sequencer), [TableOscillator](/reference/library/generators/tableoscillator)


### `Stride::Level` (1 modules)

[Level](/reference/library/level/level)


### `Stride::Literals` (7 modules)

[_StringLiteral](/reference/library/literals/_stringliteral), [_IntLiteral](/reference/library/literals/_intliteral), [_RealLiteral](/reference/library/literals/_realliteral), [_PortProperty](/reference/library/literals/_portproperty), [_MemberAccess](/reference/library/literals/_memberaccess), [_SwitchLiteral](/reference/library/literals/_switchliteral)...


### `Stride::Logic` (1 modules)

[Select](/reference/library/logic/select)


### `Stride::Math` (4 modules)

[_Pi](/reference/library/math/_pi), [_TwoPi](/reference/library/math/_twopi), [_E](/reference/library/math/_e), [Abs](/reference/library/math/abs)


### `Stride::Notes` (4 modules)

[C4](/reference/library/notes/c4), [E4](/reference/library/notes/e4), [G4](/reference/library/notes/g4), [C5](/reference/library/notes/c5)


### `Stride::Object` (8 modules)

[_Alias](/reference/library/object/_alias), [_Typed](/reference/library/object/_typed), [_Streamable](/reference/library/object/_streamable), [_Resetable](/reference/library/object/_resetable), [_Rated](/reference/library/object/_rated), [_DomainMember](/reference/library/object/_domainmember)...


### `Stride::Osc` (1 modules)

[OSCOut](/reference/library/osc/oscout)


### `Stride::Pan` (1 modules)

[Pan](/reference/library/pan/pan)


### `Stride::QualityPolicy` (6 modules)

[Optimal](/reference/library/qualitypolicy/optimal), [Fast](/reference/library/qualitypolicy/fast), [Accurate](/reference/library/qualitypolicy/accurate), [Compact](/reference/library/qualitypolicy/compact), [_PolicyBinding](/reference/library/qualitypolicy/_policybinding), [_DeviceType](/reference/library/qualitypolicy/_devicetype)


### `Stride::Resource` (3 modules)

[_ResourceConfigurationType](/reference/library/resource/_resourceconfigurationtype), [_ResourceType](/reference/library/resource/_resourcetype), [_DomainResourceType](/reference/library/resource/_domainresourcetype)


### `Stride::Schema` (11 modules)

[_Any](/reference/library/schema/_any), [_List](/reference/library/schema/_list), [_Entity](/reference/library/schema/_entity), [_Constraint](/reference/library/schema/_constraint), [_ConstrainedInt](/reference/library/schema/_constrainedint), [_ConstrainedString](/reference/library/schema/_constrainedstring)...


### `Stride::Serial` (1 modules)

[SerialPrint](/reference/library/serial/serialprint)


### `Stride::StateMachine` (2 modules)

[_TransitionType](/reference/library/statemachine/_transitiontype), [_StateType](/reference/library/statemachine/_statetype)


### `Stride::tests` (3 modules)

[ClassicScaleModule](/reference/library/tests/classicscalemodule), [ClassicAccumulatorModule](/reference/library/tests/classicaccumulatormodule), [ClassicSumLoop](/reference/library/tests/classicsumloop)

