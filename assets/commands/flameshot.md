# TAGLINE

带标注功能的截图工具

# TLDR

创建**全屏截图**

```flameshot full```

以**交互方式**创建截图（选择区域并添加标注）

```flameshot gui```

创建截图并**保存到指定路径**

```flameshot gui -p [path/to/directory]```

创建截图并**复制到剪贴板**

```flameshot gui -c```

创建截图并**输出到标准输出**（原始 PNG）

```flameshot gui -r```

从**指定显示器**创建截图

```flameshot screen -n [monitor_number]```

以毫秒为单位**延迟**后创建截图

```flameshot full -d [5000]```

打开用于高级选项的**启动器对话框**

```flameshot launcher```

# SYNOPSIS

**flameshot** [_subcommand_] [_options_]

# PARAMETERS

**gui**
> 交互模式，用于选择区域并添加标注

**full**
> 同时捕获所有显示器

**screen**
> 捕获指定的显示器

**launcher**
> 打开高级截图选项对话框

**config**
> 配置应用设置

**-c, --clipboard**
> 将捕获内容复制到剪贴板

**-d, --delay** _ms_
> 捕获前等待指定的毫秒数

**-p, --path** _directory_
> 将截图保存到指定目录

**-r, --raw**
> 将 PNG 数据输出到标准输出

**-u, --upload**
> 将截图上传到外部服务

**--region** _WxH+X+Y_
> 捕获指定尺寸的区域

**-n, --number** _monitor_
> 按编号选择显示器（用于 screen 子命令）

# DESCRIPTION

**Flameshot** 是一款功能强大而简洁的 Linux 截图工具，具有直观的图形界面用于区域选择，并内置标注功能。它支持在保存之前直接在截图上绘制形状、添加文字、箭头和标记。

该工具与系统托盘集成以便快速访问，同时支持 X11 和 Wayland 显示服务器。截图可以保存为文件、复制到剪贴板或上传到图床服务。D-Bus 接口使其支持脚本化以及与其他应用集成。

# CONFIGURATION

**~/.config/flameshot/flameshot.ini**
> 用于界面设置、默认保存路径和键盘快捷键的配置文件。

# CAVEATS

在 Wayland 下，某些功能可能需要额外的权限或特定于合成器的配置。根据所用合成器的不同，**gui** 模式的表现可能有所差异。使用 **--raw** 输出时，请确保接收程序能通过标准输入处理二进制 PNG 数据。

# HISTORY

Flameshot 由 **lupoDharkael** 创建，首次发布于 **2017 年**。它被设计为旧式截图工具的现代替代品，灵感来自 Greenshot（Windows 平台）。该项目使用 **C++** 和 Qt 框架编写，已成为 Linux 生态中最受欢迎的截图工具之一。

# INSTALL

```apt: sudo apt install flameshot```

```dnf: sudo dnf install flameshot```

```pacman: sudo pacman -S flameshot```

```apk: sudo apk add flameshot```

```zypper: sudo zypper install flameshot```

```nix: nix profile install nixpkgs#flameshot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnome-screenshot](/man/gnome-screenshot)(1), [scrot](/man/scrot)(1), [maim](/man/maim)(1), [spectacle](/man/spectacle)(1)
