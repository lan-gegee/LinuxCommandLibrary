# TAGLINE

显示系统信息并附带 ASCII 发行版标志

# TLDR

**显示系统信息**并附带发行版标志

```screenfetch```

显示信息后**截取屏幕截图**

```screenfetch -s```

**使用指定发行版的标志**

```screenfetch -D [arch]```

**不显示 ASCII 图形**

```screenfetch -n```

**仅显示 ASCII 图形**（不显示系统信息）

```screenfetch -L```

以适合截图软件的**格式输出**

```screenfetch -p```

**带详细错误消息**显示

```screenfetch -v```

# SYNOPSIS

**screenfetch** [_-v_] [_-o 'OPTIONS'_] [_-n_] [_-N_] [_-t_] [_-p_] [_-s_] [_-c string_] [_-D distro_] [_-A distro_] [_-E_] [_-V_] [_-h_]

# PARAMETERS

**-v**
> 详细输出，便于排查错误

**-o** _'OPTIONS'_
> 允许设置截图选项

**-n**
> 不显示 ASCII 图形

**-N**
> 去除输出中的所有颜色

**-t**
> 根据终端宽度截断输出

**-p**
> 以适合截图的格式输出

**-s**
> 显示信息后截取屏幕截图

**-c** _string_
> 设置颜色（两个 0-9 的数字组成的字符串）

**-D** _distro_
> 指定发行版，覆盖自动检测

**-A** _distro_
> 指定仅用于 ASCII 图形的发行版

**-L**
> 仅显示 ASCII 图形（不显示系统信息）

**-E**
> 抑制错误输出

**-V**
> 显示版本并退出

**-h**
> 显示帮助并退出

# DESCRIPTION

**screenfetch** 是一个 bash 脚本，在显示操作系统标志的 ASCII 图形的同时展示系统信息。它会获取并显示 OS、内核、运行时间、软件包数、Shell、分辨率、桌面环境、窗口管理器、主题、图标、字体、CPU、GPU 和内存等详细信息。

该工具专为展示系统配置的截图而设计，常用于 Unix 定制（"ricing"）社区。它会检测当前运行的发行版或操作系统，并自动选择相应的 ASCII 标志。

Screenfetch 支持众多 Linux 发行版、BSD、macOS 及其他类 Unix 系统。输出可通过命令行选项和环境变量高度自定义。

# CAVEATS

某些系统信息并非在所有平台或配置上都可用。截图功能需要安装 **scrot** 或 **import**（ImageMagick）。详细模式有助于排查检测问题。使用专有驱动的系统上 GPU 检测可能失败。

# HISTORY

**screenfetch** 由 **KittyKatt**（Brett Bohnenkamper）创建，首次发布于 **2010 年**。它是最早一批专为 Unix 定制截图设计的流行系统信息工具之一。在 2015 年功能更丰富、自定义选项更多的 **neofetch** 出现之前，该项目在 Linux 社区中颇受欢迎。Screenfetch 目前仍然可用且能正常工作，但相比其后来者获得的活跃开发较少。

# INSTALL

```dnf: sudo dnf install screenfetch```

```pacman: sudo pacman -S screenfetch```

```zypper: sudo zypper install screenfetch```

```brew: brew install screenfetch```

```nix: nix profile install nixpkgs#screenfetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1), [fastfetch](/man/fastfetch)(1), [inxi](/man/inxi)(1), [lshw](/man/lshw)(1), [hwinfo](/man/hwinfo)(1)
