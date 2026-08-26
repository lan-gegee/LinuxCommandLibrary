# TAGLINE

Solus Linux 的软件包管理器

# TLDR

**刷新并升级**所有已安装的软件包

```sudo eopkg upgrade```

**安装**一个或多个软件包

```sudo eopkg install [package]```

**搜索**软件仓库索引

```sudo eopkg search [search_term]```

# SYNOPSIS

**eopkg** _command_ [_options_] [_packages_]

# DESCRIPTION

**eopkg** 是独立发行版 Solus Linux 的软件包管理器。它使用 .eopkg 软件包格式，负责软件包管理的所有环节，包括安装、更新、移除和仓库管理。

该工具由最初为 Pardus Linux 开发的 PiSi 软件包管理器演化而来，并针对 Solus 做了大量改进与优化。eopkg 提供依赖解析和软件包回滚能力，并维护已安装软件包的本地数据库。它融入 Solus 的滚动发布模型，在保持系统稳定的同时提供持续更新。

# PARAMETERS

**install** _packages_
> 安装软件包（短别名：**it**）

**upgrade**
> 更新所有软件包（短别名：**up**）

**search** _term_
> 搜索软件包（短别名：**sr**）

**remove** _packages_
> 移除软件包（短别名：**rm**）

**info** _package_
> 显示软件包信息

**list-installed**
> 列出已安装的软件包（短别名：**li**）

**list-available**
> 列出软件仓库中可用的软件包（短别名：**la**）

**update-repo**
> 刷新软件仓库索引的本地副本（短别名：**ur**）

**history**
> 显示事务历史

**history -t** _number_
> 将系统回滚到之前某次事务

**check** _package_
> 校验已安装文件的完整性

# CAVEATS

Solus Linux 专属。与其他发行版不兼容。多数操作需要 root 权限。若索引可能过期，请先执行 `eopkg update-repo` 再安装或升级。

# SEE ALSO

[apt](/man/apt)(8), [dnf](/man/dnf)(8), [pacman](/man/pacman)(8)

# RESOURCES

```[Source code](https://github.com/getsolus/eopkg)```

```[Homepage](https://getsol.us/)```

```[Documentation](https://help.getsol.us/docs/user/package-management/basics)```

<!-- verified: 2026-07-14 -->
