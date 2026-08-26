# TAGLINE

快速、可直接替代 conda 的软件包管理器

# TLDR

**创建环境**

```mamba create -n [myenv] [python=3.10]```

**安装软件包**

```mamba install [numpy]```

**更新软件包**

```mamba update [package]```

**移除软件包**

```mamba remove [package]```

**搜索软件包**

```mamba search [numpy]```

**列出环境**

```mamba env list```

**激活环境**

```mamba activate [myenv]```

**清理软件包缓存**

```mamba clean --all```

# SYNOPSIS

**mamba** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的操作。

**create**
> 创建新环境。

**install**
> 安装软件包。

**update**
> 更新软件包。

**remove**
> 移除软件包。

**search**
> 在已配置的频道中搜索软件包。

**list**
> 列出当前环境中的软件包。

**clean**
> 移除缓存的软件包文件和无用的缓存。

**env**
> 环境管理。

**repoquery**
> 查询软件包的依赖和反向依赖。

**-n** _NAME_
> 环境名称。

**-c** _CHANNEL_
> 用于搜索软件包的额外频道。

**-y**, **--yes**
> 不请求确认。

**--dry-run**
> 只显示将要执行的操作。

**--no-banner**
> 不显示 mamba 横幅。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mamba** 是一个可无缝替代 **conda** 的快速工具。它使用 **libsolv** 依赖求解器（用 C++ 编写）实现更快的软件包解析，并支持并行下载软件包。

该工具与 conda 的命令、软件包和环境完全兼容。凡是用到 conda 的地方都可以使用它，且支持相同的命令行接口。

# CAVEATS

与 conda 兼容，但在个别边界情况的依赖解析上可能存在细微差异。需要已有的 conda 安装（mamba 以 conda 插件形式运行）。如需独立版本，请参见 **micromamba**。

# HISTORY

mamba 由 **QuantStack** 创建，旨在提供比 conda 更快的软件包管理。

# INSTALL

```dnf: sudo dnf install mamba```

```nix: nix profile install nixpkgs#mamba```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [micromamba](/man/micromamba)(1), [pip](/man/pip)(1)
