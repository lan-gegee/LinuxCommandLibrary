# TAGLINE

基于 Nix 构建的可复现开发环境

# TLDR

**初始化环境**

```flox init```

**安装软件包**

```flox install [ripgrep]```

**激活环境**

```flox activate```

**搜索软件包**

```flox search [nodejs]```

**列出已安装的软件包**

```flox list```

# SYNOPSIS

**flox** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 操作类型：init、install、activate、search、list 等。

**init**
> 初始化新环境。

**install** _PACKAGES_
> 安装软件包。

**activate**
> 进入环境 Shell。

**search** _QUERY_
> 搜索软件包。

**list**
> 显示已安装的软件包。

**uninstall** _PACKAGES_
> 移除软件包。

**push**
> 发布环境。

**--help**
> 显示帮助信息。

# DESCRIPTION

**flox** 是一款构建在 Nix 之上的虚拟环境管理器。它通过声明式软件包管理创建可复现的开发环境，可在不同机器和团队之间共享。

环境在一个清单文件中定义，可以推送到 FloxHub 进行共享。与传统虚拟环境不同，flox 可以处理 Nix 软件集合中的任何语言或工具。

flox 简化了 Nix 的复杂性，同时保留了其可复现性保证。

# CAVEATS

需要安装 Nix。Nix 存储的初次下载量较大。某些软件包可能不可用。

# HISTORY

flox 的创建目的是让主流开发者也能用上 **Nix**。它以熟悉的虚拟环境工作流为基础，背后是 Nix 可复现的软件包管理。

# SEE ALSO

[nix](/man/nix)(1), [direnv](/man/direnv)(1)
