# TAGLINE

轻量级的 POSIX 兼容 Shell

# TLDR

**启动** ash shell

```ash```

**执行**一条命令

```ash -c "[command]"```

运行**脚本**

```ash [script.sh]```

# SYNOPSIS

**ash** [_-c command_] [_script_] [_arguments_]

# DESCRIPTION

**ash**（Almquist Shell）是一个轻量级的 POSIX 兼容 shell。它比 bash 更小更快，适合嵌入式系统，也可作为精简系统上的 /bin/sh。

许多系统使用 dash（Debian Almquist Shell）作为其 ash 实现。BusyBox 也内置了一个 ash 实现。

# PARAMETERS

**-c** _command_
> 执行命令字符串

**-i**
> 交互模式

**-l**
> 登录 shell

**-s**
> 从 stdin 读取命令

**-e**
> 若某条命令以非零状态退出则立即退出（errexit）。

**-x**
> 执行前将每条命令打印到 stderr（xtrace）。

# CONFIGURATION

**/etc/profile**
> 系统级登录 shell 初始化。

**~/.profile**
> 每个用户的登录 shell 初始化。

**$ENV**
> 若已设置，交互式 shell 会加载它（通常指向 ~/.ashrc）。

# CAVEATS

功能不如 bash 丰富；没有数组、扩展 glob 以及众多 bash 特有语法。脚本应只使用 POSIX 语法。它胜在速度，而非便利。

# HISTORY

**ash** 由 Kenneth Almquist 于 **1989** 年为 BSD Unix 编写，作为 Bourne shell 的 POSIX 兼容替代品。后来派生出 dash，并被 BusyBox 采用。

# SEE ALSO

[dash](/man/dash)(1), [bash](/man/bash)(1), [sh](/man/sh)(1), [busybox](/man/busybox)(1)
