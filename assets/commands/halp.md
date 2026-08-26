# TAGLINE

用于获取命令行工具帮助信息的 CLI 工具

# TLDR

检查命令的**帮助标志**

```halp [command]```

显示命令的**手册页**或速查表

```halp plz [command]```

**检查命令的指定参数**

```halp --check [--flag] [command]```

为检查**设置自定义超时时间**

```halp -t [10] [command]```

# SYNOPSIS

**halp** [_options_] _command_

**halp** **plz** [_options_] _command_

# PARAMETERS

**--check** _ARG_
> 设置要检查的参数

**--no-version**
> 禁用版本信息检查

**--no-help**
> 禁用帮助信息检查

**-c**, **--config** _PATH_
> 设置配置文件

**-t**, **--timeout** _S_
> 设置命令的超时时间（默认：5 秒）

**-v**, **--verbose**
> 启用详细日志输出

**-h**, **--help**
> 打印帮助信息

**-V**, **--version**
> 打印版本信息

# DESCRIPTION

**halp** 是一个帮你找到命令行工具正确帮助标志的 CLI 工具。你无需手动尝试 **-h**、**--help**、**-?**、**help** 或其他变体，halp 会检查一份预定义的常用帮助选项列表，并报告其中哪些对该命令有效。

**plz** 子命令更进一步，可以使用你偏好的分页器快速查看命令的手册页或 **cheat.sh** 速查表。

# CAVEATS

某些命令在被特定选项调用时可能产生副作用，即使这些选项只是帮助相关的。默认的 5 秒超时对于运行缓慢的命令可能太短。通过 **cheat.sh** 查询速查表需要联网。

# HISTORY

**halp** 由 **Orhun Parmaksiz** 创建，使用 **Rust** 编写。它的设计初衷是消除猜测命令使用哪个标志来显示帮助信息的烦恼。

# INSTALL

```pacman: sudo pacman -S halp```

```brew: brew install halp```

```nix: nix profile install nixpkgs#halp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [tldr](/man/tldr)(1), [cheat](/man/cheat)(1)
