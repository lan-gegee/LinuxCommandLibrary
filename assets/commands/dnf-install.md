# TAGLINE

安装 RPM 软件包

# TLDR

按名称**安装**软件包

```sudo dnf install [package1] [package2]```

从**本地文件**安装

```sudo dnf install [path/to/file]```

从 **URL** 安装

```sudo dnf install [https://example.com/package.rpm]```

添加 **EPEL** 仓库

```sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-[10].noarch.rpm```

添加 **Remi** 仓库

```sudo dnf install https://rpms.remirepo.net/enterprise/remi-release-[8].rpm```

# SYNOPSIS

**dnf install** [_options_] _package_...

# DESCRIPTION

**dnf install** 是在 RHEL、CentOS、Fedora 和 AlmaLinux 等 Red Hat 系发行版上安装软件包的主要命令。它支持从多种来源安装：仓库中的包名、本地 RPM 文件或直接指向 RPM 包的 URL。

该命令自动解析并安装所有必需的依赖，从已配置的仓库中下载。通过 URL 安装通常用于添加第三方仓库（如 EPEL 或 RPM Fusion），方法是安装它们的 release 包。该工具会验证软件包签名并检查冲突，还能处理复杂场景，例如替换软件包或通过 --allowerasing 允许删除冲突的软件包。由于安装会修改系统文件，因此需要 root 权限。

# PARAMETERS

_package_
> 包名、本地文件路径或 URL

**-y, --assumeyes**
> 自动对所有提示回答 yes

**--allowerasing**
> 允许删除冲突的软件包

**--downloadonly**
> 仅下载，不安装

# CAVEATS

需要 root 权限。包名必须与仓库中的名称完全一致。从 URL 安装需要网络连接。

# INSTALL

```pacman: sudo pacman -S dnf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dnf](/man/dnf)(8), [rpm](/man/rpm)(8)
