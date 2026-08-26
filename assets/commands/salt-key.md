# TAGLINE

管理 Salt minion 的认证密钥

# TLDR

**列出所有密钥**（已接受、待处理和已拒绝）

```salt-key -L```

**接受指定的 minion 密钥**

```salt-key -a [minion_id]```

**接受所有待处理的密钥**

```salt-key -A```

**拒绝指定的 minion 密钥**

```salt-key -r [minion_id]```

**删除指定的 minion 密钥**

```salt-key -d [minion_id]```

**打印指定密钥的指纹**

```salt-key -f [minion_id]```

**打印所有密钥的指纹**

```salt-key -F```

# SYNOPSIS

**salt-key** [_options_]

# PARAMETERS

**-L**, **--list-all**
> 列出所有已接受、待处理和已拒绝的 minion 密钥

**-l** _ARG_, **--list**=_ARG_
> 列出密钥：pre/un/unaccepted、acc/accepted、rej/rejected 或 all

**-a** _KEY_ID_, **--accept**=_KEY_ID_
> 接受指定的 minion 密钥

**-A**, **--accept-all**
> 接受所有待处理的 minion 密钥

**-r** _KEY_ID_, **--reject**=_KEY_ID_
> 拒绝指定的 minion 密钥

**-R**, **--reject-all**
> 拒绝所有待处理的 minion 密钥

**-d** _KEY_ID_, **--delete**=_KEY_ID_
> 删除指定的 minion 密钥

**-D**, **--delete-all**
> 删除所有密钥

**-f** _KEY_ID_, **--finger**=_KEY_ID_
> 打印指定密钥的指纹

**-F**, **--finger-all**
> 打印所有密钥的指纹

**-y**, **--yes**
> 对所有问题回答 yes（谨慎使用）

**-c** _DIR_, **--config-dir**=_DIR_
> 指定 Salt 配置目录（默认：/etc/salt）

**--gen-keys**=_NAME_
> 生成具有指定名称的密钥对

**--gen-keys-dir**=_DIR_
> 保存所生成密钥对的目录

**--keysize**=_SIZE_
> 所生成密钥的大小（最小 2048）

# DESCRIPTION

**salt-key** 在 Salt master 服务器上管理 Salt minion 的公钥。在 SaltStack 架构中，minion 使用公钥加密与 master 进行身份验证。当 minion 首次连接时，它会将公钥发送给 master，必须显式接受该密钥后才能通信。

密钥有三种状态：未接受（待处理）、已接受或已拒绝。salt-key 命令允许管理员列出、接受、拒绝和删除密钥。在接受 minion 密钥之前，可通过指纹比对来安全地确认其身份。

# CONFIGURATION

**/etc/salt/pki/master/**
> 存放由 salt-key 管理的已接受、待处理和已拒绝 minion 公钥的目录。

**/etc/salt/master**
> master 配置文件，在其中定义密钥接受策略和自动签名设置。

# CAVEATS

接受密钥前务必通过比对指纹核实 minion 的身份。删除密钥是永久性的，在 minion 重新生成密钥之前它将无法连接。**-y** 标志会跳过确认提示，应谨慎使用，尤其是与 **-A**、**-D** 或 **-R** 组合时。需要 root 权限或对 /etc/salt/pki/master/ 的相应权限。

# HISTORY

salt-key 是 **SaltStack**（现为 Salt Project）的一部分，这是一款由 Thomas Hatch 于 **2011 年**创建的开源配置管理与远程执行工具。密钥管理系统为 Salt 的 master-minion 架构提供了安全基础。

# INSTALL

```apk: sudo apk add salt-lts-master```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[salt](/man/salt)(1), [salt-master](/man/salt-master)(8), [salt-minion](/man/salt-minion)(8), [salt-call](/man/salt-call)(1)
