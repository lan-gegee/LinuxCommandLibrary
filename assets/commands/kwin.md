# TAGLINE

KDE Plasma 的窗口管理器

# TLDR

**启动 KWin（X11）**

```kwin_x11 --replace```

**启动 KWin Wayland**

```kwin_wayland```

**重启 KWin**

```kwin_x11 --replace &```

**重新配置 KWin**

```qdbus org.kde.KWin /KWin reconfigure```

**列出特效**

```qdbus org.kde.KWin /Effects listLoadedEffects```

# SYNOPSIS

**kwin_x11** [_options_]

**kwin_wayland** [_options_]

# PARAMETERS

**--replace**
> 替换正在运行的窗口管理器。

**--crashes** _n_
> 触发重启的崩溃次数上限。

**--lock**
> 以锁屏状态启动。

**--no-kactivities**
> 禁用 KActivities。

# DESCRIPTION

**KWin** 是 KDE Plasma 的窗口管理器。它负责处理窗口摆放、装饰、虚拟桌面和桌面特效（合成）。

KWin 同时支持 X11（kwin_x11）和 Wayland（kwin_wayland）会话，提供窗口平铺、果冻窗口、桌面网格和脚本化等特性。

# D-BUS CONTROL

```bash
# Toggle present windows
qdbus org.kde.KWin /Effects togglePresentWindows

# Show desktop grid
qdbus org.kde.KWin /Effects showDesktopGrid

# Reconfigure after settings change
qdbus org.kde.KWin /KWin reconfigure
```

# CAVEATS

Wayland 会话与 X11 的能力有所不同。部分特效需要 OpenGL。脚本功能使用 JavaScript。

# HISTORY

KWin 由 **Matthias Ettrich** 于 **1997 年**编写，是 KDE 1 的组成部分。此后它经历了长足演进：KDE 4 中加入合成支持，Plasma 5 中加入 Wayland 支持。

# INSTALL

```apt: sudo apt install kwin-x11```

```dnf: sudo dnf install kwin-x11```

```pacman: sudo pacman -S kwin-x11```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[plasmashell](/man/plasmashell)(1), [systemsettings](/man/systemsettings)(1), [qdbus](/man/qdbus)(1)
