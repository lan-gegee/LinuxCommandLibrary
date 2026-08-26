# TAGLINE

创建并管理 TUN/TAP 虚拟网络接口

# TLDR

显示所有 **TUN/TAP** 设备

```ip tuntap```

创建一个 **TUN** 设备

```sudo ip tuntap add dev [tun0] mode tun```

创建一个 **TAP** 设备

```sudo ip tuntap add dev [tap0] mode tap```

**删除**一个 TUN/TAP 设备

```sudo ip tuntap delete dev [tun0] mode tun```

以指定**所有者**创建设备

```sudo ip tuntap add dev [tun0] mode tun user [username]```

以**所有者和组**创建设备

```sudo ip tuntap add dev [tun0] mode tun user [username] group [groupname]```

# SYNOPSIS

**ip tuntap** [_command_] [_options_]

# PARAMETERS

**add** **dev** _NAME_ **mode** _MODE_
> 创建 TUN 或 TAP 设备。

**delete** **dev** _NAME_ **mode** _MODE_
> 删除 TUN 或 TAP 设备。

**show** | **list**
> 列出现有的 TUN/TAP 设备。

**mode** _tun|tap_
> 设备模式：tun（第 3 层，IP 数据包）或 tap（第 2 层，以太网帧）。

**user** _USERNAME_
> 按用户名或 UID 设置设备所有者。

**group** _GROUPNAME_
> 按名称或 GID 设置设备组。

**one_queue**
> 使用旧的单队列 TUN/TAP 驱动。

**pi**
> 启用包信息（在每个数据包前附加 4 字节头部）。

**vnet_hdr**
> 包含 virtio-net 头部（与 vhost-net 配合使用）。

**multi_queue**
> 创建多队列 TUN/TAP 设备。

# DESCRIPTION

**ip tuntap** 创建并管理 TUN/TAP 虚拟网络接口。TUN 设备工作在第 3 层（IP 数据包），而 TAP 设备工作在第 2 层（以太网帧）。

这些虚拟接口常被 VPN 软件、虚拟化（QEMU/KVM）和网络测试工具使用。设置 user/group 所有者后，非 root 进程也可以使用该设备。

# CAVEATS

创建设备需要 root 权限。设备会一直存在，直到被删除或重启。使用该设备的应用程序必须配置为匹配的设备名。add 和 delete 操作的模式必须一致。

# HISTORY

TUN/TAP 支持自 Linux 内核 2.4 版本起就已存在。ip tuntap 命令为管理这些设备提供了现代接口，取代了通过 openvpn 或 tunctl 的旧方法。

# SEE ALSO

[ip](/man/ip)(8), [ip-link](/man/ip-link)(8), [openvpn](/man/openvpn)(8)
