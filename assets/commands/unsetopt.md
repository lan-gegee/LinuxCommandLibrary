# TAGLINE

禁用 zsh shell 选项

# TLDR

**禁用选项**

```unsetopt [optionname]```

**禁用 glob**

```unsetopt glob```

**禁用扩展 glob**

```unsetopt extendedglob```

**显示所有选项**

```unsetopt```

# SYNOPSIS

**unsetopt** [_options_]

# PARAMETERS

_option_
> 要禁用的选项。

# COMMON OPTIONS

- **glob** - 文件名通配展开
- **extendedglob** - 扩展模式
- **nomatch** - 无匹配时报错
- **correct** - 命令纠正

# DESCRIPTION

**unsetopt** 是一个 zsh 内建命令，用于禁用 shell 选项，是 **setopt** 的对应命令。它控制 zsh 行为的各个方面，包括文件名通配展开、命令纠正、历史记录处理和提示符展开。

不带参数调用时，unsetopt 会显示当前所有未设置的选项。选项名不区分大小写，且选项名中的下划线会被忽略，因此 **extendedglob**、**EXTENDED_GLOB** 和 **ExtendedGlob** 都指向同一个选项。

除非写入 ~/.zshrc 等 zsh 配置文件，否则更改仅影响当前 shell 会话。该命令为 zsh 专有，在 bash 中没有对应物；bash 用 **shopt -u** 实现类似目的，但选项名称不同。

# CAVEATS

仅限 zsh。启用选项请用 setopt。参见 zshoptions(1)。

# HISTORY

**unsetopt** 是 zsh 用于禁用 shell 选项的内建命令，与 setopt 相对应。

# SEE ALSO

[setopt](/man/setopt)(1), [zsh](/man/zsh)(1)
