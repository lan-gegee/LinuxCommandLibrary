# TAGLINE

创建新的系统组

# TLDR

创建**新组**

```sudo groupadd group_name```

创建**系统组**

```sudo groupadd -r group_name```

以指定的**组 ID** 创建组

```sudo groupadd -g 1001 group_name```

创建带**初始成员**的组

```sudo groupadd -U user1,user2 group_name```

# SYNOPSIS

**groupadd** [_options_] _NEWGROUP_

# PARAMETERS

**-f, --force**
> 若组已存在则成功退出；若指定的 GID 已被占用则使用下一个可用的 GID

**-g, --gid GID**
> 设置数字组 ID（必须唯一，除非使用 -o）

**-K, --key KEY=VALUE**
> 覆盖 /etc/login.defs 中的默认值

**-o, --non-unique**
> 允许使用重复的 GID 创建

**-p, --password PASSWORD**
> 设置加密后的组密码

**-r, --system**
> 创建系统组

**-U, --users USER1,USER2**
> 将这些用户添加为组成员

**-R, --root CHROOT_DIR**
> 在 chroot 环境中应用更改

**-P, --prefix PREFIX_DIR**
> 在前缀目录中应用更改

**-h, --help**
> 显示帮助消息并退出

# DESCRIPTION

**groupadd** 在系统上创建新的组账户。它将新组信息记录到系统文件（/etc/group 和 /etc/gshadow）中，除非另行指定，否则会分配一个唯一的 GID。

系统组（用 **-r** 创建）使用的 GID 来自 /etc/login.defs 中定义的系统范围，通常在 1000 以下。

# CAVEATS

组名最长 32 个字符，且不能以连字符、加号或波浪号开头。名称不能包含冒号、逗号、空白字符，也不能完全是数字。

# HISTORY

**groupadd** 属于用于管理类 Unix 系统上组账户的 **shadow-utils** 软件包。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groupdel](/man/groupdel)(8), [groupmod](/man/groupmod)(8), [gpasswd](/man/gpasswd)(1), [useradd](/man/useradd)(8)
