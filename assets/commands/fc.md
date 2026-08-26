# TAGLINE

列出、编辑并重新执行 shell 命令

# TLDR

**编辑并重新运行**上一条命令

```fc```

**列出最近的命令**

```fc -l```

**列出命令但不带**编号

```fc -ln [10] [20]```

按编号**重新运行命令**

```fc -s [15]```

**编辑特定命令**

```fc [20]```

# SYNOPSIS

**fc** [_options_] [_first_] [_last_]

# PARAMETERS

_FIRST_
> 起始命令（编号或字符串）。

_LAST_
> 范围的结束命令。

**-l**
> 列出命令而不进入编辑。

**-n**
> 列出时不显示命令编号。

**-r**
> 反转列表顺序。

**-s** [_OLD=NEW_]
> 重新运行命令，可选文本替换。

**-e** _EDITOR_
> 使用指定的编辑器。

# DESCRIPTION

**fc** 是一个 shell 内建命令，用于列出、编辑和重新执行历史中的命令。它会在编辑器中打开命令供修改后再执行，便于快速修正之前的命令。

该命令可以列出历史条目，在编辑器中打开单条或一段命令，并通过可选的文本替换直接重新执行命令。默认编辑器依次取自 FCEDIT、EDITOR 或 vi。

fc 特别适合修正长命令中的拼写错误，或在修改后重新运行复杂的管道。

# CAVEATS

只适用于交互式 shell 的历史记录。编辑时会启动外部编辑器。替换语法功能有限。必须启用历史记录。

# HISTORY

fc（fix command）是 **POSIX 规定**的 shell 内建命令，存在于 Korn shell、Bash 和 Zsh 中。它起源于 Korn shell，作为编辑和重新执行命令历史条目的手段。

# INSTALL

```apt: sudo apt install f2c```

```dnf: sudo dnf install f2c```

```zypper: sudo zypper install f2c```

```nix: nix profile install nixpkgs#f2c```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[history](/man/history)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1)
