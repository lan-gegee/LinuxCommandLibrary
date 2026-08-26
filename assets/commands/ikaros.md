# TAGLINE

Vanilla OS 的驱动管理工具

# TLDR

为设备**交互式安装**驱动

```ikaros install [device]```

**自动安装**推荐的驱动

```ikaros auto-install [device]```

**列出**所有设备

```ikaros list-devices```

# SYNOPSIS

**ikaros** _command_ [_arguments_]

# PARAMETERS

**install** _DEVICE_
> 交互式地为指定设备安装驱动

**auto-install** _DEVICE_
> 自动为该设备安装推荐的驱动

**list-devices**
> 列出所有检测到的可能需要驱动的设备

# DESCRIPTION

**ikaros** 是 Vanilla OS 的驱动管理工具。它检测硬件设备并帮助安装合适的驱动，简化了在 Linux 上查找和安装设备驱动这一往往复杂的过程。

该工具既可以引导用户交互式选择驱动，也可以根据检测到的硬件自动安装推荐的驱动。

# CAVEATS

仅适用于 Vanilla OS 及其软件包管理系统。设备支持情况取决于仓库中可用的驱动。某些专有驱动可能需要额外配置。

# HISTORY

Ikaros 是 Vanilla OS 项目的一部分，后者是一个于 **2022 年**发布的不可变（immutable）Linux 发行版。该工具提供了一种在 Vanilla OS 环境中管理驱动的友好方式。

# SEE ALSO

[apx](/man/apx)(1), [ubuntu-drivers](/man/ubuntu-drivers)(1)
