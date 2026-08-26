# TAGLINE

详细的 x86 CPU 诊断信息

# TLDR

**显示全部 CPU 信息**

```x86info -a```

**显示 CPU 特性标志**

```x86info -f```

**显示缓存和 TLB 信息**

```x86info -c```

**估算当前时钟频率**

```x86info -mhz```

**显示原始 CPUID 寄存器值**

```x86info -r```

**转储型号专用寄存器**（需要 root 权限）

```sudo x86info -m```

**显示详细描述**

```x86info -v```

**转储 MP 表**（多处理器信息）

```sudo x86info -mp```

# SYNOPSIS

**x86info** [**-a**] [**-c**] [**-f**] [**-m**] [**-mhz**] [**-mp**] [**-r**] [**-s**] [**-v**]

# PARAMETERS

**-a**, **--all**
> 显示所有可用信息。等价于 -c -f -m -r -mhz。

**-c**, **--cache**
> 显示 TLB 和缓存大小，包括缓存相联度。

**-f**, **--flags**
> 显示 CPU 特性标志（SSE、AVX 等）。

**-m**, **--msr**
> 转储型号专用寄存器。需要 root 权限和受支持的处理器。

**-mhz**, **--mhz**
> 估算当前 CPU 时钟频率。

**-mp**, **--mptable**
> 转储 MP 表，显示 BIOS 已知的 CPU。

**-r**, **--registers**
> 显示所有可能的 CPUID 调用返回的原始寄存器值。

**-s**, **--show-machine-check**
> 显示机器检查异常信息。

**-v**, **--verbose**
> 显示 CPU 特性的详细描述。

**-?**, **--help**
> 显示帮助信息。

# DESCRIPTION

**x86info** 显示关于 x86 CPU 的详细诊断信息，包括处理器标识、特性标志、缓存拓扑和型号专用寄存器。它通过 CPUID 指令和 MSR（Model Specific Register，型号专用寄存器）读取来查询处理器。

该工具提供的信息与 /proc/cpuinfo 类似但更加详细，包括缓存相联度、TLB 配置和原始 CPUID 数据。它可以识别 CPU 的厂商、家族、型号和步进，以及支持的指令集扩展。

要获得完整功能，内核必须启用 CPUID 和 MSR 设备驱动，并在 /dev/cpu/\<n\>/cpuid 和 /dev/cpu/\<n\>/msr 创建设备文件。某些选项（MSR 读取、MP 表）需要 root 权限。

# CAVEATS

完整功能需要 CPUID 和 MSR 内核模块。访问 MSR 需要 root 权限。型号专用寄存器的支持因处理器而异。在启用频率调节的系统上，时钟频率估算可能不准确。

# HISTORY

**x86info** 由 **Dave Jones**（davej@redhat.com）编写，他对 Linux 内核的 CPU 识别代码也做出了重要贡献。该工具自 **2000 年代初**起就已可用，提供通过其他方式不易获得的详细 x86 CPU 诊断信息。

# INSTALL

```apt: sudo apt install x86info```

```nix: nix profile install nixpkgs#x86info```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cpuid](/man/cpuid)(1), [lscpu](/man/lscpu)(1), [dmidecode](/man/dmidecode)(8)
