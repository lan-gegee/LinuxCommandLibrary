# TAGLINE

通过 systemd-homed（systemd 的一个组件）管理用户账户和家目录

# TLDR

**列出**用户账户和家目录

```homectl list```

**创建**用户账户和家目录

```sudo homectl create [username]```

**移除**用户及关联的家目录

```sudo homectl remove [username]```

更改用户的**密码**

```sudo homectl passwd [username]```

以访问**特定 home** 的方式运行 Shell 或命令

```sudo homectl with [username] -- [command]```

**锁定或解锁**家目录

```sudo homectl lock [username]```

更改分配给家目录的**磁盘空间**

```sudo homectl resize [username] 100G```

显示**帮助**

```homectl -h```

# SYNOPSIS

**homectl** [_command_] [_options_] [_user_]

# PARAMETERS

**list**
> 列出受管理的家目录

**create** _USER_
> 创建带家目录的新用户

**remove** _USER_
> 移除用户和家目录

**passwd** _USER_
> 更改用户密码

**with** _USER_ **--** _CMD_
> 以访问用户家目录的方式运行命令

**lock** _USER_
> 锁定家目录（停用）

**unlock** _USER_
> 解锁家目录（激活）

**resize** _USER_ _SIZE_
> 更改家目录大小

**inspect** _USER_
> 显示用户记录详情

**update** _USER_
> 更新用户属性

**--storage=**_TYPE_
> 存储类型：luks、directory、subvolume、fscrypt、cifs

# DESCRIPTION

**homectl** 通过 systemd-homed 管理用户账户和家目录。systemd-homed 是一个 systemd 服务，提供可移植、可加密的家目录。

systemd-homed 将用户账户存储为自带家目录的自包含记录。家目录可以加密（LUKS），支持挂起时自动锁定等安全特性，以及可在机器之间迁移的可移植家目录。

功能包括：
- 加密的家目录
- 挂起/空闲时自动锁定
- 磁盘配额管理
- 可移植的家目录

# CAVEATS

需要 systemd-homed 服务。与传统的 /etc/passwd 管理方式不兼容。某些服务在 homed 用户下可能无法正常工作。LUKS 家目录需要在登录时解锁。

# HISTORY

homectl 和 systemd-homed 由 Lennart Poettering 在 systemd 245（**2020 年**）中引入。它们代表了 Linux 用户管理的一种现代方式，内置加密和可移植性特性。

# INSTALL

```apt: sudo apt install systemd-homed```

```zypper: sudo zypper install systemd-homed```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[useradd](/man/useradd)(8), [usermod](/man/usermod)(8), [loginctl](/man/loginctl)(1)
