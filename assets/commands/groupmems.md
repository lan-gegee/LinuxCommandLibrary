# TAGLINE

管理组成员关系

# TLDR

**将用户加入组**

```sudo groupmems -g [group] -a [user]```

**将用户移出组**

```sudo groupmems -g [group] -d [user]```

**列出组成员**

```sudo groupmems -g [group] -l```

**清除所有成员**

```sudo groupmems -g [group] -p```

# SYNOPSIS

**groupmems** [_options_]

# PARAMETERS

**-g**, **--group** _GROUP_
> 目标组名。超级用户必需；普通用户只能操作自己的主组。

**-a**, **--add** _USER_
> 将用户加入组。

**-d**, **--delete** _USER_
> 将用户从组中删除。

**-l**, **--list**
> 列出组成员。

**-p**, **--purge**
> 清除组内的所有成员。

**-R**, **--root** _DIR_
> 在指定的 chroot 目录中应用更改。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**groupmems** 用于管理组成员关系。它让管理员无需直接编辑 /etc/group 即可向组添加或从中移除用户。

该工具为组成员关系变更提供了安全的接口。普通用户无需超级用户权限即可管理自己的主组；只有超级用户才能使用 **-g** 选项修改其他组。

# CAVEATS

需要 root 权限或主组所有权。属于 shadow-utils 软件包。更改在下次登录时生效。如果 /etc/gshadow 存在，其中的条目会自动更新。

# HISTORY

groupmems 作为 **shadow** 密码工具套件的一部分开发，用于安全的组管理。

# INSTALL

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groups](/man/groups)(1), [gpasswd](/man/gpasswd)(1), [usermod](/man/usermod)(8), [groupadd](/man/groupadd)(8), [groupmod](/man/groupmod)(8)
