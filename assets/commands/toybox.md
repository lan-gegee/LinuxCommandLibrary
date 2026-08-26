# TAGLINE

多用途 Unix 命令行工具箱

# TLDR

**列出**所有命令

```toybox```

显式运行**命令**

```toybox [command] [arguments]```

**列出**文件

```toybox ls```

**删除**文件

```toybox rm [path/to/file]```

显示命令的**帮助**

```toybox [command] --help```

显示**版本**

```toybox --version```

# SYNOPSIS

**toybox** [_COMMAND_ [_ARGS_...]]

# PARAMETERS

**--help**
> 显示某个命令的帮助。

**--version**
> 显示版本信息。

**--long**
> 列出各命令及其建议的安装路径。

**--install** _dir_
> 在 _dir_ 中为每个内置命令创建符号链接。

# DESCRIPTION

**toybox** 是一个多用途工具，将许多标准 Unix 实用程序组合进单个可执行文件中。它提供 ls、rm、cp 等常见命令以及其他众多命令的轻量实现。

Toybox 常用于 Android 和嵌入式 Linux 系统，在这些场景中减小二进制体积非常重要。不带参数运行 toybox 会列出所有可用的内置命令。

# CAVEATS

某些命令的功能可能少于完整的 GNU 实现。可用命令取决于构建配置。主要面向嵌入式系统和 Android 设计。

# HISTORY

**toybox** 由 **Rob Landley** 创建，是 BusyBox 的 BSD 许可替代品。它取代了旧的 Toolbox 实现，成为 Android 中的标准命令行工具箱。

# INSTALL

```apt: sudo apt install toybox```

```nix: nix profile install nixpkgs#toybox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[busybox](/man/busybox)(1)
