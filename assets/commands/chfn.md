# TAGLINE

更改用户的 finger 信息

# TLDR

更新用户的**全名**

```chfn -f [new_display_name] [username]```

更新用户的**办公室房间号**

```chfn -o [new_office_room_number] [username]```

更新用户的**办公电话号码**

```chfn -p [new_office_telephone_number] [username]```

更新用户的**家庭电话号码**

```chfn -h [new_home_telephone_number] [username]```

# SYNOPSIS

**chfn** [_options_] [_username_]

# DESCRIPTION

**chfn** 更改 /etc/passwd 中 GECOS 字段存储的用户信息。这些信息由 finger 命令及其他显示用户详情的工具展示。

用户可以修改自己的信息；root 可以修改任何用户的信息。

# PARAMETERS

**-f, --full-name** _name_
> 设置用户的全名

**-o, --office** _office_
> 设置办公室房间号

**-p, --office-phone** _phone_
> 设置办公电话号码

**-h, --home-phone** _phone_
> 设置家庭电话号码

**-u, --help**
> 显示帮助信息

# CAVEATS

某些系统会限制用户可以修改的字段。GECOS 字段有最大长度限制。除非以 root 身份运行，否则更改需要身份验证。

# HISTORY

GECOS 字段源于通用电气综合操作系统（General Electric Comprehensive Operating System），最初用于存储记账信息。将其用于存储用户信息后来成为了 Unix 的惯例。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[finger](/man/finger)(1), [passwd](/man/passwd)(1), [usermod](/man/usermod)(8)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man1/chfn.1.html)```

<!-- verified: 2026-06-22 -->
