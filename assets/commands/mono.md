# TAGLINE

ECMA 公共语言基础结构（CLI）的开源实现

# TLDR

**运行** .NET 程序集

```mono [path/to/program.exe]```

以**调试模式**运行 .NET 程序集

```mono --debug [path/to/program.exe]```

使用**特定运行时版本**运行

```mono --runtime=v4.0 [path/to/program.exe]```

执行期间**跟踪方法调用**

```mono --trace [path/to/program.exe]```

用**解释器**代替 JIT 运行

```mono --interpreter [path/to/program.exe]```

将程序集**预编译**为原生代码（AOT）

```mono --aot [path/to/assembly.dll]```

# SYNOPSIS

**mono** [_options_] _file_ [_arguments_...]

# PARAMETERS

**--debug[=_options_]**
> 启用调试模式；选项包括 casts、mdb-optimizations、gdb

**--aot[=_options_]**
> 将 CIL 预编译为原生代码；选项：llvm、full、static、asmonly

**--full-aot**
> 只在预生成的 AOT 代码上运行，不使用运行时 JIT

**--interpreter**
> 使用解释器代替 JIT 编译

**--llvm**
> 可用时使用 LLVM 后端生成代码

**--gc=_engine_**
> 选择垃圾回收器：boehm 或 sgen

**-O=_mode_**
> 启用/禁用优化（inline、sse2、tailc、abcrem 等）

**--trace[=_expression_]**
> 跟踪方法调用，可选过滤条件

**--config _filename_**
> 加载自定义配置文件

**--runtime=_version_**
> 覆盖运行时版本选择（如 v4.0）

**--debugger-agent=_options_**
> 配置远程调试能力

**--profile[=_profiler_]**
> 使用指定的分析器启用性能分析

# DESCRIPTION

**Mono** 是 ECMA 公共语言基础结构（CLI）的开源实现，可在 Linux、macOS 及其他平台上执行 .NET 应用。它为 C#、VB.NET 和其他 .NET 语言提供运行时环境。

该运行时加载程序集文件（.exe 或 .dll），并通过即时（JIT）编译把公共中间语言（CIL）字节码编译为原生机器码。也支持预先（AOT）编译，以改善启动性能。

# CAVEATS

已部署的应用不应使用 MONO_PATH 环境变量，因为它会破坏程序集加载器。由于包含针对特定 CPU 的优化，AOT 生成的代码通常无法在不同计算机之间迁移。某些 Windows 专有 API 可能不可用或行为有所不同。

# HISTORY

**Mono** 由 **Miguel de Icaza** 和 **Ximian** 于 **2001 年**启动，是 .NET Framework 的开源实现。后来由 Novell、Xamarin 和 Microsoft 相继赞助。在微软官方发布 .NET Core 之前，该项目使跨平台 .NET 开发成为可能。

# INSTALL

```apt: sudo apt install mono-runtime```

```pacman: sudo pacman -S mono```

```apk: sudo apk add mono```

```brew: brew install mono```

```nix: nix profile install nixpkgs#mono```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mcs](/man/mcs)(1), [gacutil](/man/gacutil)(1), [dotnet](/man/dotnet)(1)
