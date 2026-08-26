# TAGLINE

使用 JIT 编译器执行 LLVM 位码

# TLDR

**运行 LLVM 位码**

```lli [program.bc]```

**运行 LLVM IR**

```lli [program.ll]```

**附带参数**

```lli [program.bc] [arg1] [arg2]```

**强制 JIT 编译**

```lli -force-interpreter=false [program.bc]```

**使用解释器**

```lli -force-interpreter [program.bc]```

**设置 JIT 类型**

```lli -jit-kind=[orc] [program.bc]```

# SYNOPSIS

**lli** [_options_] _file_ [_args_]

# PARAMETERS

_FILE_
> LLVM 位码或 IR 文件。

_ARGS_
> 程序参数。

**-force-interpreter**
> 使用解释器而非 JIT。

**-jit-kind** _KIND_
> JIT 引擎类型（mcjit、orc）。

**-entry-function** _NAME_
> 入口函数名称。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lli** 使用即时（JIT）编译器直接执行 LLVM 位码（.bc）或 LLVM 汇编（.ll）格式的程序。lli 不是在磁盘上生成独立的可执行文件，而是在运行时将 LLVM IR 编译为内存中的本机机器代码并立即开始执行，这使它成为快速测试和原型化 LLVM IR 的便利工具，无需单独的编译和链接步骤。

该工具支持两种执行引擎：JIT 编译器（默认），它按需将函数转换为本机代码以获得接近原生的性能；以及通过 `-force-interpreter` 启用的较慢的解释器模式。JIT 后端可以通过 `-jit-kind` 标志在 MCJIT 与较新的 ORC 引擎之间选择。程序参数可以放在位码文件名之后传递，让 lli 可以像原生可执行文件一样运行 LLVM 程序。

# CAVEATS

需要 LLVM 位码输入。启动时有 JIT 开销。属于 LLVM 工具链的一部分。

# HISTORY

lli 是 **LLVM** 项目的组成部分，提供了直接执行 LLVM 中间表示的方式。

# INSTALL

```apt: sudo apt install llvm-runtime```

```dnf: sudo dnf install llvm```

```pacman: sudo pacman -S llvm```

```apk: sudo apk add llvm```

```zypper: sudo zypper install llvm```

```brew: brew install llvm```

```nix: nix profile install nixpkgs#llvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[llc](/man/llc)(1), [llvm-as](/man/llvm-as)(1), [clang](/man/clang)(1)
