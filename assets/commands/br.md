# TAGLINE

用于交互式目录导航的 Shell 函数

# TLDR

开始**交互式**导航

```br```

显示文件**大小**

```br -s```

显示**隐藏**文件

```br -h```

**仅显示目录**

```br -f```

**安装**或重新安装 br shell 函数

```broot --install```

# SYNOPSIS

**br** [_options_] [_path_]

# DESCRIPTION

**br** 是封装了 **broot** 的 shell 函数，提供交互式目录树导航，并支持更改 shell 的当前工作目录。它是 broot 进行 shell 集成的推荐方式。支持的 shell 有 bash、zsh、fish 和 nushell。

首次运行时，broot 会提议在 shell 配置中注册 **br** 函数。你也可以用 **broot --install** 手动安装，或用 **broot --print-shell-function** _shell_ 打印该函数的定义。

# PARAMETERS

所有可用选项参见 **broot**。常用选项：

**-s, --sizes**
> 显示文件和目录的大小。

**-h, --hidden**
> 显示隐藏文件和目录。

**-f, --only-folders**
> 仅显示目录。

**-p, --permissions**
> 显示文件权限。

# CAVEATS

必须通过 "broot --install" 安装 br 函数才能正确进行 shell 集成。与直接调用 broot 不同，br 允许更改 shell 的当前目录。

# HISTORY

**br** 是 **broot** 的 shell 函数组件，安装后可启用目录导航与 shell 集成功能。

# INSTALL

```apt: sudo apt install bottlerocket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[broot](/man/broot)(1), [tree](/man/tree)(1), [ranger](/man/ranger)(1), [nnn](/man/nnn)(1), [yazi](/man/yazi)(1)

# RESOURCES

```[Source code](https://github.com/Canop/broot)```

```[Homepage](https://dystroy.org/broot/)```

<!-- verified: 2026-06-19 -->
