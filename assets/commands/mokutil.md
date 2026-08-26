# TAGLINE

管理存储在 shim 数据库中的机器所有者密钥（MOK）

# TLDR

显示**是否已启用安全启动**

```mokutil --sb-state```

**启用**安全启动验证

```mokutil --enable-validation```

**禁用**安全启动验证

```mokutil --disable-validation```

**列出已登记的**密钥

```mokutil -l```

**登记新密钥**

```mokutil -i [path/to/key.der]```

**列出待登记的密钥**

```mokutil -N```

**删除**密钥

```mokutil -d [path/to/key.der]```

**测试**某密钥是否已登记

```mokutil -t [path/to/key.der]```

# SYNOPSIS

**mokutil** [**--sb-state**] [**-l**] [**-i** _keyfile_] [**-d** _keyfile_] [**--enable-validation**] [**--disable-validation**] [_options_]

# PARAMETERS

**--sb-state**
> 显示当前安全启动状态

**-l, --list-enrolled**
> 列出当前已登记的密钥

**-N, --list-new**
> 显示待登记的密钥

**-D, --list-delete**
> 显示标记为待删除的密钥

**-i, --import _keyfile_**
> 将密钥（DER 格式）加入登记队列

**-d, --delete _keyfile_**
> 将密钥加入移除队列

**-x, --export**
> 从 MokListRT 中提取已存储的密钥

**-t, --test-key _keyfile_**
> 验证某个密钥是否已登记

**--enable-validation**
> 启用 shim 验证（安全启动）

**--disable-validation**
> 禁用 shim 验证

**--reset**
> 清空 MOK 列表

**-p, --password**
> 设置 MokManager 密码

**-c, --clear-password**
> 移除密码保护

**-P, --root-pw**
> 使用 /etc/shadow 中的 root 密码哈希

**--pk, --kek, --db, --dbx**
> 列出各个安全启动数据库中的密钥

**--timeout _seconds_**
> 设置启动时 MOK 提示的持续时间

**-X, --mokx**
> 操作 MOK 黑名单而非标准列表

# DESCRIPTION

**mokutil** 管理存储在 shim 数据库中的机器所有者密钥（Machine Owner Key，MOK）。MOK 是在安全启动过程中使用的加密密钥，用于在 UEFI 系统上验证启动组件的真实性。

该工具可以导入、删除和管理用于授权内核模块、引导加载程序及其他签名代码的密钥。对 MOK 数据库的更改需要重启才能生效，重启期间 MokManager 会要求输入配置好的密码进行确认。

# CAVEATS

修改 MOK 数据库的操作（导入、删除、启用/禁用验证）需要重启才能生效。必须在启动时通过 MokManager 输入密码来确认更改。导入的密钥必须是 DER 格式。密钥管理不当可能导致系统在启用安全启动时无法启动。

# HISTORY

**mokutil** 是 **shim** 项目的一部分，该项目旨在让 Linux 系统能够使用安全启动。Shim 是一个由微软签名的第一阶段引导加载程序，借助 MOK 授权各发行版自己的签名密钥，使 Linux 发行版能够在启用安全启动的 UEFI 系统上启动。

# INSTALL

```apt: sudo apt install mokutil```

```dnf: sudo dnf install mokutil```

```pacman: sudo pacman -S mokutil```

```apk: sudo apk add mokutil```

```zypper: sudo zypper install mokutil```

```nix: nix profile install nixpkgs#mokutil```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[efibootmgr](/man/efibootmgr)(8)
