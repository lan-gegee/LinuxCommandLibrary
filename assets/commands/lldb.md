# TAGLINE

LLVM 调试器

# TLDR

**调试可执行文件**

```lldb [program]```

**带参数调试**

```lldb -- [program] [arg1] [arg2]```

**附加到进程**

```lldb -p [pid]```

**按名称附加**

```lldb -n [process_name]```

**启动时执行命令**

```lldb -o "[breakpoint set -n main]" [program]```

**加载核心转储**

```lldb -c [core] [program]```

# SYNOPSIS

**lldb** [_options_] [_program_] [-- _args_]

# PARAMETERS

_PROGRAM_
> 要调试的可执行文件。

**-p** _PID_
> 按 PID 附加到进程。

**-n** _NAME_
> 按名称附加到进程。

**-c** _CORE_
> 加载核心转储文件。

**-o** _CMD_
> 启动时执行命令。

**-s** _FILE_
> 加载后从文件中读取命令。

**-O** _CMD_
> 在加载文件之前执行命令。

**-f** _FILE_
> 指定要调试的可执行文件。

**-a** _ARCH_
> 指定启动程序时使用的架构。

**-w**
> 等待具有 -n 所给名称的进程启动。

**-x**
> 不自动解析 .lldbinit 文件。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**lldb** 是 LLVM 调试器，用于调试 C、C++、Objective-C 和 Swift 程序。

该工具提供断点、观察点、单步执行和内存检查功能。它是 macOS 上的默认调试器，也是 Xcode 开发者工具的一部分。

# CAVEATS

需要调试符号（编译时加 -g 标志）。其命令与 gdb 不同；参见 `lldb` 的 `help` 或 GDB 到 LLDB 的命令对照表。属于 LLVM 工具链的一部分。

# HISTORY

LLDB 由 **Apple** 作为 LLVM 的一部分开发，提供模块化架构的现代调试器。

# INSTALL

```apt: sudo apt install lldb```

```dnf: sudo dnf install lldb```

```pacman: sudo pacman -S lldb```

```apk: sudo apk add lldb```

```zypper: sudo zypper install lldb```

```nix: nix profile install nixpkgs#lldb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [clang](/man/clang)(1)
