# TAGLINE

查询软件包元数据

# TLDR

**搜索软件包**

```mamba repoquery search [package]```

**显示软件包的依赖**

```mamba repoquery depends [package]```

**显示哪些软件包依赖于它**

```mamba repoquery whoneeds [package]```

**显示软件包信息**

```mamba repoquery info [package]```

**查询已安装的软件包**

```mamba repoquery search --installed [pattern]```

# SYNOPSIS

**mamba repoquery** _command_ [_options_] _query_

# PARAMETERS

_COMMAND_
> 查询类型。

_QUERY_
> 软件包名称或模式。

**search**
> 搜索软件包。

**depends**
> 显示依赖。

**whoneeds**
> 显示反向依赖。

**info**
> 软件包信息。

**--installed**
> 仅查询已安装的软件包。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mamba repoquery** 用于查询软件包元数据。它可以显示依赖和反向依赖关系。

该工具有助于理解软件包之间的关系。比 conda search 更快。

# CAVEATS

属于 mamba 的一部分。仓库必须已建立索引。使用 conda 频道（channel）。

# HISTORY

mamba repoquery 使用 **mamba** 优化过的 C++ 后端提供快速的软件包查询。

# INSTALL

```dnf: sudo dnf install mamba```

```nix: nix profile install nixpkgs#mamba```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mamba](/man/mamba)(1), [conda](/man/conda)(1)
