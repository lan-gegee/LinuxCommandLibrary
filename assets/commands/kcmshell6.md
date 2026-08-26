# TAGLINE

打开单个 KDE Plasma 6 系统设置模块

# TLDR

**列出**所有可用的 KCM 模块

```kcmshell6 --list```

打开**显示 / 屏幕**设置模块

```kcmshell6 kcm_kscreen```

打开**网络**设置

```kcmshell6 kcm_networkmanagement```

在同一个对话框中打开多个模块

```kcmshell6 kcm_fonts kcm_style```

以自定义**窗口标题**和**图标**打开模块

```kcmshell6 kcm_keyboard --caption "[Keyboard]" --icon preferences-desktop-keyboard```

为与默认值不同的设置显示**指示标记**

```kcmshell6 kcm_fonts --highlight```

向模块传递**参数**

```kcmshell6 kcm_kwinrules --args "[window-class]"```

# SYNOPSIS

**kcmshell6** [**--list**] [**--args** _arguments_] [**--icon** _icon_] [**--caption** _caption_] [**--highlight**] _module_...

# PARAMETERS

**--list**
> 列出所有可发现的 KCM（KDE Control Module）插件 ID 及其简短描述，然后退出。

_module_
> 要打开的一个或多个配置模块。ID 可以是完整的插件 id（例如 **kcm_fonts**），也可以是短名称，**kcmshell6** 会依次尝试 **kcm_**_name_ 和 **kcm**_name_ 来展开。多个模块会在列表式对话框中一起打开。

**--args** _arguments_
> 以空格分隔并转发给模块的参数（按 shell 命令行的方式解析）。

**--icon** _icon_
> 对话框窗口使用的主题图标名称。默认使用模块自己的图标。

**--caption** _caption_
> 自定义窗口标题。对于未指定此选项的单个模块，将使用模块名作为标题。

**--highlight**
> 当某项设置被改为偏离默认值时，显示可视化的指示标记。

**--help**
> 显示命令行帮助（通过 KAboutData / QCommandLineParser）。

**--version**
> 显示版本信息。

# DESCRIPTION

**kcmshell6** 在独立对话框中启动一个或多个 **KDE Control Modules（KCM）**，无需打开完整的 **systemsettings** 应用。它是 Plasma 6 中 **kcmshell5** 的后继者，随 **KCMUtils** 框架一同发布。

模块以插件形式在常见的 Plasma KCM 命名空间下被发现（**plasma/kcms**、**plasma/kcms/systemsettings**、**plasma/kcms/systemsettings_qwidgets** 和 **plasma/kcms/kinfocenter**）。每个模块呈现一个聚焦的设置面板（字体、显示、网络、电源等）。当给定多个模块 ID 时，它们会一起出现在多页列表对话框中。

脚本、desktop 文件和文档经常调用 **kcmshell6** 来深链接到单个设置页面。交互式用户通常用 **systemsettings** 浏览设置，在已知模块 id 时则直接使用 **kcmshell6**。

# CAVEATS

需要运行中的图形会话且 Qt/KDE 库可用（通常是 Plasma 桌面）。模块 ID 在不同 Plasma 版本之间有所不同；请在目标机器上使用 **kcmshell6 --list**，而不要硬编码过时的名称。某些模块进行系统级更改时需要提升权限或 PolicyKit。未知的模块 ID 可能仍会打开一个只显示错误的对话框。

# HISTORY

**kcmshell** 起源于 KDE，用于在完整控制中心之外启动单独的控制模块。Plasma 5 使用 **kcmshell5**；Plasma 6 将该二进制文件更名为 **kcmshell6**，并通过 KCMUtils 加载 Qt 6 / KF6 的 KCM 插件（包括基于 QML 的模块）。

# INSTALL

```apt: sudo apt install libkf6kcmutils-bin```

```pacman: sudo pacman -S kcmutils```

```apk: sudo apk add kcmutils```

<!-- packages: 2026-08-04 -->

# SEE ALSO

[systemsettings](/man/systemsettings)(1), [plasmashell](/man/plasmashell)(1), [kwriteconfig5](/man/kwriteconfig5)(1)

# RESOURCES

```[Source code](https://invent.kde.org/frameworks/kcmutils)```

```[Homepage](https://develop.kde.org/docs/features/configuration/kcm/)```

<!-- verified: 2026-08-04 -->
