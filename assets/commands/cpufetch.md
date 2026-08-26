# TAGLINE

CPU 架构信息展示工具

# TLDR

**显示** CPU 信息（默认设置）

```cpufetch```

**以特定配色方案显示**

```cpufetch --color [amd]```

**使用**自定义 RGB 颜色

```cpufetch --color [239,90,45:210,200,200:0,0,0:100,200,45:0,200,200]```

**使用**复古风格

```cpufetch --style retro```

**显示**完整未缩写的 CPU 名称

```cpufetch --full-cpu-name```

在窄终端中**强制使用**小 logo

```cpufetch --logo-short```

# SYNOPSIS

**cpufetch** [_OPTION_]...

# PARAMETERS

**-c**, **--color** _scheme_
> 设置配色方案。接受预定义名称（intel、amd、ibm、arm）或格式为 R,G,B:R,G,B:R,G,B:R,G,B:R,G,B 的自定义 RGB 值（前 3 组用于 ASCII 图案，后 2 组用于文字）。

**-s**, **--style** _style_
> 设置 CPU logo 的风格：fancy（默认）、retro 或 legacy（不支持彩色）。

**-F**, **--full-cpu-name**
> 显示完整未缩写的 CPU 名称。

**--logo-short**
> 强制显示短版 logo。

**--logo-long**
> 强制显示长版 logo。

**--logo-intel-old**
> 使用旧版 Intel logo。

**--logo-intel-new**
> 使用新版 Intel logo。

**-d**, **--debug**
> 打印 CPU 型号和 CPUID 级别以供调试。

**-v**, **--verbose**
> 打印获取过程的额外信息。

**-r**, **--raw**
> 打印原始 CPUID 数据以供调试。

**-h**, **--help**
> 打印帮助并退出。

**-V**, **--version**
> 打印版本并退出。

# DESCRIPTION

**cpufetch** 是一个用 C 编写的命令行工具，以美观的格式显示详细的 CPU 架构信息——类似 neofetch 展示系统信息的方式，但专注于 CPU。它会在渲染 CPU 制造商 logo 的 ASCII 艺术图的同时，呈现 CPU 名称、微架构、核心与线程数、最高频率、制程工艺、缓存大小、AVX/FMA/SSE 支持情况以及理论峰值性能等技术细节。

支持 x86_64、ARM、RISC-V 和 PowerPC 架构，覆盖 Linux、Windows、Android、macOS 和 FreeBSD。

# CAVEATS

峰值性能计算使用 CPU 最大频率，但未考虑 AVX 专用的降频。要准确测量峰值性能请改用 **peakperf**。macOS 的 ARM 支持仅限 Apple Silicon 芯片。FreeBSD 支持仅限 x86_64/x86。

# HISTORY

**cpufetch** 由 **Dr-Noob** 创建，首次提交于 **2018 年 3 月**。以 C 编写，采用 GPL-2.0 许可证。最新版本为 v1.07（2025 年 11 月）。同一作者还创建了用于 GPU 信息的 **gpufetch** 和用于精确测量 CPU 性能的 **peakperf**。

# INSTALL

```apt: sudo apt install cpufetch```

```dnf: sudo dnf install cpufetch```

```pacman: sudo pacman -S cpufetch```

```zypper: sudo zypper install cpufetch```

```brew: brew install cpufetch```

```nix: nix profile install nixpkgs#cpufetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1), [fastfetch](/man/fastfetch)(1), [lscpu](/man/lscpu)(1), [screenfetch](/man/screenfetch)(1)
