# TAGLINE

Gentoo 的内核源码符号链接管理器

# TLDR

**列出**可用的内核源码目标

```eselect kernel list```

**按编号设置** /usr/src/linux 符号链接

```eselect kernel set [number]```

**按名称设置** /usr/src/linux 符号链接

```eselect kernel set [linux-6.1.0-gentoo]```

**显示**当前内核符号链接的目标

```eselect kernel show```

# SYNOPSIS

**eselect kernel** _action_ [_options_]

# PARAMETERS

**list**
> 列出可用的内核源码及其编号，星号标记当前选中的项

**set** _target_
> 将 /usr/src/linux 符号链接设置为指定目标（列表中的名称或编号）

**show**
> 显示当前符号链接的目标

# DESCRIPTION

**eselect kernel** 是 eselect 框架的一个模块，用于管理 Gentoo 系统上的 /usr/src/linux 符号链接。该符号链接至关重要，因为它决定了构建外部内核模块、配置内核或编译需要内核头文件的软件时使用哪个内核源码树。

当安装了多个内核源码版本时（在内核升级或测试期间很常见），该工具提供了一种简便的方式在它们之间切换，无需手动重建符号链接。这对于维护必须针对与正在运行或目标内核版本相匹配的正确内核源码编译的外部模块尤为重要，例如显卡驱动或虚拟化软件。

# CAVEATS

仅适用于 Gentoo Linux。需要先通过 emerge 安装内核源码。所做的更改会影响内核模块的编译路径。它不影响当前正在运行的内核，只影响 /usr/src/linux 所指向的源码树。

# SEE ALSO

[eselect](/man/eselect)(1), [emerge](/man/emerge)(1)
