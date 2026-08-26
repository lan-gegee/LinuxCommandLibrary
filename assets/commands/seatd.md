# TAGLINE

面向 Wayland 的极简 seat 管理守护进程

# TLDR

以默认设置**启动 seatd**

```seatd```

使用指定的套接字路径**启动 seatd**

```seatd -s [/path/to/socket.sock]```

以指定的用户和组属主**启动 seatd**

```seatd -u [user] -g [group]```

以调试日志**启动 seatd**

```seatd -l debug```

在文件描述符上通过 s6 通知**启动 seatd**

```seatd -n [fd]```

# SYNOPSIS

**seatd** [**-h**] [**-v**] [**-n** _fd_] [**-u** _user_] [**-g** _group_] [**-s** _path_] [**-l** _loglevel_]

# PARAMETERS

**-h**
> 显示帮助信息并退出。

**-v**
> 显示版本号并退出。

**-n** _fd_
> 用于就绪通知的文件描述符。当 seatd 准备好处理请求时，会写入一个换行符并关闭该 fd。与 s6 的通知协议兼容。

**-u** _user_
> seatd 套接字的属主用户。

**-g** _group_
> seatd 套接字的属主组。

**-s** _path_
> 创建 seatd 套接字的位置。默认为 `/run/seatd.sock`。

**-l** _loglevel_
> 设置日志详细程度。有效级别为 **debug**、**info**、**error** 或 **silent**。默认为 **error**。

# DESCRIPTION

**seatd** 是一个极简的 seat 管理守护进程，用于在多会话、多 seat 环境中协调对显示器和输入设备等共享资源的访问。它为 Wayland 合成器提供了 elogind 的替代方案，尤其适合基于 wlroots 的合成器。

该守护进程通过 UNIX 域套接字工作，客户端协议由 **libseat** 提供。与 elogind 不同，seatd 只专注于 seat 管理，不包含额外的会话管理功能，因此非常轻量，适合精简的系统配置。

Seat 管理让 Wayland 合成器等应用无需 root 权限即可访问特权设备（显卡、输入设备），在保持功能的同时提高了安全性。

# CONFIGURATION

**SEATD_VTBOUND**
> 设为 "0" 时，seat 将不会绑定到虚拟终端。

# CAVEATS

seatd 需要适当的权限才能访问设备节点。套接字路径必须对需要 seat 管理的客户端可访问。同一时间只能运行一个 seat 管理守护进程。某些合成器可能需要额外配置才能让 libseat 使用 seatd 而非 elogind。

# HISTORY

**seatd** 由 Kenny Levinsen 创建，作为 logind/elogind 所提供 seat 管理功能的极简替代方案。它专为支持 Wayland 合成器而设计，尤其是 Sway 等基于 wlroots 的合成器，且不需要完整的 systemd 或 elogind 栈。随着更多用户寻求在没有 systemd 的系统上运行 Wayland 的轻量级方案，该项目逐渐受到关注。

# INSTALL

```apt: sudo apt install seatd```

```dnf: sudo dnf install seatd```

```pacman: sudo pacman -S seatd```

```apk: sudo apk add seatd```

```zypper: sudo zypper install seatd```

```nix: nix profile install nixpkgs#seatd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1)
