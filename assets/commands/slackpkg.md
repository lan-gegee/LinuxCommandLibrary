# TAGLINE

自动化的 Slackware 软件包管理工具

# TLDR

从镜像源**更新软件包列表**

```slackpkg update```

**搜索软件包**

```slackpkg search [package_name]```

**安装软件包**

```slackpkg install [package_name]```

**升级软件包**

```slackpkg upgrade [package_name]```

**升级所有已安装的软件包**

```slackpkg upgrade-all```

**移除软件包**

```slackpkg remove [package_name]```

**安装系统初装后新增的软件包**

```slackpkg install-new```

**清理系统中的非官方软件包**

```slackpkg clean-system```

# SYNOPSIS

**slackpkg** [_OPTIONS_] _action_ [_PACKAGE|PATTERN|FILE_]

# PARAMETERS

**update**
> 从镜像源下载并更新软件包列表

**update gpg**
> 更新用于软件包验证的 GPG 密钥

**install** _package_
> 安装指定的软件包

**upgrade** _package_
> 升级指定的软件包

**upgrade-all**
> 将所有已安装的软件包升级到最新版本

**remove** _package_
> 移除指定的软件包

**reinstall** _package_
> 重新安装指定的软件包

**search** _pattern_
> 搜索匹配模式的软件包

**file-search** _file_
> 搜索包含指定文件的软件包

**info** _package_
> 显示软件包信息

**install-new**
> 安装 Slackware 初装之后新增的软件包

**clean-system**
> 移除不属于官方 Slackware 发行版的软件包

**blacklist** _package_
> 将软件包加入黑名单

**new-config**
> 查找并合并新的配置文件

# DESCRIPTION

**slackpkg** 是一个通过网络管理 Slackware 软件包的自动化工具。它可以从官方 Slackware 镜像源下载、安装、升级和移除软件包。

使用前，需要在 **/etc/slackpkg/mirrors** 中取消注释一个镜像条目以完成配置。运行 **slackpkg update** 下载软件包列表。/etc/slackpkg/blacklist 中的黑名单功能可防止特定软件包被修改。

slackpkg 同时提供基于菜单的界面和命令行界面。在 /etc/slackpkg/slackpkg.conf 中设置 DIALOG=off 可切换为纯控制台操作。

# CONFIGURATION

**/etc/slackpkg/mirrors**
> 镜像列表文件；取消注释恰好一个镜像 URL 作为软件包来源。

**/etc/slackpkg/blacklist**
> 在安装、升级和移除操作中排除在外的软件包列表。

**/etc/slackpkg/slackpkg.conf**
> 主配置文件，包含对话框模式、代理设置和下载选项。

# CAVEATS

同一时间只能启用一个镜像。slackpkg 只管理官方 Slackware 软件包；第三方仓库请使用 **slackpkg+**。**clean-system** 命令会移除所有非官方软件包，请谨慎使用。

# HISTORY

slackpkg 的诞生是为 Slackware Linux 提供基于网络的软件包管理。此前该发行版传统上依赖 installpkg、upgradepkg 和 removepkg 进行手动软件包管理。

# SEE ALSO

[sbopkg](/man/sbopkg)(8), [installpkg](/man/installpkg)(8), [upgradepkg](/man/upgradepkg)(8), [removepkg](/man/removepkg)(8)
