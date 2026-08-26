# TAGLINE

转储详细的 x86/x64 处理器信息

# TLDR

显示**所有 CPU** 的信息

```cpuid```

仅显示**当前 CPU** 的信息

```cpuid -1```

显示未经解码的**原始十六进制**信息

```cpuid -r```

使用**内核 CPUID 模块**显示信息

```cpuid -k```

从**文件**读取 CPUID 数据

```cpuid -f [cpuid_dump.txt]```

# SYNOPSIS

**cpuid** [_options_]

# DESCRIPTION

**cpuid** 通过执行 CPUID 指令并解码结果来转储详细的 CPU 信息。它显示处理器标识、特性标志、缓存信息以及其他 CPU 细节。

比 /proc/cpuinfo 更详细，可展示低层级的处理器能力。

# PARAMETERS

**-1, --one-cpu**
> 仅显示当前 CPU 的信息

**-r, --raw**
> 显示原始十六进制值，不做解码

**-f, --file** _file_
> 从文件读取原始数据，而不是执行 CPUID 指令

**-k, --kernel**
> 使用内核 CPUID 模块（/dev/cpu/*/cpuid）；可能需要 root 权限

**-h, --help**
> 显示帮助信息

**-v, --version**
> 显示 cpuid 版本

# CAVEATS

仅支持 x86/x86_64。在虚拟机中运行时，部分信息可能是虚拟化的。解读输出需要对 CPU 架构有所了解。

# INSTALL

```apt: sudo apt install cpuid```

```dnf: sudo dnf install cpuid```

```zypper: sudo zypper install cpuid```

```brew: brew install cpuid```

```nix: nix profile install nixpkgs#cpuid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lscpu](/man/lscpu)(1), [x86info](/man/x86info)(1)
