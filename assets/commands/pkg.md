# TAGLINE

FreeBSD 二进制软件包管理器

# TLDR

**安装软件包**

```pkg install [package]```

**搜索软件包**

```pkg search [query]```

**更新软件仓库目录**

```pkg update```

**升级所有已安装的软件包**

```pkg upgrade```

**删除软件包**

```pkg delete [package]```

**列出所有已安装的软件包**

```pkg info```

**显示特定已安装软件包的详细信息**

```pkg info [package]```

**审计已安装软件包的安全漏洞**

```pkg audit -F```

**锁定软件包以防止升级**

```pkg lock [package]```

# SYNOPSIS

**pkg** [_command_] [_options_] [_package_...]

# PARAMETERS

**install** _PACKAGE_
> 安装软件包及其依赖。

**search** _QUERY_
> 在远程软件仓库中搜索软件包。

**update**
> 更新远程仓库目录。

**upgrade**
> 将已安装的软件包升级到最新的可用版本。

**delete** _PACKAGE_
> 删除软件包。

**info** [_PACKAGE_]
> 显示已安装软件包的信息，或特定软件包的详细信息。

**audit** [**-F**]
> 审计已安装软件包的已知安全漏洞。-F 会获取最新的数据库。

**lock** _PACKAGE_
> 锁定软件包以防止修改或删除。

**unlock** _PACKAGE_
> 解锁之前锁定的软件包。

**autoremove**
> 移除作为依赖安装的无用软件包。

**query** _FORMAT_ [_PACKAGE_]
> 使用格式字符串查询已安装软件包的信息。

**clean**
> 清理已下载软件包的本地缓存。

# DESCRIPTION

**pkg** 是 FreeBSD 的官方二进制软件包管理器。它负责从 FreeBSD 软件仓库安装、删除、升级和搜索预构建的软件包，取代了较旧的 pkg_add 工具。

该工具会自动解析依赖关系，管理本地软件包数据库，并支持多个软件仓库。它还可以锁定软件包以防止升级、审计已安装软件包的安全漏洞，以及从已安装的 ports 创建软件包。

# CONFIGURATION

**/usr/local/etc/pkg.conf**
> 控制 pkg 行为和默认设置的主配置文件。

**/usr/local/etc/pkg/repos/**
> 仓库配置目录，包含各仓库的 .conf 文件。

# CAVEATS

仅适用于 FreeBSD。安装需要 root 权限。基于软件仓库运作。

# HISTORY

pkg 取代 pkg_add 成为 **FreeBSD 的软件包管理器**。

# INSTALL

```nix: nix profile install nixpkgs#pkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pkg-add](/man/pkg-add)(8), [ports](/man/ports)(7)
