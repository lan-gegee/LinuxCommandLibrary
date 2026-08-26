# TAGLINE

将任意应用停靠到系统托盘。

# TLDR

**点击模式：**运行 alltray 后点击一个窗口将其停靠

```alltray```

将**指定应用停靠**到系统托盘

```alltray [application]```

用自定义图标**停靠应用**

```alltray -i [path/to/icon.png] [application]```

**停靠应用**并在启动后保持可见

```alltray -s [application]```

**停靠应用**使其在所有工作区都可见

```alltray --sticky [application]```

**创建切换窗口的快捷键**

```alltray -k [Modifier:]Key [application]```

# SYNOPSIS

**alltray** [_OPTIONS_] [_APPLICATION_]

# PARAMETERS

**-h**, **--help**
> 显示选项摘要。

**-v**, **--version**
> 显示程序版本。

**-d**, **--debug**
> 显示调试消息。

**-s**, **--show**
> 启动后不隐藏窗口。

**-i**, **--icon** _FILE_
> 使用 PNG 图片作为托盘图标。

**-l**, **--large_icons**
> 允许大于 24x24 像素的图标。

**-st**, **--sticky**
> 使窗口在所有工作区都可见。

**-g**, **--geometry** _GEOMETRY_
> 设置初始窗口位置（格式见 man X）。

**-k**, **--key** _[Modifier:]Key_
> 创建切换窗口可见性的键盘快捷键。

**-nm**, **--nominimize**
> 关闭按钮直接关闭应用而不是最小化到托盘。

**-conf**, **--configure**
> 显示 KDE 配置对话框。

# DESCRIPTION

**AllTray** 可将任意应用停靠到系统托盘，即使是原生不支持托盘图标的应用。这让你能把终端、邮件客户端或媒体播放器等应用最小化到系统托盘而不是任务栏。

一个关键特性是点击窗口关闭按钮会将应用最小化到托盘而不是退出。此行为可通过 **--nominimize** 选项更改。AllTray 支持 GNOME、KDE、XFCE 4、Fluxbox、WindowMaker 以及其他支持系统托盘规范的窗口管理器。

不带参数运行时，AllTray 进入点击模式，你可以点击任意窗口将其停靠。按 **c** 可中止点击模式。

# CAVEATS

AllTray 依赖 X Window System 和标准系统托盘协议。它可能无法在基于 Wayland 的桌面环境中使用。某些窗口层次复杂的应用可能无法正确停靠。桌面环境必须提供系统托盘，AllTray 才能工作。

# HISTORY

AllTray 由 Jochen Baier 于 **2005** 年创建，旨在为 Linux 桌面上将应用停靠到系统托盘提供通用方案。在许多应用尚未加入原生托盘支持的时代，它因能让应用在后台保持运行而不弄乱任务栏而流行起来。

# INSTALL

```aur: yay -S alltray```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[kdocker](/man/kdocker)(1), [trayer](/man/trayer)(1), [stalonetray](/man/stalonetray)(1)

# RESOURCES

```[Source code](https://github.com/mbt/AllTray)```

<!-- verified: 2026-06-11 -->
