# TAGLINE

查询并显示 libalpm 支持的功能特性

# TLDR

列出所有**可用的功能特性**

```paccapability```

检查**指定的功能特性**

```paccapability nls```

检查 **downloader** 功能特性

```paccapability downloader```

检查 **signatures** 功能特性

```paccapability signatures```

显示**帮助**

```paccapability --help```

# SYNOPSIS

**paccapability** [_options_] [_capability_...]

# PARAMETERS

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**paccapability** 查询并显示 libalpm（Arch Linux Package Management 库）所支持的功能特性。它可以列出所有可用特性，或检查是否支持特定特性。

常见的功能特性包括 nls（原生语言支持）、downloader（内置下载支持）和 signatures（软件包签名验证）。

# CAVEATS

可用功能取决于 libalpm 的编译方式。某些特性可能并非在所有系统上都可用。

# HISTORY

属于 **pacutils**，这是一组基于 libalpm 构建、用于 Arch Linux 软件包管理的工具集。

# SEE ALSO

[pacman](/man/pacman)(8), [libalpm](/man/libalpm)(3)
