# TAGLINE

X11 模拟和数字时钟显示

# TLDR

显示**模拟**时钟

```xclock```

显示**数字**时钟（24 小时简式）

```xclock -digital -brief```

带**自定义格式**的数字时钟

```xclock -digital -strftime [format]```

按**秒**更新的数字时钟

```xclock -digital -strftime '%H:%M:%S' -update 1```

**12 小时制**数字时钟

```xclock -digital -twelve -brief```

# SYNOPSIS

**xclock** [_OPTIONS_]

# PARAMETERS

**-digital**
> 显示数字时钟而不是模拟时钟

**-brief**
> 只显示时和分

**-twelve**
> 使用 12 小时制格式

**-strftime** _FORMAT_
> 自定义时间格式（参见 strftime）

**-update** _SECONDS_
> 更新间隔

# DESCRIPTION

**xclock** 在 X11 窗口中以模拟或数字形式显示时间。它可以以多种时间格式显示，并以可配置的间隔更新。

模拟显示呈现传统的钟表表盘。数字模式支持 strftime 格式化以实现自定义显示。

# CAVEATS

仅支持 X11。需要运行 X 服务器。属于 X.Org 实用工具的一部分。

# INSTALL

```apt: sudo apt install x11-apps```

```dnf: sudo dnf install xclock```

```apk: sudo apk add xclock```

```zypper: sudo zypper install xclock```

```nix: nix profile install nixpkgs#xclock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[date](/man/date)(1)
