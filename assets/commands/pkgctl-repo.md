# TAGLINE

管理 Arch Linux Git 打包仓库

# TLDR

**克隆**软件包仓库（需要在 Arch Linux GitLab 中配置 SSH 密钥）

```pkgctl repo clone [pkgname]```

通过 **HTTPS** 克隆软件包仓库

```pkgctl repo clone --protocol https [pkgname]```

**创建**新的 GitLab 软件包仓库并克隆

```pkgctl repo create [pkgbase]```

**切换**软件包仓库到指定版本

```pkgctl repo switch [version] [pkgbase]```

**打开**软件包仓库的网站

```pkgctl repo web [pkgbase]```

# SYNOPSIS

**pkgctl repo** _command_ [_options_] [_package_]

# PARAMETERS

**clone**
> 克隆软件包仓库

**create**
> 创建新的 GitLab 仓库

**switch**
> 切换到特定版本/分支

**web**
> 在网页浏览器中打开仓库

**--protocol _proto_**
> 克隆协议：ssh（默认）或 https

**--maintainer _name_**
> 按维护者过滤

**--universe**
> 从 universe（community）而非 packages 克隆

# DESCRIPTION

**pkgctl repo** 管理托管在 GitLab 上的 Arch Linux 软件包的 Git 打包仓库。它提供克隆、创建和管理软件包源码仓库的命令。

该工具与 Arch Linux 位于 gitlab.archlinux.org 的 GitLab 基础设施集成，官方软件包源码就维护在那里。SSH 访问需要在你的 GitLab 账户中配置密钥。

软件包维护者用它获取源码以更新软件包，而只读的 HTTPS 访问允许任何人查看软件包的构建文件。

# CAVEATS

SSH 克隆需要有配置 SSH 密钥的 GitLab 账户。创建仓库需要有效的 GitLab API 身份验证和相应权限。属于面向 Arch Linux 开发的 pkgctl 工具集。

# SEE ALSO

[pkgctl](/man/pkgctl)(1), [pkgctl-build](/man/pkgctl-build)(1), [git](/man/git)(1), [asp](/man/asp)(1)
