# TAGLINE

在终端中实时绘制图形的 ping 工具

# TLDR

**以图形方式 ping 主机**

```gping [example.com]```

**ping 多台主机**

```gping [example.com] [google.com] [cloudflare.com]```

**以自定义间隔 ping**

```gping -i [0.5] [example.com]```

**执行命令并绘制结果图形**

```gping --cmd "[curl -so /dev/null -w '%{time_total}' example.com]"```

**以自定义缓冲区大小 ping**

```gping -b [100] [example.com]```

**强制使用 IPv4**

```gping -4 [example.com]```

**设置图表颜色**

```gping --color [blue] [example.com]```

**使用简单图形模式**（用于不支持盲文点字的终端）

```gping -s [example.com]```

# SYNOPSIS

**gping** [_options_] _host_...

# PARAMETERS

**-i**, **--interval** _seconds_
> ping 间隔。默认：0.2。

**-b**, **--buffer** _size_
> 图表中的数据点数量。默认：300。

**-n**, **--watch-interval** _seconds_
> 命令执行图表的间隔。

**-s**, **--simple-graphics**
> 使用点号字符代替盲文点字。

**--vertical-margin** _lines_
> 图表上方的垂直边距。

**--horizontal-margin** _cols_
> 图表两侧的水平边距。

**-c**, **--color** _color_
> 图表线条颜色（可重复使用）。

**-4**
> 强制使用 IPv4。

**-6**
> 强制使用 IPv6。

**--cmd** _command_
> 执行命令并将输出按浮点数绘图。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# COLORS

red, green, blue, yellow, cyan, magenta, white, black

# DESCRIPTION

**gping** 是一个图形化的 ping 工具，它在终端中以实时更新的图表显示延迟。可以同时 ping 多台主机，每台主机用不同颜色显示，便于比较。

**--cmd** 选项可以执行任意命令并将其数值输出绘制成图，适用于绘制响应时间、资源占用等任何时间序列指标。简单图形模式（**-s**）为缺少 Unicode 盲文点字支持的终端使用基本字符。

# CAVEATS

需要 ICMP 权限（在 Linux 上可能需要 root/sudo）。终端需支持 256 色才能获得最佳显示效果。某些终端可能无法正确渲染盲文点字字符。

# HISTORY

gping 由 **orf** 创建，首次发布于 **2020 年**前后。它用 Rust 编写，旨在作为带有可视化反馈的传统 ping 的现代替代品。该项目凭借直观的显示和多主机对比能力而广受欢迎。

# INSTALL

```apt: sudo apt install gping```

```pacman: sudo pacman -S gping```

```apk: sudo apk add gping```

```zypper: sudo zypper install gping```

```brew: brew install gping```

```nix: nix profile install nixpkgs#gping```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ping](/man/ping)(1), [mtr](/man/mtr)(1), [trippy](/man/trippy)(1), [fping](/man/fping)(1)
