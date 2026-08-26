# TAGLINE

修改组定义

# TLDR

修改**组名**

```sudo groupmod -n [new_group] [group_name]```

修改**组 ID**

```sudo groupmod -g [new_id] [group_name]```

# SYNOPSIS

**groupmod** [_options_] _group_

# PARAMETERS

**-g**, **--gid** _GID_
> 将组 ID 改为 _GID_

**-n**, **--new-name** _NAME_
> 将组名改为 _NAME_

**-o**, **--non-unique**
> 允许非唯一的 GID

**-p**, **--password** _PASSWORD_
> 设置加密后的组密码

**-a**, **--append**
> 与 **-U** 搭配使用时，将给定用户追加到组的现有成员之后而不是替换成员列表

**-U**, **--users** _USER_[,_USER_,...]
> 以逗号分隔的用户名列表，设置为组的成员

**-R**, **--root** _CHROOT_DIR_
> 在 chroot 环境中应用更改

**-P**, **--prefix** _PREFIX_DIR_
> 在前缀目录中应用更改（不 chroot，但使用其中的配置文件）

**-h**, **--help**
> 显示帮助消息并退出

# DESCRIPTION

**groupmod** 修改系统上现有组的属性。它可以更改组名、组 ID（GID）或组密码。

更改 GID 时，该组所拥有的文件不会被自动更新。你必须手动查找并更新文件归属，例如使用 **find / -gid OLDGID -exec chgrp NEWGROUP {} \;** 这样的命令。

更改组名对文件归属没有影响，因为文件是通过 GID 而不是名称来引用组的。

# CAVEATS

修改 GID 不会自动更新文件归属。用户必须注销后重新登录，组变更才会生效。不能把组改成已存在的名称或 GID（除非对 GID 使用 -o）。

# HISTORY

groupmod 属于 shadow-utils 软件包，后者一直是各 Linux 发行版上 Unix 组管理的标准工具。它提供对 /etc/group 和 /etc/gshadow 文件的安全修改。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groupadd](/man/groupadd)(8), [groupdel](/man/groupdel)(8), [gpasswd](/man/gpasswd)(1), [usermod](/man/usermod)(8)
