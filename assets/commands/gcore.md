# TAGLINE

生成进程核心转储

# TLDR

**生成核心转储**

```gcore [pid]```

**指定输出文件**

```gcore -o [corefile] [pid]```

**对所有**线程生成转储

```gcore -a [pid]```

# SYNOPSIS

**gcore** [_options_] _pid_

# PARAMETERS

_PID_
> 要转储的进程 ID。

**-o** _FILE_
> 输出文件名前缀。

**-a**
> 转储所有线程。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcore** 在不终止进程的情况下生成正在运行的进程的核心转储。它捕获进程的内存状态供调试或分析之用，而进程本身继续运行。

该工具会临时附加到目标进程以创建转储。生成的核心文件可以用 GDB 等调试器分析，以检查程序状态。

gcore 适用于在不造成停机的前提下调试生产系统。

# CAVEATS

需要 ptrace 权限。大型进程会产生很大的转储文件。可能会短暂暂停目标进程。

# HISTORY

gcore 是 **GDB**（GNU Debugger）的一部分，提供无损核心转储生成功能，可在不中断服务的情况下调试运行中的进程。

# INSTALL

```apt: sudo apt install gdb```

```dnf: sudo dnf install gdb```

```pacman: sudo pacman -S gdb```

```apk: sudo apk add gdb```

```zypper: sudo zypper install gdb```

```brew: brew install gdb```

```nix: nix profile install nixpkgs#gdb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [kill](/man/kill)(1)
