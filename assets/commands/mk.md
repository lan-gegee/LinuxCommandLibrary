# TAGLINE

Plan 9 的 make 替代品

# TLDR

**构建默认目标**

```mk```

**构建指定目标**

```mk [target]```

**并行构建**

```mk -j```

**使用指定的 mkfile**

```mk -f [mkfile.custom]```

**试运行**

```mk -n```

**强制重新构建**

```mk -a```

# SYNOPSIS

**mk** [_options_] [_target_]

# PARAMETERS

_TARGET_
> 要构建的目标。

**-f** _FILE_
> 使用指定的 mkfile。

**-j**
> 并行执行。

**-n**
> 试运行。

**-a**
> 强制重建全部。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mk** 是 Plan 9 的 make 替代品。它提供类似功能，但语法更简洁。

该工具读取 mkfile 获取构建指令。比传统 make 更简单。

# CAVEATS

Plan 9/9front 工具。与 GNU make 不同。规则语法更简单。

# HISTORY

mk 由贝尔实验室为 **Plan 9** 创建，作为更简洁的 make 替代品。

# INSTALL

```apk: sudo apk add bmk```

```brew: brew install mk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[make](/man/make)(1), [ninja](/man/ninja)(1), [rc](/man/rc)(1)
