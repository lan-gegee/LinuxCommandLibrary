# TAGLINE

切换用户身份或运行命令

# TLDR

**切换**到超级用户（root）

```su```

**切换**到指定用户

```su [username]```

**以完整登录 Shell 切换**到某用户

```su - [username]```

以其他用户身份**执行**命令

```su - [username] -c "[command]"```

**使用指定 Shell 切换**到某用户

```su -s /[path/to/shell] [username]```

# SYNOPSIS

**su** [_options_] [_-_] [_user_]

# PARAMETERS

**-, -l, --login**
> 提供登录 Shell 环境

**-c, --command _command_**
> 向 Shell 传递单条命令

**-s, --shell _shell_**
> 使用指定的 Shell 而不是默认值

**-p, --preserve-environment**
> 保留整个环境

**-m**
> 保留环境（与 -p 相同）

**-g, --group _group_**
> 指定主组

# DESCRIPTION

**su**（substitute user）允许以其他用户的身份运行 Shell 或命令。不提供用户名时，默认切换到 root 用户。

**su** 与 **su -** 的区别在于后者提供完整的登录环境，会重置环境变量并切换到目标用户的主目录。

# CAVEATS

需要目标用户的密码（或 root 权限）。在许多现代系统上，以 root 身份运行命令时更推荐使用 **sudo**。建议使用 **su -** 而不是单纯的 **su**，以获得干净的环境。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add heimdal-su```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sudo](/man/sudo)(8), [login](/man/login)(1), [runuser](/man/runuser)(1)
