# TAGLINE

从 justfile 读取配方来执行命令的命令运行器

# TLDR

**运行默认配方**

```just```

**运行指定配方**

```just [recipe]```

**带参数运行配方**

```just [recipe] [arg1] [arg2]```

**列出可用配方**

```just --list```

**显示配方源码**

```just --show [recipe]```

# SYNOPSIS

**just** [_options_] [_recipe_...] [_arguments_...]

# PARAMETERS

**--list**
> 列出可用配方。

**--show** _recipe_
> 显示配方源码。

**-f**, **--justfile** _file_
> 使用指定的 justfile。

**--choose**
> 交互式选择配方。

**--dry-run**
> 只打印命令而不执行。

**-q**, **--quiet**
> 抑制输出。

# DESCRIPTION

**just** 是一个命令运行器，它从 justfile 中读取配方。它提供了一种保存和运行项目专属命令的便捷方式。语法借鉴了 make，但专注于运行命令而非构建。配方可以用任何语言编写。

# SEE ALSO

[make](/man/make)(1), [task](/man/task)(1)
