# TAGLINE

Verilog 转 C++ 仿真编译器

# TLDR

**对 Verilog 进行静态检查**

```verilator --lint-only [design.v]```

**编译为 C++**

```verilator --cc [design.v]```

**配合测试平台（testbench）使用**

```verilator --cc [design.v] --exe [testbench.cpp]```

**构建仿真程序**

```verilator --cc [design.v] --exe [tb.cpp] --build```

**生成波形文件**

```verilator --cc [design.v] --trace```

**生成 SystemC 输出**

```verilator --sc [design.v]```

**直接构建二进制可执行文件**

```verilator --binary [design.v] --exe [tb.cpp]```

**以并行任务编译**

```verilator --cc [design.v] --exe [tb.cpp] --build -j [4]```

# SYNOPSIS

**verilator** [_--lint-only_] [_--cc_] [_--trace_] [_options_] _files_

# PARAMETERS

**--lint-only**
> 仅进行 lint 检查。

**--cc**
> 生成 C++ 代码。

**--exe**
> 创建可执行文件。

**--build**
> 编译生成的输出。

**--trace**
> 启用波形跟踪。

**--sc**
> 生成 SystemC 输出。

**--binary**
> 生成 C++ 并直接构建出二进制可执行文件。

**-Wall**
> 启用所有警告。

**--top-module** _module_
> 指定顶层模块名称。

**-j** _N_
> 构建任务的并行度。

**-CFLAGS** _flags_
> 向 C++ 编译器传递选项。

**-LDFLAGS** _flags_
> 向 C++ 链接器传递选项。

# DESCRIPTION

**verilator** 将可综合的 Verilog 和 SystemVerilog 设计转换为优化的 C++ 或 SystemC 模型。生成的代码会编译为原生可执行文件，运行速度显著快于解释型仿真器，使其成为目前最快的开源 Verilog 仿真器之一。

该工具还可以通过 **--lint-only** 作为 lint 检查器使用，在不生成仿真代码的情况下捕获常见的编码错误和风格问题。可通过 **--trace** 启用波形跟踪，生成 VCD 文件供 GTKWave 等波形查看器查看。

# CAVEATS

Verilator 基于周期（cycle-based），仅支持 Verilog/SystemVerilog 的可综合子集。它不支持所有仿真结构（例如延迟、部分系统任务）。仅支持两态仿真（不传播 X/Z）。

# HISTORY

**Verilator** 由 **Wilson Snyder** 创建，通过 C++ 编译实现了最快速的 Verilog 仿真。

# INSTALL

```apt: sudo apt install verilator```

```dnf: sudo dnf install verilator```

```pacman: sudo pacman -S verilator```

```apk: sudo apk add verilator```

```zypper: sudo zypper install verilator```

```brew: brew install verilator```

```nix: nix profile install nixpkgs#verilator```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iverilog](/man/iverilog)(1), [gtkwave](/man/gtkwave)(1), [yosys](/man/yosys)(1)
