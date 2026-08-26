# TAGLINE

一次性创建多个用户

# TLDR

**从文件创建用户**

```newusers [users.txt]```

**从 stdin 读取**

```echo "[user:password:uid:gid:gecos:home:shell]" | newusers```

**加密方式**

```newusers -c [SHA512] [users.txt]```

**系统默认值**

```newusers -r [users.txt]```

# SYNOPSIS

**newusers** [_options_] [_file_]

# PARAMETERS

_FILE_
> 包含用户条目的文件。

**-c** _METHOD_
> 加密方法。

**-r**
> 创建系统账户。

**--help**
> 显示帮助信息。

# DESCRIPTION

**newusers** 可一次性创建多个用户。它从文件读取用户数据。

该工具处理 passwd 格式的条目，供管理员批量创建用户。

# CAVEATS

需要 root 权限。文件格式有严格要求。输入期间密码为明文。

# HISTORY

newusers 是 **shadow-utils** 的组成部分，用于在 Unix 系统上批量创建用户。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[useradd](/man/useradd)(1), [passwd](/man/passwd)(1), [chpasswd](/man/chpasswd)(1)
