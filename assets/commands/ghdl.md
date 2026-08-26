# TAGLINE

开源 VHDL 模拟器与综合器

# TLDR

**分析 VHDL 文件**

```ghdl -a [file.vhdl]```

**细化（elaborate）设计**

```ghdl -e [entity_name]```

**运行仿真**

```ghdl -r [entity_name]```

**以 VCD 波形输出运行**

```ghdl -r [entity_name] --vcd=[output.vcd]```

**以 GHW 波形输出运行**

```ghdl -r [entity_name] --wave=[output.ghw]```

**带停止时间运行仿真**

```ghdl -r [entity_name] --stop-time=[100ns]```

一步完成**细化并运行**

```ghdl --elab-run [entity_name] --vcd=[output.vcd]```

用组合命令**分析、细化并运行**

```ghdl -c [file.vhdl] -r [entity_name]```

**导入文件**

```ghdl -i [file.vhdl]```

**仅做语法检查**

```ghdl -s [file.vhdl]```

# SYNOPSIS

**ghdl** _command_ [_options_] _files_

# PARAMETERS

**-a** _FILE_
> 分析 VHDL 源文件。

**-e** _ENTITY_
> 细化设计实体。

**-r** _ENTITY_
> 运行仿真。

**-i** _FILE_
> 导入 VHDL 文件。

**-s** _FILE_
> 仅做语法检查。

**--vcd** _FILE_
> 生成 VCD 波形输出。

**--wave** _FILE_
> 生成 GHW 波形输出。

**--stop-time** _TIME_
> 仿真停止时间（例如 100ns、1us、10ms）。

**--std** _STANDARD_
> 使用的 VHDL 标准：87、93、93c、00、02、08。

**--work** _NAME_
> 设置 work 库的名称（默认：work）。

**--workdir** _DIR_
> 设置 work 库所在的目录。

**--ieee** _LIBRARY_
> 选择 IEEE 库的变体：none、standard、synopsys。

**-P** _DIRECTORY_
> 添加库搜索路径。

**--elab-run**
> 在单步中完成设计的细化与运行。

**-m** _ENTITY_
> 分析过时文件并细化设计（make 模式）。

**-c** _FILES_ **-r** _ENTITY_
> 在一条命令中完成分析与细化。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ghdl** 是一款开源的 VHDL 模拟器与综合器。它可以对 VHDL 设计进行分析、细化和仿真，支持 VHDL-87、VHDL-93、VHDL-2002 和 VHDL-2008 标准。

典型工作流分为三步：先分析源文件（**-a**）以检查语法并编译，再细化设计层次（**-e**）以解析全部依赖，最后运行仿真（**-r**）。可以生成 VCD 和 GHW 格式的波形输出，供 GTKWave 等工具查看。

# CAVEATS

部分高级 VHDL 特性可能存在限制。综合支持仍属实验性质。大规模仿真可能占用大量内存。

# HISTORY

GHDL 由 **Tristan Gingold** 发起，使用 Ada 编写。它为商业 VHDL 模拟器提供了自由软件替代方案。

# INSTALL

```apt: sudo apt install ghdl-common```

```dnf: sudo dnf install ghdl```

```nix: nix profile install nixpkgs#ghdl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gtkwave](/man/gtkwave)(1), [iverilog](/man/iverilog)(1), [verilator](/man/verilator)(1)
