# TAGLINE

从系统中删除组

# TLDR

按**名称**从系统中删除组

```sudo groupdel [group_name]```

# SYNOPSIS

**groupdel** [_options_] _group_

# PARAMETERS

**-f**, **--force**
> 强制删除该组，即使有用户把它作为自己的主组

**-h**, **--help**
> 显示帮助消息并退出

**-R**, **--root** _CHROOT_DIR_
> 在 CHROOT_DIR 目录中应用更改并使用其配置文件。仅支持绝对路径

**-P**, **--prefix** _PREFIX_DIR_
> 在 PREFIX_DIR 目录中应用更改。不进行 chroot；用于准备交叉编译目标环境

# DESCRIPTION

**groupdel** 从系统中删除一个组条目。它会修改 /etc/group 和 /etc/gshadow。指定的组必须存在。你不能删除任何现有用户的主组；必须先删除该用户。

被删除组的所属文件仍保留其数字 GID，但失去与组名的关联。你应当手动检查所有文件系统，确保没有文件仍归属于被删除的组。

# CAVEATS

如果有用户的主组是某个组，则无法删除该组；必须先删除该用户。作为次要成员的已登录用户在下一次登录前不会失去访问权限。组被删除后，其所属文件将显示数字 GID 而非组名。退出值：0（成功）、2（语法无效）、6（组不存在）、8（无法删除用户的主组）、10（无法更新组文件）。

# HISTORY

groupdel 属于 shadow-utils 软件包，后者提供标准的 Unix 组管理工具。它与 groupadd 和 groupmod 配合，实现完整的组生命周期管理。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groupadd](/man/groupadd)(8), [groupmod](/man/groupmod)(8), [gpasswd](/man/gpasswd)(1), [userdel](/man/userdel)(8), [chgrp](/man/chgrp)(1), [groups](/man/groups)(1)
