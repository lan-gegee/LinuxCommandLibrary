# TAGLINE

为 i3bar、dzen2、xmobar 或类似状态栏生成状态行

# TLDR

使用默认配置将**状态行**输出到 stdout

```i3status```

使用**指定配置**输出状态行

```i3status -c [path/to/i3status.conf]```

显示**帮助**和版本

```i3status -h```

# SYNOPSIS

**i3status** [_-c config_] [_-h_]

# PARAMETERS

**-c** _CONFIG_
> 使用指定的配置文件

**-h**
> 显示帮助和版本

# DESCRIPTION

**i3status** 为 i3bar、dzen2、xmobar 或类似状态栏生成状态行。它以适合管道传给状态栏的格式输出系统信息，如电池状态、网络连接、磁盘用量和时间。

配置存储在 **~/.config/i3status/config** 或 **/etc/i3status.conf**。配置文件定义要显示哪些模块及其顺序。

常用模块：
- **disk** — 文件系统用量
- **wireless/ethernet** — 网络状态
- **battery** — 电量与状态
- **cpu_usage** — CPU 利用率
- **load** — 系统平均负载
- **time** — 日期与时间
- **volume** — 音频音量

# CAVEATS

主要为 i3 窗口管理器设计，但也可与其他状态栏配合使用。某些模块需要特定的内核特性或硬件。可通过包装方式用自定义脚本扩展功能。

# HISTORY

i3status 由 Michael Stapelberg 创建，是始于 **2009 年**的 i3 窗口管理器项目的一部分。它遵循 Unix 哲学，提供轻量高效的状态行生成功能。

# INSTALL

```apt: sudo apt install i3status```

```dnf: sudo dnf install i3status```

```pacman: sudo pacman -S i3status```

```apk: sudo apk add i3status```

```zypper: sudo zypper install i3status```

```nix: nix profile install nixpkgs#i3status```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[i3](/man/i3)(1), [polybar](/man/polybar)(1), [waybar](/man/waybar)(5)
