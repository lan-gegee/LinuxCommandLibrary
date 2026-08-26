# TAGLINE

管理组密码和组成员关系

# TLDR

定义组**管理员**

```sudo gpasswd -A [user1,user2] [group]```

设置组**成员**列表

```sudo gpasswd -M [user1,user2] [group]```

为指定组创建**密码**

```gpasswd [group]```

将用户**添加**到指定组

```gpasswd -a [user] [group]```

从指定组**移除**用户

```gpasswd -d [user] [group]```

# SYNOPSIS

**gpasswd** [_option_] _group_

# PARAMETERS

**-a**, **--add** _USER_
> 将用户添加到组

**-d**, **--delete** _USER_
> 将用户从组中移除

**-A**, **--administrators** _USER,..._
> 设置组管理员列表

**-M**, **--members** _USER,..._
> 设置组成员列表（替换现有成员）

**-r**, **--remove-password**
> 移除组密码

**-R**, **--restrict**
> 限制对组的访问（仅成员可以使用 newgrp）

# DESCRIPTION

**gpasswd** 用于管理 /etc/group 和 /etc/gshadow 文件。它可以向组中添加或移除用户、设置组管理员以及管理组密码。

组管理员（通过 **-A** 设置）无需 root 权限即可添加或移除成员，从而把组管理委托给受信任的用户。组密码（很少使用）允许非成员通过 **newgrp** 命令临时加入某个组。

# CAVEATS

**-M** 选项会替换全部组成员，而不是追加。增量修改请用 **-a** 和 **-d**。不建议使用组密码，应优先采用规范的成员管理。更改将在下次登录时生效。

# HISTORY

gpasswd 是 shadow-utils 软件包的一部分，该软件包为 Unix 系统提供影子密码（shadow password）套件。shadow 系统开发于 20 世纪 80 年代，通过将密码哈希从人人可读的 /etc/passwd 移到受限访问的 /etc/shadow 文件来提升密码安全性。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groupadd](/man/groupadd)(8), [groupmod](/man/groupmod)(8), [usermod](/man/usermod)(8), [newgrp](/man/newgrp)(1)

# RESOURCES

```[Source code](https://github.com/shadow-maint/shadow)```

<!-- verified: 2026-07-17 -->
