# TAGLINE

KDE 下拉式终端模拟器

# TLDR

**启动** yakuake

```yakuake```

**显示版本**信息

```yakuake --version```

**显示帮助**

```yakuake --help```

# SYNOPSIS

**yakuake** [_Qt options_] [_KDE options_]

# PARAMETERS

**--help**
> 显示帮助信息。

**--help-qt**
> 显示 Qt 特有选项。

**--help-kde**
> 显示 KDE 特有选项。

**--version**
> 显示版本信息。

**--author**
> 显示作者与致谢。

**--license**
> 显示许可信息。

# KEYBOARD SHORTCUTS

**F12**
> 切换 Yakuake 的可见性（收起/展开）。

**Ctrl+Shift+T**
> 打开新会话（标签页）。

**Ctrl+Shift+W**
> 关闭当前会话。

**Ctrl+(**
> 左右拆分当前会话。

**Ctrl+)**
> 上下拆分当前会话。

**Ctrl+Shift+X**
> 关闭活动的拆分窗格。

**Shift+Left / Shift+Right**
> 切换到上一个/下一个会话标签页。

**Ctrl+Alt+S**
> 重命名当前会话。

**Ctrl+Shift+,**
> 打开配置对话框。

# DESCRIPTION

**yakuake** 是一款面向 KDE 的下拉式终端模拟器，基于 **Konsole** 技术。按下可配置的全局快捷键（默认 F12）激活时，它会从屏幕顶部滑下，类似于 Quake 风格的控制台。

该终端支持标签页、水平和垂直拆分视图、可配置的宽度/高度/透明度，并可通过 KDE 设置系统和 D-Bus 脚本进行大量定制。

# CAVEATS

专为 KDE Plasma 设计，但在安装了所需 KDE Frameworks 库的情况下也能在其他桌面上运行。F12 全局快捷键可能与其他应用冲突，可在配置对话框中重新绑定。

# INSTALL

```apt: sudo apt install yakuake```

```dnf: sudo dnf install yakuake```

```pacman: sudo pacman -S yakuake```

```apk: sudo apk add yakuake```

```zypper: sudo zypper install yakuake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[guake](/man/guake)(1), [konsole](/man/konsole)(1), [tilda](/man/tilda)(1)
