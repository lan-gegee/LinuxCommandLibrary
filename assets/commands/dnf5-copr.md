# TAGLINE

用 DNF5 管理 Copr 软件仓库

# TLDR

**启用** Copr 仓库

```sudo dnf5 copr enable [owner]/[project]```

为特定 **chroot** 启用 Copr 仓库

```sudo dnf5 copr enable [owner]/[project] [fedora-rawhide-ppc64le]```

从特定 **hub** 启用 Copr 仓库

```sudo dnf5 copr enable [hub]/[owner]/[project]```

**禁用** Copr 仓库

```sudo dnf5 copr disable [owner]/[project]```

**移除** Copr 仓库

```sudo dnf5 copr remove [owner]/[project]```

**列出**已配置的 Copr 仓库

```dnf5 copr list```

打印系统的**调试**信息

```dnf5 copr debug```

# SYNOPSIS

**dnf5 copr** {_list_|_enable_|_disable_|_remove_|_debug_} [_options_] [_project-spec_] [_chroot_]

# PARAMETERS

**list**
> 列出系统上已配置的 Copr 仓库

**enable** _project-spec_ [_chroot_]
> 从 Copr 服务器下载仓库信息并安装为 `/etc/yum.repos.d/*.repo` 文件

**disable** _project-spec_
> 禁用指定的 Copr 仓库（设置 `enabled=0`；保留 `.repo` 文件）

**remove** _project-spec_
> 移除指定的 Copr 仓库及其 `/etc/yum.repos.d/*.repo` 文件

**debug**
> 打印有助于调试的系统信息

**--hub** _hostname_
> Copr hub（Web UI/API 服务器）主机名；默认为 `copr.fedorainfracloud.org`

**project-spec**
> 项目 ID，格式为 `OWNER/PROJECT` 或 `HUB/OWNER/PROJECT`（owner 可以是用户名或 `@@groupname`）

**chroot**
> chroot，采用 `NAME-RELEASE-ARCH` 形式（如 `fedora-rawhide-ppc64le`）；省略时自动检测

# DESCRIPTION

**dnf5 copr** 管理 Fedora 系系统上的 Copr 仓库。Copr（Cool Other Package Repo）托管社区和第三方软件包仓库，一条命令即可启用。

启用项目会在 `/etc/yum.repos.d/` 下安装仓库定义。禁用会保留定义但将其关闭；移除则彻底删除该定义。

# CAVEATS

Copr 项目由用户自行维护，并非 Fedora 官方软件包。启用前请先查看项目页面。错误的 chroot 可能安装为其他发行版或架构构建的软件包。

# HISTORY

**copr** 是面向 Fedora Copr 构建服务的 DNF5 插件，取代了 DNF4 中较旧的 `dnf copr` 插件。

# SEE ALSO

[dnf5](/man/dnf5)(8), [dnf](/man/dnf)(8)

# RESOURCES

```[Source code](https://github.com/rpm-software-management/dnf5)```

```[Documentation](https://dnf5.readthedocs.io/en/latest/dnf5_plugins/copr.8.html)```

<!-- verified: 2026-07-28 -->
