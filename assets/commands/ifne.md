# TAGLINE

仅在有输入时才运行命令

# TLDR

**有输入时才运行命令**

```command1 | ifne command2```

**有结果时删除文件**

```find . -empty | ifne xargs rm```

**反转条件**

```command | ifne -n echo "no output"```

**有错误时发送邮件**

```make 2>&1 | ifne mail -s "errors" [admin]```

# SYNOPSIS

**ifne** [_options_] _command_ [_args_]

# PARAMETERS

_COMMAND_
> 要运行的命令。

_ARGS_
> 命令参数。

**-n**
> 在没有输入时才运行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ifne**（"if not empty"，即"非空则执行"）从标准输入读取数据，只有当输入非空时才运行给定命令。缓冲的输入随后会重新发送到该命令的标准输入，因此下游看到的仍是原始数据流。使用 **-n** 时行为相反：只有当标准输入为空时才运行命令（适用于在脚本中处理"无事可做"的分支）。

这使得 **ifne** 成为那些可能不产生输出的过滤器的天然补充：像 **find ... -print0 | ifne xargs -0 rm** 或 **make 2>&1 | ifne mail -s "errors" admin** 这样的管道，在没有事情要做时会保持安静。

# CAVEATS

属于 **moreutils**。输入必须能装进内存或管道缓冲区；整个数据流会在命令启动前被读完，因此非常大的输入可能导致速度慢或占用大量内存。只有当输入非空时，stdin 才会被转发给所包装的命令；在 **-n** 的情况下，被包装的命令继承的是空的 stdin。

# HISTORY

ifne 是 **moreutils** 的一部分，后者是由 **Joey Hess** 编写的一套 Unix 工具集。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xargs](/man/xargs)(1), [moreutils](/man/moreutils)(7), [test](/man/test)(1)
