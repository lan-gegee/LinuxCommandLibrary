# TAGLINE

数字仿真结果的波形查看器

# TLDR

**打开波形文件**

```gtkwave [dump.vcd]```

**连同保存文件一起打开**

```gtkwave [dump.vcd] [signals.gtkw]```

**将 FST 转换为 VCD**

```vcd2fst [input.vcd] [output.fst]```

**打开 LXT 文件**

```gtkwave [dump.lxt]```

# SYNOPSIS

**gtkwave** [_options_] [_dumpfile_] [_savefile_]

# PARAMETERS

_dumpfile_
> 波形文件（VCD、FST、LXT、LXT2）。

_savefile_
> GTKWave 保存文件（.gtkw）。

**-o**, **--optimize**
> 加载时将 VCD 转换/优化为 FST，以减少内存占用。

**-a** _file_, **--save** _file_
> 指定要使用的保存文件（.gtkw）名称。

**-c** _n_, **--cpu** _n_
> 可用于可并行操作的 CPU 数量。

**-r** _file_, **--rcfile** _file_
> 覆盖默认的 .gtkwaverc 文件名。

**-S** _file_, **--script** _file_
> 要执行的 Tcl 命令脚本文件。

**-T** _file_, **--tcl_init** _file_
> 启动时加载的 Tcl 命令脚本文件。

**-N**, **--nowm**
> 为大多数窗口禁用窗口管理器。

**-6**, **--dark**
> 优先使用深色主题。

**-x**, **--exit**
> 加载波形后立即退出（适用于脚本化转换）。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**GTKWave** 是一款数字仿真结果波形查看器。它显示来自 VCD（Value Change Dump）、FST、LXT 等格式的信号轨迹，这些格式由 Verilator、Icarus Verilog 和 GHDL 等仿真器生成。

该工具提供层次化信号浏览、缩放/平移、标记、注释以及导出功能，用于分析数字电路行为。

# SUPPORTED FORMATS

- VCD (IEEE 1364)
- FST (Fast Signal Trace)
- LXT, LXT2（压缩格式）
- GHW（GHDL 波形）
- VZT（压缩 VCD）

# CAVEATS

大型 VCD 文件可能很慢；请使用 FST 格式。复杂层次结构需要手动导航。内存占用随转储文件大小增长。

# HISTORY

GTKWave 由 **Tony Bybell** 编写，是一款面向数字设计验证的开源波形查看器。它已成为开源 HDL 仿真器的标准查看器。

# INSTALL

```apt: sudo apt install gtkwave```

```dnf: sudo dnf install gtkwave```

```pacman: sudo pacman -S gtkwave```

```zypper: sudo zypper install gtkwave```

```nix: nix profile install nixpkgs#gtkwave```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iverilog](/man/iverilog)(1), [verilator](/man/verilator)(1), [ghdl](/man/ghdl)(1)

# RESOURCES

```[Source code](https://github.com/gtkwave/gtkwave)```

```[Homepage](https://gtkwave.sourceforge.net/)```

```[Documentation](https://gtkwave.github.io/gtkwave/)```

<!-- verified: 2026-07-17 -->
