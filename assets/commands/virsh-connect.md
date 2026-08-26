# TAGLINE

在 virsh shell 中连接或重新连接到 libvirt hypervisor

# TLDR

**重新连接本地 QEMU/KVM 系统守护进程（root 身份）**

```virsh connect qemu:///system```

**连接会话级 QEMU/KVM 守护进程（普通用户身份）**

```virsh connect qemu:///session```

**通过 SSH 连接远程主机**

```virsh connect qemu+ssh://[user]@[host]/system```

**通过 TLS 连接远程主机**

```virsh connect qemu+tls://[host]/system```

**建立只读连接**

```virsh connect qemu:///system --readonly```

# SYNOPSIS

**connect** [_URI_] [_--readonly_]

# PARAMETERS

**--readonly**
> 建立到 hypervisor 的只读连接。将操作限制为非破坏性查询。

# DESCRIPTION

**connect** 是一个 virsh shell 命令，用于建立或重建与 libvirt hypervisor 的连接。virsh shell 启动时会自动执行它，使用命令行 **-c** 标志提供的 URI。在运行中的 virsh 会话内也可以交互式地使用它来切换到不同的 hypervisor 连接。

如果不提供 URI，virsh 会使用当前 URI 重新连接。URI 格式为 `driver[+transport]://[user@][host][:port]/[path]`。常见的本地 URI 包括 `qemu:///system`（系统级 QEMU/KVM，需要 root）、`qemu:///session`（每用户 QEMU/KVM）、`xen:///system`（Xen）和 `lxc:///system`（Linux Containers）。远程连接使用传输后缀，如 **+ssh**、**+tls**、**+tcp** 或 **+libssh**。当完全没有指定 URI 时，libvirt 会先检查 `LIBVIRT_DEFAULT_URI` 环境变量，然后检查客户端配置中的 `uri_default` 设置，最后探测可用的 hypervisor。

# INSTALL

```apt: sudo apt install libvirt-clients```

```dnf: sudo dnf install libvirt-client```

```apk: sudo apk add libvirt-client```

```zypper: sudo zypper install libvirt-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-list](/man/virsh-list)(1), [virsh-help](/man/virsh-help)(1)

