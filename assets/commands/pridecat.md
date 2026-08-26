# TAGLINE

以 pride 旗帜配色显示文件

# TLDR

以 **pride 配色**打印文件

```pridecat file.txt```

以 **trans** pride 配色打印

```pridecat --trans file.txt```

以 **bisexual** pride 配色打印

```pridecat --bi file.txt```

以 **lesbian** pride 配色打印

```pridecat --lesbian file.txt```

将配色应用于**背景**

```pridecat -b file.txt```

将命令输出通过管道传给 **pridecat**

```ls | pridecat --rainbow```

# SYNOPSIS

**pridecat** [_options_] [_file_]

# DESCRIPTION

**pridecat** 是 cat 的彩色替代品，用 pride 旗帜配色显示文件内容。它支持多种 pride 旗帜，可以为前景文字和背景着色。

# PARAMETERS

**--rainbow**
> 使用彩虹 pride 旗帜配色（默认）

**--trans, --transgender**
> 使用跨性别（transgender）pride 旗帜配色

**--bi, --bisexual**
> 使用双性恋（bisexual）pride 旗帜配色

**--lesbian**
> 使用女同性恋（lesbian）pride 旗帜配色

**--gay**
> 使用男同性恋（gay）pride 旗帜配色

**--pan, --pansexual**
> 使用泛性恋（pansexual）pride 旗帜配色

**--nb, --nonbinary**
> 使用非二元性别（non-binary）pride 旗帜配色

**--ace, --asexual**
> 使用无性恋（asexual）pride 旗帜配色

**-b, --background**
> 将配色应用于背景而非文字

**-f, --force**
> 即使输出目标不是终端也强制彩色输出

**-h, --help**
> 显示帮助信息

# CAVEATS

颜色以 ANSI 转义序列实现。在不支持颜色的终端中输出可能无法正确显示。多个旗帜选项可以组合使用，使各旗帜交替出现。

# HISTORY

**pridecat** 是作为 cat 的一个有趣、多彩的替代品而创建的，让用户可以用 pride 旗帜配色装饰文件内容的显示。

# INSTALL

```nix: nix profile install nixpkgs#pridecat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cat](/man/cat)(1), [lolcat](/man/lolcat)(1)
