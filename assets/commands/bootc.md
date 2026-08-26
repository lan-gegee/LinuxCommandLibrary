# TAGLINE

基于容器镜像的事务性操作系统更新

# TLDR

按引导加载程序顺序显示**部署**

```bootc status```

检查**是否有可用更新**

```bootc upgrade --check```

准备新的**更新并重启**

```bootc upgrade --apply```

将 **OS 基础**更换为新容器镜像

```bootc switch [image]```

**重启**进入先前的部署

```bootc rollback```

以事务方式应用**配置更改**

```bootc edit```

**安装到目标块设备**

```bootc install to-disk --target-no-signature-verification [/dev/sda]```

**以 JSON 格式显示状态**

```bootc status --format json```

# SYNOPSIS

**bootc** _command_ [_options_]

# DESCRIPTION

**bootc** 使用 OCI/Docker 容器镜像管理事务性的就地操作系统更新。它实现原子化的系统升级：整个 OS 在启动时被替换为新的容器镜像。

该工具适用于基于镜像的 Linux 发行版（如 Fedora CoreOS 和 RHEL），并在更新引发问题时提供回滚能力。它构建于 OSTree 之上以实现原子化部署，并使用标准容器镜像仓库分发镜像。

# SUBCOMMANDS

**status**
> 显示当前部署及其在引导加载程序中的顺序。

**upgrade**
> 获取并暂存新版本的操作系统。

**switch**
> 切换到另一个容器镜像。

**rollback**
> 回退到上一个 OS 部署。

**edit**
> 以事务方式应用配置更改。

**install to-disk**
> 将容器镜像安装到目标块设备。

**install to-filesystem**
> 安装到现有文件系统（支持 LVM、LUKS、RAID）。

# PARAMETERS

**--check**
> 只检查更新而不应用（与 upgrade 配合使用）。

**--apply**
> 应用升级并重启（与 upgrade 配合使用）。

**--format** _FORMAT_
> status 的输出格式：json 或 yaml。

**--quiet**
> 不显示非错误输出。

# CAVEATS

仅适用于为 bootc 设计的系统（基于镜像的 Linux 发行版）。对根文件系统的更改会丢失，除非使用配置管理。需要容器镜像基础设施。

# HISTORY

**bootc** 是日益壮大的基于镜像的 Linux 系统生态的一部分，构建在 OSTree 和容器镜像等技术之上。它代表了由 CoreOS 等项目开创的现代系统更新方式。它在 **containers** GitHub 组织下开发，已成为 RHEL 镜像模式的关键组件。

# INSTALL

```dnf: sudo dnf install bootc```

```nix: nix profile install nixpkgs#bootc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bootc-switch](/man/bootc-switch)(1), [rpm-ostree](/man/rpm-ostree)(1), [podman](/man/podman)(1), [skopeo](/man/skopeo)(1), [ostree](/man/ostree)(1)
