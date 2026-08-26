# TLDR

# TAGLINE

管理 systemd 可移植服务镜像

# TLDR

**列出**可移植服务镜像

```portablectl list```

**将镜像附加**到系统

```portablectl attach [path/to/image]```

**从系统分离**镜像

```portablectl detach [image_name]```

**查看**镜像元数据

```portablectl inspect [path/to/image]```

检查镜像是否已**附加**

```portablectl is-attached [image_name]```

# SYNOPSIS

**portablectl** [**list**|**attach**|**detach**|**inspect**|**is-attached**] [_options_] [_image_]

# COMMANDS

**list**
> 列出发现的可移植服务镜像

**attach**
> 将镜像附加到系统

**detach**
> 从系统分离镜像

**inspect**
> 显示镜像详情和元数据

**is-attached**
> 检查附加状态

**reattach**
> 分离并重新附加镜像

# PARAMETERS

**--copy _mode_**
> 复制模式：auto、copy、symlink

**--profile _profile_**
> 使用特定的 profile

**--now**
> 立即启动/停止 unit

**--enable**
> 附加后启用 unit

# DESCRIPTION

**portablectl** 用于管理 systemd 可移植服务镜像。可移植服务是一种轻量级的容器替代方案，它将服务及其依赖打包到磁盘镜像中，可以附加到正在运行的系统上。

镜像是自包含的，可以包含多个服务。它们适合在无需完整容器化开销的情况下部署应用。

# CAVEATS

需要 systemd 239 及以上版本。镜像必须遵循可移植服务格式。附加操作需要 root 权限。profile 控制沙箱级别。

# HISTORY

**portablectl** 随 **systemd portable services** 推出，作为一种轻量级容器化方案。它在提供隔离能力的同时保持与 systemd 服务管理器的紧密集成。

# INSTALL

```apt: sudo apt install systemd-container```

```dnf: sudo dnf install systemd-container```

```zypper: sudo zypper install systemd-container```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [machinectl](/man/machinectl)(1), [systemd-nspawn](/man/systemd-nspawn)(1)
