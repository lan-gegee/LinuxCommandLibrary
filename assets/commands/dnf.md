# TAGLINE

Fedora/RHEL 软件包管理器

# TLDR

将已安装的软件包**升级**到最新版本

```sudo dnf upgrade```

按关键字**搜索**软件包

```dnf search [keyword]```

显示软件包的**详细信息**

```dnf info [package]```

**安装**新软件包

```sudo dnf install [package]```

**移除**软件包

```sudo dnf remove [package]```

列出**已安装的**软件包

```dnf list --installed```

查找哪个软件包**提供**某个命令

```dnf provides [command]```

**清理**缓存数据

```sudo dnf clean all```

# SYNOPSIS

**dnf** [_options_] _command_ [_arguments_]

# DESCRIPTION

**dnf**（Dandified YUM）是 Fedora、RHEL 及相关发行版的软件包管理器。自 Fedora 22 起成为默认，DNF5 则在 Fedora 41+ 成为默认。它是 YUM 的后继者，提供更好的依赖解析、性能和更一致的接口。

# PARAMETERS

**install, in package**
> 安装指定的软件包

**remove, rm package**
> 移除指定的软件包

**upgrade, up**
> 升级所有已安装的软件包

**search, se keyword**
> 搜索匹配关键字的软件包

**info, if package**
> 显示软件包的详细信息

**list, ls**
> 列出软件包（--installed、--available、--updates）

**provides command**
> 查找提供某个文件或命令的软件包

**clean option**
> 清理缓存数据（all、dbcache、expire-cache、metadata、packages）

**repolist**
> 显示已配置的软件仓库

**history**
> 查看事务历史

**autoremove**
> 移除不再需要的软件包

**-y, --assumeyes**
> 自动对所有提示回答 yes

**--refresh**
> 在执行命令前将元数据标记为过期

# CONFIGURATION

**/etc/dnf/dnf.conf**
> DNF 主配置文件，包含软件包管理行为的设置。

**/etc/yum.repos.d/*.repo**
> 定义软件来源的仓库配置文件。

# CAVEATS

DNF5（用于 Fedora 41+）与早期 DNF 版本存在一些差异。请查阅文档了解具体版本差异。

# HISTORY

DNF 作为实验性软件包管理器随 **Fedora 18** 推出，并在 **Fedora 22** 成为默认。DNF5 是一次完全重写，随 Fedora 41 发布。

# INSTALL

```pacman: sudo pacman -S dnf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yum](/man/yum)(8), [rpm](/man/rpm)(8), [apt](/man/apt)(8), [pacman](/man/pacman)(8)
