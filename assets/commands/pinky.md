# TAGLINE

显示已登录用户的信息

# TLDR

**显示已登录用户**

```pinky```

**显示特定用户**

```pinky [username]```

**长格式**

```pinky -l [username]```

**短格式**

```pinky -s```

**省略全名**

```pinky -f```

**省略远程主机**

```pinky -h```

# SYNOPSIS

**pinky** [_-l_] [_-s_] [_-f_] [_-h_] [_options_] [_users_]

# PARAMETERS

**-l**
> 长输出格式。

**-s**
> 短输出格式。

**-f**
> 省略全名。

**-h**
> 省略远程主机。

**-w**
> 省略主目录。

**-b**
> 长格式中省略主目录。

**-p**
> 长格式中省略 project 文件。

**--help**
> 显示帮助。

# DESCRIPTION

**pinky** 显示已登录用户的信息。它是 finger 的轻量级替代品。

默认输出显示登录名、全名、终端、空闲时间、登录时间和主机。

长格式增加主目录、shell 和 plan/project 文件，类似 finger 的详细视图。

短格式只显示最少的信息。适合快速列出用户。

该命令读取系统的 utmp 和用户信息。不进行任何网络查询。

# CAVEATS

功能不如 finger 完整。不支持远程主机查询。plan 文件可能不存在。

# HISTORY

**pinky** 是 GNU coreutils 的一部分，作为 **finger** 命令更轻量的本地方案而创建。它不支持网络 finger 协议。

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

[finger](/man/finger)(1), [who](/man/who)(1), [w](/man/w)(1), [users](/man/users)(1)
