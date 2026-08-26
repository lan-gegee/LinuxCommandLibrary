# TAGLINE

用于在 Linux 上运行 macOS 软件的翻译层

# TLDR

运行一个**内建命令**

```darling shell [uname]```

带参数运行**指定程序**

```darling shell [path/to/program] [argument1] [argument2]```

打开 **macOS Shell**

```darling shell```

**关闭** Darling 服务

```darling shutdown```

# SYNOPSIS

**darling** _command_ [_arguments_]

# DESCRIPTION

**darling** 是一个翻译层，允许在 Linux 上运行 macOS 软件，类似于 Wine 在 Linux 上运行 Windows 软件、Wine64 运行 64 位 Windows 应用的方式。它将 macOS 系统调用翻译为对应的 Linux 实现，并提供 macOS 框架和库的兼容实现。

该工具在 Linux 内创建一个 macOS 兼容环境，包括 Foundation、CoreFoundation 及其他关键 Apple 框架的实现。应用程序运行在一个前缀（类似 Wine 的 prefix）中，与宿主系统隔离，同时可以访问必要的资源。

**shell** 命令提供在 Darling 环境中运行 macOS 二进制程序和命令的能力。你可以运行单个 macOS 程序、使用 uname 等 macOS 内建工具，或者打开一个行为类似 macOS 终端的交互式 Shell。

Darling 对需要在 Linux 上测试 macOS 应用的开发者，以及想在没有 Apple 硬件的情况下运行特定 macOS 工具的用户尤其有用。

# PARAMETERS

**shell** [_command_]
> 运行一条命令；不带参数时打开交互式 macOS Shell。

**shutdown**
> 停止 Darling 服务并卸载前缀。

**version**
> 打印 Darling 版本。

**help**
> 显示用法信息。

# CAVEATS

并非所有 macOS 软件都兼容。需要 Darling 内核模块。性能可能与原生 macOS 有差异。某些系统特性可能未完整实现。

# HISTORY

**Darling** 是一个开源项目，旨在通过系统调用翻译和提供兼容框架，让 macOS 应用运行在 Linux 上，定位类似 Windows 平台的 Wine。

# SEE ALSO

[wine](/man/wine)(1), [proton](/man/proton)(1)
