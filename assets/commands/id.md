# TAGLINE

显示用户和组的身份信息

# TLDR

**显示当前用户信息**

```id```

**显示指定用户的信息**

```id [username]```

**只显示用户 ID**

```id -u```

**只显示组 ID**

```id -g```

**显示所有组 ID**

```id -G```

**显示名称而非数字**

```id -n -u```

# SYNOPSIS

**id** [_options_] [_user_]

# PARAMETERS

_USER_
> 要查询的用户名。

**-u**, **--user**
> 仅打印用户 ID。

**-g**, **--group**
> 打印主组 ID。

**-G**, **--groups**
> 打印所有组 ID。

**-n**, **--name**
> 打印名称而非 ID。

**-r**, **--real**
> 打印真实 ID。

**--help**
> 显示帮助信息。

# DESCRIPTION

**id** 显示用户和组的身份信息，展示用户的 UID、GID 以及附加组。

该命令可用于核实权限和组成员关系。默认查询当前用户，也可以查询任意用户。

# CAVEATS

属于 coreutils。显示的是登录时缓存的信息。支持真实 ID 与有效 ID 的区分。

# HISTORY

id 是标准的 **Unix** 命令，在 Linux 上属于 **GNU coreutils**。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[whoami](/man/whoami)(1), [groups](/man/groups)(1), [users](/man/users)(1)
