# TAGLINE

比较 RCS 文件的修订

# TLDR

**比较工作文件与最新修订**

```rcsdiff [file]```

**比较特定修订**

```rcsdiff -r[1.1] -r[1.2] [file]```

**统一 diff 格式**

```rcsdiff -u [file]```

**上下文 diff 格式**

```rcsdiff -c [file]```

**与特定修订比较**

```rcsdiff -r[1.5] [file]```

**并排显示**

```rcsdiff -y [file]```

# SYNOPSIS

**rcsdiff** [_-r rev1_] [_-r rev2_] [_-u_] [_-c_] _file_

# PARAMETERS

**-r** _REV_
> 要比较的修订。

**-u**
> 统一 diff 输出。

**-c**
> 上下文 diff 输出。

**-y**
> 并排显示。

**-q**
> 安静模式。

**-n**
> RCS 格式输出。

# DESCRIPTION

**rcsdiff** 比较由版本控制系统（RCS）管理的文件的不同修订。不带 **-r** 标志时，它将当前工作文件与最新检入的修订进行比较，显示本地修改。带一个 **-r** 标志时，它将工作文件与指定修订比较；带两个 **-r** 标志时，则直接比较两个历史修订。

该工具支持所有标准的 diff 输出格式，包括统一格式（**-u**）、上下文格式（**-c**）、并排格式（**-y**）和普通 diff。它会将选项透传给底层的 diff 命令，是比较版本化文件历史时的便捷封装。

# CAVEATS

RCS 是遗留系统，建议改用 Git。仅支持文件级版本管理。

# HISTORY

**rcsdiff** 属于 **RCS**（Revision Control System），由 **Walter Tichy** 于 1982 年在普渡大学创建。

# INSTALL

```apt: sudo apt install rcs```

```dnf: sudo dnf install rcs```

```pacman: sudo pacman -S rcs```

```apk: sudo apk add rcs```

```zypper: sudo zypper install rcs```

```brew: brew install rcs```

```nix: nix profile install nixpkgs#rcs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rcs](/man/rcs)(1), [ci](/man/ci)(1), [co](/man/co)(1), [diff](/man/diff)(1)
