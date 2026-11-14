# Systems, Frameworks, Platforms, and Domains

Stride formalizes the division between physical hardware, toolchains, computation scheduling, and system topology into four distinct architectural concepts:

```mermaid
flowchart TD
    subgraph System["System: Multi-Domain Topology"]
        direction TB

        subgraph Host["Platform: PC Host (Desktop / Server)"]
            direction TB
            FrameworkHost["Framework: JIT / C++ Runtime"]
            DomStream["Domain: StreamDomain<br/>(Real-time Signal / Audio / Telemetry)"]
            DomControl["Domain: ControlDomain<br/>(State Machine & Control Logic)"]

            FrameworkHost --> DomStream
            FrameworkHost --> DomControl
        end

        subgraph MCU["Platform: Dual-Core Microcontroller (RP2350)"]
            direction TB
            FrameworkMCU["Framework: PicoSDK / BareMetal"]
            DomDSP["Domain: DspDomain<br/>(Core 0: Low-Latency Signal Processing)"]
            DomIO["Domain: IoDomain<br/>(Core 1: Hardware Peripheral I/O)"]

            FrameworkMCU --> DomDSP
            FrameworkMCU --> DomIO
            DomDSP <==>|Connection: Shared SRAM / DMA| DomIO
        end

        DomControl ==>|Connection: USB / Serial / Protobuf| FrameworkMCU
    end
```

---

## 1. Architectural Taxonomy

| Concept | What It Represents | Key Responsibilities | Examples |
| :--- | :--- | :--- | :--- |
| **Platform** | **Hardware Support** | Hardware descriptions, device pinouts, peripherals, registers, memory layouts, DMA controllers, interrupt vectors. | `RP2040`, `RP2350`, `STM32F4`, `Local_x86_64` |
| **Framework** | **Toolchain & Runtime** | Code emission targets, compiler backends, platform modules, language operator lowerings, runtime library bindings. | `JIT`, `Cpp`, `RtAudio`, `Wiring`, `PicoSDK` |
| **System** | **Deployment Topology** | Groups platforms and frameworks into a whole; declares abstract **Connections** between disparate execution targets. | `DesktopApp`, `DualCoreBldcSystem`, `GameEngineSystem` |
| **Domain** | **Computation Group** | Execution context for signals, streams, and state machines; bound to a **Framework**; requires and provides **Resources**. | `StreamDomain`, `ControlDomain`, `GameStateDomain`, `RootDomain` |

---

## 2. Platforms: Hardware Abstraction

A **Platform** (`platform`) encapsulates target hardware capabilities and physical resources. It defines the physical substrate:
- Processor cores (ARM Cortex-M, RISC-V, x86_64), clock frequencies, and cache structures.
- Memory topologies: SRAM banks, flash boundaries, tightly-coupled memories (TCM), zero-latency scratchpads (zpads).
- Peripheral bindings: GPIOs, ADC/DAC channels, SPI/I2C/UART controllers.

```stride
platform _PicoPlatform {
    framework: "Pico"
    frameworkVersion: "1.0"
    hardware: "RP2040"
    hardwareVersion: "1.0"
}
```

---

## 3. Domains: Thread & Rate Isolation

A **Domain** represents a single thread of execution, core, or rate context:

* **Real-time stream domains** (such as high-rate audio DSP, sensor telemetry, or motor control) run inside high-priority interrupts or dedicated DSP cores without dynamic memory allocation.
* **Discrete state machine & control domains** (such as turn-based game logic, protocol parsers, or user interfaces) run asynchronously or inside background scheduler loops.

When streams cross domain boundaries, Stride enforces synchronization mechanisms:
- **Semaphores & Mutexes**: For buffer pool leases and atomic resource locks.
- **Double-Buffer Ping-Pong**: For DMA transfers without latency jitter.
- **Ring Buffers / FIFOs**: For asynchronous event and message streams.
