# TAGLINE

开源 Verilog RTL 综合框架

# TLDR

对 Verilog 文件**运行综合**

```yosys -p "synth -top [module]" [design.v]```

**启动交互式 Shell**

```yosys```

**执行脚本文件**

```yosys -s [script.ys]```

**综合并输出到文件**

```yosys -p "synth -top [module]" -o [output.json] [design.v]```

快速综合**快捷方式**

```yosys -S [design.v]```

**运行 TCL 脚本**

```yosys -c [script.tcl]```

**列出可用命令**

```yosys -H```

**获取命令帮助**

```yosys -h [synth]```

# SYNOPSIS

**yosys** [_options_] [_infile_...]

# PARAMETERS

**-s** _scriptfile_
> 从脚本文件执行命令。

**-c** _tclfile_
> 执行 TCL 脚本文件。

**-p** _command_
> 执行命令。

**-o** _outfile_
> 退出时将设计写入文件。

**-f** _frontend_
> 输入文件使用的前端。

**-b** _backend_
> 输出文件使用的后端。

**-m** _module_
> 加载插件模块。

**-l** _logfile_
> 将日志写入文件。

**-q**
> 安静模式（仅输出错误）。

**-v** _level_
> 日志详细程度级别。

**-t**
> 在日志中添加时间戳。

**-S**
> synth 命令的快捷方式。

**-H**
> 打印命令列表。

**-h** _command_
> 显示特定命令的帮助。

**-Q**
> 不显示横幅。

**-T**
> 不显示页脚。

# DESCRIPTION

**yosys** 是一个开源的 RTL 综合框架。它读取 Verilog 硬件描述语言，并将其综合为适用于多种目标工艺的门级网表。

该工具提供交互式 Shell，包含大量命令用于读取设计、细化、优化、工艺映射和写出结果。综合流程通过脚本文件或命令行参数定义。

支持的输入格式包括 Verilog、RTLIL 和 Liberty。输出格式包括 BLIF、EDIF、JSON、Verilog 以及各种 FPGA 专用格式。该工具支持通过插件扩展功能。

Yosys 广泛应用于开源 FPGA 工具链，包括基于 nextpnr 的 Lattice iCE40 和 ECP5 流程。

# CAVEATS

SystemVerilog 支持有限。复杂设计可能需要多次综合。部分功能需要外部插件模块。存储器和时序优化可能需要手动调整。

# HISTORY

**yosys** 由 Clifford Wolf（现名 Claire Wolf）创建并于 2012 年发布。它成为开源 FPGA 工具链的基础，实现了完全开源的综合流程。该项目现由 YosysHQ 维护，仍是开源 FPGA 生态的核心。

# INSTALL

```apt: sudo apt install yosys```

```dnf: sudo dnf install yosys```

```pacman: sudo pacman -S yosys```

```brew: brew install yosys```

```nix: nix profile install nixpkgs#yosys```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iverilog](/man/iverilog)(1), [verilator](/man/verilator)(1)
