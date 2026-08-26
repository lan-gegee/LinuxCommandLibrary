# TAGLINE

Thunderbolt 设备管理守护进程

# TLDR

**启动 bolt 守护进程**

```boltd```

以前台方式**启动**并输出调试信息

```boltd --replace```

**查看 bolt 守护进程版本**

```boltctl --version```

**列出已连接的 Thunderbolt 设备**

```boltctl list```

**授权一台设备**

```boltctl authorize [device_uuid]```

# SYNOPSIS

**boltd** [_options_]

# DESCRIPTION

**boltd** 是管理 Linux 上 Thunderbolt 3 和 USB4 设备的系统守护进程。它负责设备授权和安全策略，并存储已知设备的信息，以便重新连接时自动授权。

Thunderbolt 安全级别从允许所有连接到要求对每台设备逐一授权不等。boltd 与内核的 Thunderbolt 子系统交互，并提供用于设备管理的 D-Bus API。

该守护进程通常由 systemd 自动启动。用户通过 **boltctl**（管理 Thunderbolt 设备的命令行界面）与它交互。

# PARAMETERS

**--replace**
> 替换现有的守护进程实例。

**--version**
> 显示版本信息。

# CAVEATS

需要内核提供相应的 Thunderbolt 支持。安全级别在 BIOS/UEFI 中设置，可能限制 boltd 能授权的范围。设备必须先物理连接才能授权。某些系统可能需要在 BIOS 中启用 Thunderbolt。

# HISTORY

**boltd** 由 **Red Hat** 的 **Christian Kellner** 于 **2017 年**开始开发，旨在为 Linux 提供 Thunderbolt 设备管理。它的诞生源于 Thunderbolt 3 的推出及其要求显式设备授权的安全模型。该项目是 freedesktop.org 生态的一部分，已被主流 Linux 发行版集成。

# SEE ALSO

[boltctl](/man/boltctl)(1), [udevadm](/man/udevadm)(8)
