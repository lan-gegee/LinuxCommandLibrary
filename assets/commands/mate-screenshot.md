# TAGLINE

在 MATE 桌面环境中截取屏幕截图

# TLDR

创建**全屏**截图

```mate-screenshot```

创建**活动窗口**截图

```mate-screenshot --window```

创建**指定区域**截图

```mate-screenshot --area```

以**交互方式**创建截图

```mate-screenshot --interactive```

创建**无边框**的截图

```mate-screenshot --window --remove-border```

创建带**特定效果**的截图

```mate-screenshot --effect [shadow|border|none]```

创建带**特定延迟**（秒）的截图

```mate-screenshot --delay [5]```

创建截图并**复制到剪贴板**而不是保存

```mate-screenshot --clipboard```

# SYNOPSIS

**mate-screenshot** [_options_]

# PARAMETERS

**--window, -w**
> 仅捕获活动窗口

**--area, -a**
> 选择要捕获的区域

**--interactive, -i**
> 在截图前打开对话框选择捕获选项

**--delay _seconds_, -d**
> 捕获前等待指定的秒数

**--remove-border, -B**
> 从窗口截图中去除窗口边框

**--effect _type_, -e**
> 添加效果：shadow、border 或 none

**--include-border, -b**
> 在截图中包含窗口边框（默认）

**--clipboard, -c**
> 将截图复制到剪贴板而不是保存

# DESCRIPTION

**mate-screenshot** 在 MATE 桌面环境中截取屏幕截图。它可以捕获整个屏幕、单个窗口或用户选择的区域。

默认情况下，截图会以带时间戳的文件名保存到 Pictures 目录。交互模式会在截图前显示一个对话框，用于选择捕获类型、延迟和效果。

可以为窗口截图应用投影等效果，使其外观更加精美。

# CAVEATS

区域选择需要用鼠标绘制捕获范围。延迟选项适用于捕获悬停时才显示的菜单或工具提示。在某些合成器或窗口管理器下，窗口捕获可能无法正常工作。

# INSTALL

```apt: sudo apt install mate-utils```

```dnf: sudo dnf install mate-utils```

```pacman: sudo pacman -S mate-utils```

```apk: sudo apk add mate-utils```

```zypper: sudo zypper install mate-screenshot```

```nix: nix profile install nixpkgs#mate-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnome-screenshot](/man/gnome-screenshot)(1), [scrot](/man/scrot)(1), [flameshot](/man/flameshot)(1), [maim](/man/maim)(1)
