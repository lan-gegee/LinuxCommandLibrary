# TAGLINE

修改用户账户属性

# TLDR

更改**用户名**

```sudo usermod -l new_username username```

更改**用户 ID**

```sudo usermod -u 1001 username```

更改用户的 **shell**

```sudo usermod -s /bin/zsh username```

将用户**加入**补充组

```sudo usermod -aG group1,group2 username```

**设置**用户的补充组（会替换现有配置）

```sudo usermod -G group1,group2 username```

更改**主目录**并迁移原有内容

```sudo usermod -m -d /new/home username```

**锁定**账户

```sudo usermod -L username```

**解锁**账户

```sudo usermod -U username```

# SYNOPSIS

**usermod** [_options_] _LOGIN_

# DESCRIPTION

**usermod** 通过修改系统账户文件来更改用户账户属性。它可以更新用户名、用户 ID、所属组、主目录、shell 以及账户状态。

# PARAMETERS

**-a, --append**
> 追加到补充组（与 -G 搭配使用）

**-c, --comment COMMENT**
> 更改注释字段（GECOS）

**-d, --home HOME_DIR**
> 设置新的主目录

**-e, --expiredate DATE**
> 设置账户过期日期（YYYY-MM-DD）

**-f, --inactive DAYS**
> 密码过期后多少天将账户禁用

**-g, --gid GROUP**
> 更改主要组

**-G, --groups GROUP1,GROUP2**
> 设置补充组（会替换现有配置）

**-l, --login NEW_LOGIN**
> 更改用户名

**-L, --lock**
> 锁定用户账户

**-m, --move-home**
> 把主目录内容移动到新位置

**-o, --non-unique**
> 与 -u 搭配使用时允许 UID 不唯一

**-p, --password PASSWORD**
> 设置加密后的密码（crypt(3) 的返回值）

**-s, --shell SHELL**
> 更改登录 shell

**-u, --uid UID**
> 更改用户 ID

**-U, --unlock**
> 解锁用户账户

**-Z, --selinux-user SEUSER**
> 设置 SELinux 用户映射

# CAVEATS

更改 UID 时，需要手动更新该用户所拥有文件的属主信息。搭配使用 **-a** 与 **-G** 可以在保留现有组的同时追加新组。更改用户名时，该用户不能有正在运行的进程。

# HISTORY

**usermod** 属于 **shadow-utils** 软件包，用于管理类 Unix 系统上的用户账户。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[useradd](/man/useradd)(8), [userdel](/man/userdel)(8), [passwd](/man/passwd)(1), [groupmod](/man/groupmod)(8)
