# TAGLINE

显示 zsh 内建命令的帮助页面

# TLDR

**显示命令的帮助**

```run-help [command]```

**显示内建命令的帮助**

```run-help cd```

**显示外部命令的帮助**

```run-help grep```

**显示感知子命令的 git 帮助**（需要 autoload）

```run-help-git [subcommand]```

**输入时调用帮助**（默认按键绑定）

> 在命令行按下 **ESC h** 或 **Alt+h**

# SYNOPSIS

**run-help** [_command_]

# PARAMETERS

_COMMAND_
> 需要获取帮助的命令、内建命令或函数。

# DESCRIPTION

**run-help** 是一个 Zsh 函数，为命令提供上下文相关的帮助。被调用时，它会判断命令的类型并显示相应的文档，来源可以是 man page、内建帮助或函数定义。

在 Zsh 中，**run-help** 默认绑定到 **ESC h**（或 **Alt+h**），让你在输入命令时快速获取帮助。该函数能智能处理不同类型的命令：对外部命令显示 man page，对内建命令显示 Zsh 文档，对 shell 函数则显示函数源码。

标准的 Zsh 发行版还包含 **run-help-git**、**run-help-ip**、**run-help-openssl** 和 **run-help-sudo** 等辅助函数，可为复杂命令提供感知子命令的帮助。这些函数必须先 autoload 才可用。

要在 Zsh 中启用增强版 run-help 功能，请在 .zshrc 中添加：

```
autoload -Uz run-help
unalias run-help 2>/dev/null
alias help=run-help
```

# CAVEATS

在某些 Zsh 配置中，run-help 默认被别名到 man，从而失去智能行为。**unalias run-help** 命令可移除该别名以恢复完整功能。针对特定命令的辅助函数（如 run-help-git 等）必须单独 autoload。该函数依赖已安装的 man page 来提供外部命令的文档。

# HISTORY

**run-help** 从早期版本起就是 Zsh 的一部分，在 shell 中提供了一个集成帮助系统。该函数逐步演进，可以为带子命令的复杂命令支持模块化辅助函数。它体现了 Zsh 直接在命令行提供丰富、上下文相关用户辅助的理念。

# SEE ALSO

[man](/man/man)(1), [help](/man/help)(1), [info](/man/info)(1), [whatis](/man/whatis)(1), [apropos](/man/apropos)(1)
