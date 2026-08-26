# TAGLINE

Icarus Verilog 编译器

# TLDR

**编译 Verilog 文件**

```iverilog -o [output] [input.v]```

**编译多个文件**

```iverilog -o [output] [file1.v] [file2.v]```

**指定顶层模块**

```iverilog -s [top_module] -o [output] [input.v]```

**生成 VCD 输出**

```iverilog -o [output] [input.v] && vvp [output]```

**包含目录**

```iverilog -I [include_dir] -o [output] [input.v]```

**定义宏**

```iverilog -D[MACRO=value] -o [output] [input.v]```

# SYNOPSIS

**iverilog** [_options_] _file_...

# PARAMETERS

**-o** _FILE_
> 输出文件名。

**-s** _MODULE_
> 指定顶层模块。

**-I** _DIR_
> 添加包含目录。

**-D** _MACRO_
> 定义预处理宏。

**-g** _STANDARD_
> Verilog 标准（2001、2005、2009、2012）。

**-t** _TARGET_
> 目标格式（vvp、null）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**iverilog** 是 Icarus Verilog 编译器。它将 Verilog HDL 编译为仿真可执行文件。

该工具支持 IEEE Verilog 标准。输出结果通过 vvp 仿真器运行，用于验证和测试。

# CAVEATS

仅支持仿真，不支持综合。对部分 SystemVerilog 的支持有限。输出需要 vvp 运行时。

# HISTORY

Icarus Verilog 由 **Stephen Williams** 创建，作为商业 Verilog 仿真器的开源替代品。

# INSTALL

```apt: sudo apt install iverilog```

```dnf: sudo dnf install iverilog```

```pacman: sudo pacman -S iverilog```

```apk: sudo apk add iverilog```

```zypper: sudo zypper install iverilog```

```nix: nix profile install nixpkgs#iverilog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gtkwave](/man/gtkwave)(1), [verilator](/man/verilator)(1), [yosys](/man/yosys)(1)
