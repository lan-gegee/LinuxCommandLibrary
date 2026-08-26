# TAGLINE

暂停执行指定时长

# TLDR

以**秒**为单位的延迟

```sleep [seconds]```

以**分钟**为单位的延迟（其他单位：d=天，h=小时，s=秒）

```sleep [minutes]m```

延迟 **1 天 3 小时**

```sleep 1d 3h```

在 **20 分钟**后执行命令

```sleep 20m && [command]```

**无限期**延迟

```sleep infinity```

显示**帮助**

```sleep --help```

# SYNOPSIS

**sleep** _NUMBER_[_SUFFIX_]...

**sleep** _OPTION_

# PARAMETERS

**NUMBER**
> 睡眠的时长

**s**
> 秒（无后缀时的默认值）

**m**
> 分钟

**h**
> 小时

**d**
> 天

**infinity** / **inf**
> 永久睡眠（直到被中断）

**--help**
> 显示帮助并退出

**--version**
> 输出版本信息并退出

# DESCRIPTION

**sleep** 会让程序暂停指定的时长。它接受浮点数和多个时间参数，各参数会相加。该命令常用于 shell 脚本中，在操作之间加入延迟或等待外部进程。

GNU sleep 支持时间后缀（s、m、h、d）以及用于无限期暂停的特殊值 infinity。多个参数会被相加，因此可以写出 **sleep 1h 30m** 这样表示 90 分钟的表达式。

# CAVEATS

时间精度取决于系统能力；极小的小数时长可能不会被精确遵守。infinity 选项会让进程一直运行直到被杀死，仅占用极少资源。并非所有实现都支持后缀或多个参数（POSIX 只要求支持秒）。

# HISTORY

Sleep 自 **Version 4 Unix（1973 年）**起就是 Unix 的一部分。最初的实现只接受整数秒。GNU coreutils 为其扩展了浮点数支持、时间后缀和多个参数。infinity 特性的加入是为了简化需要无限期等待的脚本。

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

[wait](/man/wait)(1), [timeout](/man/timeout)(1), [watch](/man/watch)(1)
