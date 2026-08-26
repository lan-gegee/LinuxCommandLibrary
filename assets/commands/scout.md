# TAGLINE

在 openSUSE 上按二进制文件、模块等属性搜索软件包

# TLDR

**在可用软件包中搜索二进制文件**

```scout bin [command_name]```

**搜索 Java 类**

```scout java [class_name]```

**搜索 autoconf 宏**

```scout autoconf [macro_name]```

**搜索 Python 模块**

```scout python [module_name]```

**使用指定软件仓库搜索**

```scout -r [repo_name] bin [command_name]```

# SYNOPSIS

**scout** [_module_] [_options_] [_search_term_]

# PARAMETERS

**bin**
> 在软件包中搜索二进制文件/可执行文件

**java**
> 在软件包中搜索 Java 类

**python**
> 在软件包中搜索 Python 模块

**autoconf**
> 在软件包中搜索 autoconf 宏

**-r** _repo_, **--repo**=_repo_
> 指定要搜索的软件仓库（默认：zypp）

**-p**, **--package**
> 仅显示软件包名称

**-l**, **--listrepos**
> 列出可用的软件仓库

# DESCRIPTION

**Scout** 是一款 openSUSE 命令行实用程序，用于按二进制文件、Java 类、Python 模块、autoconf 宏等各种属性搜索软件包。bash 和 zsh 中的 "command-not-found" 功能就由它驱动。

当你输入未知命令时，shell 会自动调用 scout 查找提供该命令的软件包，并建议通过 zypper 安装。Scout 搜索软件包索引，无需安装相应软件包。

该工具与 zypp 软件包管理系统集成，可以查询多个软件仓库。

# CAVEATS

Scout 依赖预先构建的索引，其中可能未包含所有软件包或最新添加的内容。在 openSUSE 系统上，command-not-found 处理器会在 bash 和 zsh 中自动启用。

# HISTORY

Scout 由 **openSUSE** 项目开发，用于在用户输入未安装的命令时提供有用的提示。在较新的 openSUSE 发行版中，它已由 **cnf**（command-not-found）接替。

# INSTALL

```apt: sudo apt install openafs-client```

```nix: nix profile install nixpkgs#scout```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zypper](/man/zypper)(8), [pkgfile](/man/pkgfile)(1), [apt-file](/man/apt-file)(1)
