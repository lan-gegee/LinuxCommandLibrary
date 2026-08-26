# TAGLINE

跟踪提交之间的作者归属变化

# TLDR

**显示当前未暂存改动的归属**

```git guilt```

**显示两个提交之间的归属差异**

```git guilt [HEAD~3] [HEAD]```

**从 origin/main 到 HEAD 的归属差异**

```git guilt [origin/main]```

**显示邮箱而非作者姓名**

```git guilt -e [HEAD~3] [HEAD]```

**最近三周内的归属差异**

```git guilt @{3.weeks.ago}```

# SYNOPSIS

**git guilt** [_options_]

**git guilt** [_options_] _since_ [_until_]

# PARAMETERS

_SINCE_
> 起始提交。

_UNTIL_
> 结束提交（默认：HEAD）。

**-e**, **--email**
> 显示作者的邮箱而非姓名。

**-w**, **--ignore-whitespace**
> 在进行 blame 归属时忽略纯空白字符的改动。

**-d**, **--debug**
> 输出调试信息。

**-h**
> 显示用法信息。

# DESCRIPTION

**git guilt** 显示两个提交之间 blame 的差异，计算在指定修订版本之间哪些作者获得或失去了代码行。输出以一串加号或减号组成的条形展示每位作者的净行数变化：正向长度表示归属行数净增加，负向表示净减少。不带参数运行时，它显示的是当前未暂存的已修改文件的归属计数，而不是比较两个修订版本。

它是 git-extras 套件的组成部分，能揭示谁正在积极修改代码库的哪些区域，有助于了解近期的代码所有权变化。

# CAVEATS

属于 git-extras 软件包。基于 blame 的分析在大型历史上可能较慢。衡量的是行数而非复杂度。不支持限定到特定路径。

# HISTORY

git guilt 是 **git-extras** 的组成部分，提供基于 blame 的变更跟踪，其名称源自为代码"追究责任"（assign guilt）这一行为；该技术最初由 Atlassian 的 Tim Pettersen 推广。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-blame](/man/git-blame)(1), [git-effort](/man/git-effort)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/man/git-guilt.md)```

<!-- verified: 2026-07-17 -->
