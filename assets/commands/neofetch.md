# TAGLINE

带 ASCII 艺术图的命令行系统信息工具

# TLDR

**显示系统信息**并附带发行版标志

```neofetch```

**使用文件中的自定义 ASCII 艺术图**

```neofetch --ascii [path/to/ascii.txt]```

**使用指定发行版的标志**

```neofetch --ascii_distro [arch]```

**只显示特定信息行**

```neofetch --disable [gpu] [memory]```

**用图片代替 ASCII 艺术图**

```neofetch --backend [kitty] --source [path/to/image.png]```

**不显示 ASCII 艺术图**

```neofetch --off```

**将输出保存到文件**

```neofetch --stdout > [neofetch.txt]```

# SYNOPSIS

**neofetch** [_options_]

# PARAMETERS

**--disable** _info_
> 禁用特定的信息行（如 gpu、memory、uptime）

**--ascii_distro** _distro_
> 使用指定发行版的 ASCII 艺术图

**--ascii** _path_
> 自定义 ASCII 艺术图文件的路径

**--source** _path_
> 图片文件路径（与图像后端配合使用）

**--backend** _backend_
> 图像后端（ascii、kitty、iterm2、sixel、w3m 等）

**--off**
> 完全禁用 ASCII 艺术图

**--color_blocks** _on/off_
> 启用或禁用色块

**--colors** _x x x x x x_
> 更改文字颜色（标题、@、下划线、副标题、冒号、信息）

**--ascii_colors** _x x x x x x_
> 更改 ASCII 艺术图的颜色

**--bold** _on/off_
> 启用或禁用粗体文字

**--stdout**
> 将输出打印到 stdout（便于管道处理/保存）

**--config** _path_
> 使用指定的配置文件

**--print_config**
> 将当前配置打印到 stdout

**--help**
> 显示帮助消息

**--version**
> 显示版本号

# DESCRIPTION

**neofetch** 是一款命令行系统信息工具，能以美观的格式显示操作系统、软件和硬件信息，并搭配发行版的 ASCII 标志或自定义图片一起呈现。

显示的信息包括操作系统、内核版本、开机时长、已安装软件包数量、Shell、分辨率、桌面环境、窗口管理器、终端、CPU、GPU 和内存占用。输出的各个方面都可以通过命令行选项或配置文件高度定制。

Neofetch 因常出现在展示系统配置的截图中而广受欢迎，尤其在 Unix 和 Linux 定制社区。它支持众多操作系统，包括 Linux、BSD、macOS、iOS 和 Windows。

# CAVEATS

图片显示需要兼容的终端模拟器（kitty、iTerm2 或支持 sixel/w3m 的终端）。某些信息并非在所有系统上都可用，或可能需要额外的工具。首次运行会生成配置文件，该文件可能显著改变默认行为。

# HISTORY

**neofetch** 由 **Dylan Araps** 创建，于 **2015 年**作为 bash 脚本首次发布。它很快作为功能更丰富的 **screenfetch** 替代品流行起来。该项目凭借丰富的自定义选项和广泛的发行版支持，在 Unix rice（美化定制）社区声名远扬。**2024 年 4 月**，原作者将项目归档，但 **hyfetch**、**fastfetch** 等社区分支仍在延续其精神。

# INSTALL

```aur: yay -S neofetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[screenfetch](/man/screenfetch)(1), [fastfetch](/man/fastfetch)(1), [inxi](/man/inxi)(1), [hwinfo](/man/hwinfo)(1), [lshw](/man/lshw)(1)
