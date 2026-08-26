# TAGLINE

Gentoo 系统配置和管理工具

# TLDR

列出所有**可用模块**

```eselect modules list```

显示特定模块的**帮助**

```eselect [module] help```

**列出**某个模块可用的选项

```eselect [module] list```

**显示**某个模块当前的设置

```eselect [module] show```

**为某个模块设置**目标

```sudo eselect [module] set [target]```

选择生效的**内核**源码

```sudo eselect kernel set [number]```

# SYNOPSIS

**eselect** [_global options_] _module_ _action_ [_options_]

# GLOBAL OPTIONS

**--brief**
> 降低输出的详细程度。

**--colour=**_yes_|_no_|_auto_
> 控制彩色输出（默认：auto）。

# DESCRIPTION

**eselect** 是 Gentoo Linux 的多用途配置和系统管理工具。它提供统一、模块化的框架来管理各种系统设置，否则这些设置就需要手动编辑配置文件或管理符号链接。常见用途包括选择内核源码、切换编译器版本、管理 Java 实现、配置 locale 以及设置系统 profile。

该工具的模块化设计意味着系统配置的每个方面都由一个专用模块以一致的语法处理（list、set、show、help）。这让系统管理更加便捷，并降低了配置出错的风险。额外的模块可以由软件包提供，按需扩展 eselect 对特定软件的支持能力。

# PARAMETERS

**list**
> 列出可用的选项。

**set** _target_
> 设置指定的目标。

**show**
> 显示当前设置。

**help**
> 显示模块帮助。

**update**
> 在配置未设置或无效时刷新配置。

**version**
> 显示模块版本。

# COMMON MODULES

**kernel**
> 配置 /usr/src/linux 符号链接。

**profile**
> 管理 make.profile 符号链接。

**locale**
> 设置 LANG 环境变量。

**gcc**
> 选择生效的 GCC 编译器版本。

**editor**
> 管理 EDITOR 环境变量。

**repository**
> 管理 ebuild 软件仓库。

**news**
> 阅读 Gentoo 新闻条目。

# CAVEATS

仅适用于 Gentoo Linux。可用模块取决于已安装的软件包。部分模块需要 root 权限。

# SEE ALSO

[eselect-kernel](/man/eselect-kernel)(1), [eselect-locale](/man/eselect-locale)(1), [eselect-profile](/man/eselect-profile)(1), [emerge](/man/emerge)(1)
