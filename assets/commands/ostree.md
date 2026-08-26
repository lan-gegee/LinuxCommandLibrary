# TAGLINE

面向二进制文件的版本控制系统，专为管理操作系统根文件系统而优化

# TLDR

**初始化**仓库

```ostree init --repo [path/to/repo]```

为文件创建**提交**（快照）

```ostree commit --repo [path/to/repo] --branch [branch_name]```

**显示**提交中的**文件**

```ostree ls --repo [path/to/repo] [commit_id]```

显示提交的**元数据**

```ostree show --repo [path/to/repo] [commit_id]```

显示**提交列表**（日志）

```ostree log --repo [path/to/repo] [branch_name]```

显示**仓库摘要**

```ostree summary --repo [path/to/repo] --view```

显示可用的 **refs**（分支）

```ostree refs --repo [path/to/repo]```

# SYNOPSIS

**ostree** [_global-options_] _command_ [_command-options_] [_arguments_]

# PARAMETERS

**init**
> 初始化新仓库

**commit**
> 创建新提交

**checkout**
> 将提交检出为目录

**ls**
> 列出提交中的文件

**show**
> 显示提交元数据

**log**
> 显示提交历史

**refs**
> 列出可用的 refs（分支）

**summary**
> 显示或更新仓库摘要

**diff**
> 显示两个提交之间的差异

**cat**
> 显示提交中文件的内容

**prune**
> 查找不可达的对象并删除

**remote**
> 管理远程仓库配置

**pull**
> 从远程仓库拉取

**fsck**
> 检查仓库一致性

**static-delta**
> 管理提交之间的静态增量

**admin**
> 管理系统部署（针对可引导的文件树）

**--repo _path_**
> 仓库路径

**--verbose**
> 启用详细输出

**--version**
> 打印版本并退出

# DESCRIPTION

**ostree** 是一个面向二进制文件的版本控制系统，专为管理操作系统根文件系统而优化。与 git（跟踪文本文件）不同，OSTree 能高效处理 OS 文件树中常见的大型二进制文件和硬链接。

OSTree 是 Fedora Silverblue、Fedora CoreOS 和 Endless OS 等不可变、基于镜像的操作系统的基石。它支持操作系统的原子升级、回滚以及多个并行部署。

该系统使用内容寻址存储（类似 git）并进行去重，因此能高效存储共享大部分文件的多个操作系统版本。

# CAVEATS

仓库格式与 git 不兼容。系统部署（可引导的文件树）需要通过 **ostree admin** 进行额外配置。在去重生效之前，大型提交最初可能占用大量磁盘空间。并非为任意二进制文件设计；针对文件系统树进行了优化。

# HISTORY

OSTree 由 Red Hat 的 Colin Walters 开发，最初服务于 GNOME 的持续集成系统。后来演变为 Fedora 不可变桌面变体和容器导向发行版的基础。

# INSTALL

```apt: sudo apt install ostree```

```dnf: sudo dnf install ostree```

```pacman: sudo pacman -S ostree```

```apk: sudo apk add ostree```

```nix: nix profile install nixpkgs#ostree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpm-ostree](/man/rpm-ostree)(1), [flatpak](/man/flatpak)(1), [podman](/man/podman)(1)
