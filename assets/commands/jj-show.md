# TAGLINE

显示变更的详细信息

# TLDR

显示当前变更（工作副本）

```jj show```

显示特定修订

```jj show [revset]```

显示改动直方图

```jj show --stat```

仅显示被更改文件的摘要

```jj show -s```

显示 Git 格式的 diff

```jj show --git```

使用自定义输出模板

```jj show -T "[template]"```

# SYNOPSIS

**jj show** [_options_] [_revsets_...]

# PARAMETERS

_REVSETS_
> 要显示的修订（默认：@，即工作副本提交）。

**-T**, **--template** _TEMPLATE_
> 使用给定模板渲染每个修订。

**-p**, **--patch**
> 显示相对于父修订的补丁。

**-s**, **--summary**
> 对每个路径，仅显示它是被修改、新增还是删除。

**--stat**
> 显示改动的直方图。

**--types**
> 对每个路径，仅显示其类型（F=文件、L=符号链接、C=冲突、G=Git 子模块）。

**--name-only**
> 对每个路径，仅显示其路径名。

**--git**
> 显示 Git 格式的 diff。

**--color-words**
> 显示词级别的 diff，仅通过颜色标示改动。

**--tool** _TOOL_
> 通过外部命令生成 diff。

**--context** _N_
> 显示的上下文行数。

**-w**, **--ignore-all-space**
> 比较行时忽略空白字符。

**-b**, **--ignore-space-change**
> 比较行时忽略空白字符数量的变化。

# DESCRIPTION

**jj show** 显示 Jujutsu 仓库中某个变更的详细信息，包括描述、作者、时间戳以及与其父修订相比的 diff。输出可以通过模板和多种 diff 格式化选项进行自定义。

# CAVEATS

**jj** 的子命令。符号 `@` 指工作副本提交。模板语法是 Jujutsu 特有的；参见 `jj help -k templates`。

# HISTORY

**jj show** 是 **Jujutsu**（jj，一款与 Git 兼容的 DVCS）的一部分，用于详细查看单个变更。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-log](/man/jj-log)(1), [jj-diff](/man/jj-diff)(1)
