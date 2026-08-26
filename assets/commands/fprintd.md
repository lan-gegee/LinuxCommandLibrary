# TAGLINE

D-Bus 指纹认证服务

# TLDR

指纹录入与匹配由拆分的工具完成 —— 列出**已录入**的指纹

```fprintd-list [username]```

**录入**新指纹

```fprintd-enroll [username]```

**验证**手指是否与已录入数据匹配

```fprintd-verify [username]```

**删除**已录入的指纹

```fprintd-delete [username]```

# SYNOPSIS

**fprintd** 是一个 D-Bus 守护进程，不是独立命令。请使用相关的客户端命令。

# DESCRIPTION

**fprintd** 是通过 D-Bus 提供指纹扫描功能的指纹守护进程。它作为系统服务管理指纹读取器和已录入的指纹数据，让应用程序能够通过指纹认证用户。

守护进程本身在后台运行，通常由 systemd 启动。用户通过客户端工具与其交互：

**fprintd-enroll** - 录入新指纹
**fprintd-list** - 列出已录入的指纹
**fprintd-verify** - 验证指纹
**fprintd-delete** - 删除已录入的指纹

与 PAM 的集成让指纹认证可用于登录、sudo 以及其他系统认证环节。

# CAVEATS

需要 libfprint 支持的兼容指纹读取器。并非所有读取器都能可靠工作。指纹数据存储在 **/var/lib/fprint** 中，应妥善保护。要与系统认证集成需要进行 PAM 配置。

# HISTORY

fprintd 是 fprint 项目的一部分，该项目为 Linux 提供指纹读取器支持。项目的目标是把标准化的指纹认证带入 Linux 系统，并利用 libfprint 库实现硬件抽象。

# INSTALL

```dnf: sudo dnf install fprintd```

```pacman: sudo pacman -S fprintd```

```zypper: sudo zypper install fprintd```

```nix: nix profile install nixpkgs#fprintd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fprintd-enroll](/man/fprintd-enroll)(1), [fprintd-list](/man/fprintd-list)(1), [fprintd-verify](/man/fprintd-verify)(1), [fprintd-delete](/man/fprintd-delete)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/libfprint/fprintd)```

```[Homepage](https://fprint.freedesktop.org/)```

<!-- verified: 2026-07-15 -->
