# TAGLINE

移除 shell 命令别名

# TLDR

**移除特定别名**

```unalias [name]```

**移除所有别名**

```unalias -a```

**移除多个别名**

```unalias [name1] [name2]```

# SYNOPSIS

**unalias** [**-a**] _name_ ...

# PARAMETERS

**-a**
> 从当前 shell 执行环境中移除所有别名定义。

_name_
> 要移除的一个或多个别名名称。

# DESCRIPTION

**unalias** 是一个 shell 内建命令，用于移除先前定义的命令别名。它可以按名称移除特定别名，也可以使用 **-a** 标志一次移除所有别名。

移除操作仅影响当前 shell 会话。在 shell 启动文件（如 ~/.bashrc 或 ~/.zshrc）中定义的别名会在启动新 shell 时恢复。这使得 unalias 适合临时绕过某个别名以测试底层命令的行为，或调试 shell 配置问题。

成功时返回 0，如果指定的别名名称不存在则返回大于 0 的值。

# CAVEATS

shell 内建命令。跨会话不持久。仅影响当前 shell 执行环境。

# HISTORY

**unalias** 是 POSIX 标准的 shell 内建命令，用于移除用 alias 命令定义的命令别名。

# SEE ALSO

[alias](/man/alias)(1), [type](/man/type)(1), [which](/man/which)(1), [bash](/man/bash)(1), [hash](/man/hash)(1)
