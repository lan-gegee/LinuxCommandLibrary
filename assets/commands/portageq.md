# TAGLINE

查询 Gentoo Portage 软件包数据库

# TLDR

显示 **Portage 环境变量**的值

```portageq envvar [VARIABLE]```

显示**软件仓库**配置

```portageq repos_config /```

按**优先级**列出软件仓库

```portageq get_repos /```

检查**软件包是否已安装**

```portageq has_version / [category]/[package]```

查找软件包的**最佳可见版本**

```portageq best_visible / ebuild [category]/[package]```

查询软件包**元数据**

```portageq metadata / ebuild [category]/[package] [DEPEND]```

# SYNOPSIS

**portageq** _command_ [_root_] [_arguments_...]

# COMMANDS

**envvar**
> 显示 Portage 环境变量

**repos_config**
> 显示详细的软件仓库配置

**get_repos**
> 按优先级列出软件仓库

**metadata**
> 查询软件包元数据

**best_visible**
> 查找最佳的可见软件包版本

**match**
> 查找匹配 atom 的软件包

**has_version**
> 检查软件包是否已安装。为真返回 0，否则返回 1。

**best_version**
> 返回已安装的最高匹配 category/package-version。

**owners**
> 查询文件或目录属于哪个软件包。

# PARAMETERS

**root**
> 查询所用的根目录（通常是 /）

**variable**
> 环境变量名

**category/package**
> 查询用的软件包 atom

# DESCRIPTION

**portageq** 在 Gentoo Linux 上查询 Portage 配置和软件包数据库。它提供对 Portage 内部数据的编程访问，适用于脚本和构建自动化。

该工具可以获取环境变量、仓库信息和详细的软件包元数据，而无需直接解析配置文件。

# CAVEATS

Gentoo 专属工具。有些查询要求软件包已安装。大多数命令需要 root 参数。输出格式因命令而异。

# HISTORY

**portageq** 是 Gentoo 软件包管理系统 **Portage** 的组成部分。它为脚本提供稳定的查询接口，避免直接解析 Portage 复杂的配置。

# SEE ALSO

[emerge](/man/emerge)(1), [equery](/man/equery)(1), [eix](/man/eix)(1)
