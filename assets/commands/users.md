# TAGLINE

列出当前登录的用户名

# TLDR

**显示已登录的用户**

```users```

**从指定文件读取**

```users [/var/log/wtmp]```

# SYNOPSIS

**users** [_file_]

# PARAMETERS

_file_
> 用作替代的 utmp 文件。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**users** 以紧凑、空格分隔的形式打印当前登录系统的用户名列表。如果某位用户拥有多个登录会话，其名字会随会话数量重复出现。

该命令默认读取 /var/run/utmp 来判断谁已登录。也可以把其他 utmp 格式的文件作为参数传入，例如查看 /var/log/wtmp 来获取历史登录记录。

与能提供每个会话详细信息的 **who** 和 **w** 不同，users 的输出极为精简，适合快速检查，或者只需要登录用户名列表的脚本场景。

# CAVEATS

输出十分简单。如需详细信息请使用 who。只反映当前的登录情况。

# HISTORY

**users** 是一条标准的 Unix 命令，用于以紧凑列表的形式输出当前登录系统的用户。

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

[who](/man/who)(1), [w](/man/w)(1), [last](/man/last)(1), [whoami](/man/whoami)(1)
