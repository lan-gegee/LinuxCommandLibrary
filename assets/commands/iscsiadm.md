# TAGLINE

管理 iSCSI 发起端连接的命令行工具

# TLDR

显示**活动会话**

```sudo iscsiadm -m session```

列出所有**已知节点**

```sudo iscsiadm -m node```

在门户上**发现** iSCSI 目标

```sudo iscsiadm -m discovery -t sendtargets -p [ip_address]```

**登录**到 iSCSI 目标

```sudo iscsiadm -m node -T [iqn] -p [ip_address]:3260 -l```

从 iSCSI 目标**登出**

```sudo iscsiadm -m node -T [iqn] -p [ip_address]:3260 -u```

手动**创建**节点（用于 CHAP 认证）

```sudo iscsiadm -m node -o new -T [iqn] -p [ip_address]:3260```

配置 **CHAP 认证**

```sudo iscsiadm -m node -T [iqn] -p [ip_address]:3260 -o update -n node.session.auth.authmethod -v CHAP```

# SYNOPSIS

**iscsiadm** **-m** _mode_ [_options_]

# PARAMETERS

**-m**, **--mode** _MODE_
> 操作模式：discovery、node、session、iface

**-t**, **--type** _TYPE_
> 发现类型：sendtargets、isns

**-p**, **--portal** _IP:PORT_
> 目标门户地址

**-T**, **--targetname** _IQN_
> 目标 iSCSI 限定名称（IQN）

**-l**, **--login**
> 登录到目标

**-u**, **--logout**
> 从目标登出

**-o**, **--op** _OP_
> 操作：new、delete、update、show

**-n**, **--name** _NAME_
> 参数名

**-v**, **--value** _VALUE_
> 参数值

# DESCRIPTION

**iscsiadm** 是用于管理 iSCSI 发起端连接的命令行工具。它负责发现 iSCSI 目标、配置认证以及管理会话。

iSCSI 允许通过 IP 网络访问块存储，将远程存储呈现为本地 SCSI 设备。发起端（客户端）使用 IQN（iSCSI Qualified Name，iSCSI 限定名称）标识自身并连接到目标（存储端）。

# CAVEATS

需要 root 权限。iscsid 守护进程必须正在运行。对于需要认证的目标，必须在登录前配置好 CHAP 凭据。节点配置的更改需要登出后重新登录才能生效。

# HISTORY

iscsiadm 是 Open-iSCSI 项目的一部分，该项目为 Linux 提供标准的 iSCSI 实现。iSCSI 于 **2004 年**在 RFC 3720 中标准化。

# INSTALL

```apt: sudo apt install open-iscsi```

```pacman: sudo pacman -S open-iscsi```

```apk: sudo apk add open-iscsi```

```zypper: sudo zypper install open-iscsi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsblk](/man/lsblk)(8)
