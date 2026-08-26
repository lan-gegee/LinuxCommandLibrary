# TAGLINE

支持容器化子系统的软件包管理器

# TLDR

查看管理**软件包管理器**的文档

```apx pkgmanagers --help```

查看管理**栈**的文档

```apx stacks --help```

查看管理**子系统**的文档

```apx subsystems --help```

**进入**子系统 Shell

```apx [subsystem] enter```

在子系统中**安装**软件包

```apx [subsystem] install [package]```

在子系统中**运行**命令

```apx [subsystem] run [command]```

将应用从子系统**导出**到主机

```apx [subsystem] export --app [application]```

# SYNOPSIS

**apx** [_subsystem_] _command_ [_options_]

# DESCRIPTION

**apx** 是 Vanilla OS 的软件包管理工具，通过容器化子系统支持多种软件来源。它允许从不同的 Linux 发行版（Debian、Fedora、Arch 等）安装软件包，而不影响主机系统。

软件包安装在基于 Podman 容器的隔离子系统中。应用可以导出到主机系统并与桌面环境集成，同时保持与不可变主机操作系统的分离。

# SUBCOMMANDS

**pkgmanagers**
> 管理软件包管理器配置

**stacks**
> 管理栈配置（基础镜像和软件包管理器）

**subsystems**
> 管理子系统（容器环境）

**enter**
> 进入子系统的 Shell

**install**
> 在子系统中安装软件包

**remove**
> 从子系统中删除软件包

**run**
> 在子系统中运行命令

**search**
> 在子系统中搜索软件包

**update**
> 更新子系统中可用软件包的列表

**upgrade**
> 升级子系统中已安装的软件包

**export**
> 将应用或二进制文件从子系统导出到主机系统

**unexport**
> 移除先前导出的应用或二进制文件

# CONFIGURATION

**/etc/apx/apx.json**
> 系统级配置，定义容器存储路径、apnx 存储路径和默认栈设置。

**~/.local/share/apx/**
> 每用户目录，包含栈、子系统和软件包管理器配置。

# CAVEATS

需要 Podman 进行容器管理。首次创建子系统会下载可能较大的容器镜像。导出的应用在容器内运行，可能有轻微的性能开销。

# HISTORY

**apx** 作为 Vanilla OS 的一部分开发，该不可变 Linux 发行版于 **2022** 年首次发布。它提供了一种新颖的软件包管理方式，在保持系统不可变性的同时，允许用户从多个 Linux 生态系统安装软件。

# INSTALL

```dnf: sudo dnf install apx```

```aur: yay -S apx```

```nix: nix profile install nixpkgs#apx```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apx-pkgmanagers](/man/apx-pkgmanagers)(1), [apx-stacks](/man/apx-stacks)(1), [apx-subsystems](/man/apx-subsystems)(1), [podman](/man/podman)(1)

# RESOURCES

```[Source code](https://github.com/Vanilla-OS/apx)```

```[Homepage](https://apx.vanillaos.org/)```

```[Documentation](https://docs.vanillaos.org/docs/en/apx)```

<!-- verified: 2026-06-11 -->
