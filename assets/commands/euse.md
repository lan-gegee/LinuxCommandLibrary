# TAGLINE

Gentoo USE 标志管理工具

# TLDR

列出**生效的全局** USE 标志

```euse -a -g```

列出**生效的本地** USE 标志

```euse -a -l```

**启用**一个全局 USE 标志

```sudo euse -E useflag```

**禁用**一个全局 USE 标志

```sudo euse -D useflag```

**移除**一个全局 USE 标志

```sudo euse -P useflag```

显示某个 USE 标志的**信息**

```euse -i useflag```

# SYNOPSIS

**euse** [_options_] [_useflag_]

# DESCRIPTION

**euse** 是一个 Gentoo 工具，用于启用、禁用 USE 标志以及获取其信息。USE 标志控制安装期间哪些可选特性被编译进软件包，从而对软件能力、依赖关系和二进制体积进行细粒度控制。

该工具提供命令行界面来修改系统和软件包级别的标志，无需手动编辑配置文件，从而简化了 USE 标志的管理。这正是 Gentoo 编译期定制理念的核心所在。

# PARAMETERS

**-a, --active**
> 显示生效中的 USE 标志

**-g, --global**
> 操作全局 USE 标志（make.conf）

**-l, --local**
> 操作本地 USE 标志（package.use）

**-E, --enable**
> 启用指定的 USE 标志

**-D, --disable**
> 禁用指定的 USE 标志（添加 '-' 前缀）

**-P, --prune**
> 从配置中移除指定的 USE 标志

**-i, --info**
> 显示某个 USE 标志的信息（描述、状态、类型）。

**-I, --info-installed**
> 类似 **--info**，但还会列出当前已安装的使用该标志的软件包。

**-h, --help**
> 显示帮助信息。

**-v, --version**
> 显示版本信息。

# CONFIGURATION

**/etc/portage/make.conf**
> 整个系统的全局 USE 标志，通过 USE 变量设置。

**/etc/portage/package.use/**
> 各软件包的 USE 标志设置，以文件形式组织在该目录下。

# CAVEATS

全局 USE 标志设置在 /etc/portage/make.conf 中。本地 USE 标志设置在 /etc/portage/package.use/ 中。更改 USE 标志后，应使用 emerge --changed-use 重新构建受影响的软件包。

# HISTORY

**euse** 是 **gentoolkit** 的一部分，后者是面向 Gentoo Linux 的管理脚本合集。

# SEE ALSO

[emerge](/man/emerge)(1), [equery](/man/equery)(1), [eselect](/man/eselect)(1)
