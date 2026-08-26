# TAGLINE

以长格式列出目录内容

# TLDR

**以长格式列出目录内容**

```vdir```

**包含隐藏文件**

```vdir -a```

**以人类可读方式显示大小**

```vdir -h```

**按修改时间排序，最新的在前**

```vdir -t```

**反转排序顺序**

```vdir -r```

# SYNOPSIS

**vdir** [_-a_] [_-h_] [_-t_] [_options_] [_files_]

# PARAMETERS

**-a**
> 包含隐藏文件。

**-h**
> 人类可读。

**-t**
> 按时间排序。

**-r**
> 反转顺序。

**-S**
> 按大小排序。

# DESCRIPTION

**vdir** 默认以长格式列出目录内容，相当于执行 **ls -l**。它会显示每个条目的文件权限、所有者、组、大小、修改时间和名称。

该命令属于 GNU coreutils，接受与 **ls** 相同的选项。它为偏好详细目录列表的用户提供便利，无需每次指定 **-l** 选项。

# CAVEATS

等价于 ls -l。GNU 特有。为可移植性考虑请使用 ls。

# HISTORY

**vdir** 是 **GNU coreutils** 的一部分，默认采用长列表格式，等价于 ls。

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

[ls](/man/ls)(1), [dir](/man/dir)(1), [exa](/man/exa)(1)
