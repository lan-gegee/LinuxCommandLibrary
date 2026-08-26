# TAGLINE

snap 软件包管理的后台服务

# TLDR

**启动 snapd 服务**

```sudo systemctl start snapd```

**设置 snapd 开机自启**

```sudo systemctl enable snapd```

**检查 snapd 服务状态**

```systemctl status snapd```

**重启 snapd 服务**

```sudo systemctl restart snapd```

**启用经典 snap 支持**（创建符号链接）

```sudo ln -s /var/lib/snapd/snap /snap```

# SYNOPSIS

**snapd** [_--version_]

# DESCRIPTION

**snapd** 是在 Linux 系统上管理 snap 软件包的后台服务。它通过 REST API 接口处理 snap 的安装、更新、移除和安全沙箱。

Snap 是捆绑了全部依赖的自包含应用软件包，可实现跨发行版兼容。该守护进程每天自动检查四次更新，并在后台完成更新。

snapd 使用 AppArmor 和 seccomp 强制执行应用程序沙箱，居中调解 snap 与宿主系统之间的访问。用户通过 **snap** 命令行客户端与 snapd 交互。

必须先运行此服务，才能执行任何 snap 操作。

# CAVEATS

经典 snap 支持需要一个从 /snap 到 /var/lib/snapd/snap 的符号链接。在启用 SELinux 的系统（如 Fedora）上，由于 AppArmor 和 SELinux 无法同时完全生效，snap 沙箱功能会降级。由于捆绑依赖，Snap 可能比传统软件包占用更多磁盘空间。

# HISTORY

Snap 由 **Canonical** 作为 Ubuntu 的一部分开发，首次出现于 **Ubuntu 16.04**（2016 年）。最初名为 Snappy，其设计目标是提供跨发行版行为一致且自动更新的通用 Linux 软件包。

# INSTALL

```dnf: sudo dnf install snapd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snap](/man/snap)(8), [flatpak](/man/flatpak)(1), [apparmor](/man/apparmor)(7)
