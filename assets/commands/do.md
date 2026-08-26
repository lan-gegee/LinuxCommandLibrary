# TAGLINE

命令重复执行工具

# TLDR

**重复执行命令**

```do [command] [args]```

**指定次数执行**

```do -n [5] [command]```

**指定间隔执行**

```do -i [2] [command]```

**执行直到成功**

```do -s [command]```

# SYNOPSIS

**do** [_options_] _command_ [_args_...]

# PARAMETERS

_COMMAND_
> 要执行的命令。

_ARGS_
> 传递给命令的参数。

**-n** _COUNT_
> 迭代次数。

**-i** _SECONDS_
> 各次执行之间的间隔。

**-s**
> 成功（退出码为零）时停止。

**-f**
> 失败（退出码非零）时停止。

**--help**
> 显示帮助信息。

# DESCRIPTION

**do** 是一个用于重复执行命令的简单工具。它提供了控制迭代次数、时间间隔以及基于命令退出状态的终止条件的选项。

该工具适用于轮询操作、重试失败的命令以及自动化测试等场景。对于常见的重复模式，它比 while 循环提供了更简单的接口。

不同系统和软件仓库中存在多种名为 'do' 的实现，功能集各不相同。具体行为取决于所安装的版本。

# CAVEATS

名称可能与 Shell 内建命令或其他实用程序冲突。不同实现的选项各不相同。对会被 Shell 解释的参数可能需要转义。

# HISTORY

不同系统和软件仓库中存在多个名为 'do' 的工具。命令重复是 Shell 脚本中的基础概念，各种工具为其提供了便捷的接口。

# INSTALL

```aur: yay -S do```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[watch](/man/watch)(1), [while](/man/while)(1)
