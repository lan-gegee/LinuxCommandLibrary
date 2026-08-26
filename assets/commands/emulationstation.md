# TAGLINE

复古游戏模拟器的图形化前端

# TLDR

**启动 EmulationStation**

```emulationstation```

**以窗口模式启动**

```emulationstation --windowed```

**指定分辨率**

```emulationstation --resolution [1920] [1080]```

**强制完整刷新界面**

```emulationstation --force-full```

**显示帮助**

```emulationstation --help```

# SYNOPSIS

**emulationstation** [_options_]

# PARAMETERS

**--windowed**
> 以窗口模式运行。

**--resolution** _width_ _height_
> 设置屏幕分辨率。

**--gamelist-only**
> 跳过没有 gamelist 的系统。

**--ignore-gamelist**
> 忽略 gamelist.xml 文件。

**--force-full**
> 强制完整重新加载界面。

**--no-splash**
> 启动时不显示启动画面。

**--no-exit**
> 不在菜单中显示退出选项。

**--draw-framerate**
> 在屏幕上显示帧率。

**--vsync** _1|0_
> 开启或关闭垂直同步（默认：开启）。

**--force-kiosk**
> 强制 kiosk 模式。

**--force-kid**
> 强制儿童界面模式。

**--home** _path_
> 指定用作主目录路径的目录。

**--debug**
> 启用调试输出与额外日志。

**--help**, **-h**
> 显示帮助。

# DESCRIPTION

**EmulationStation** 是一个用于组织和启动模拟游戏的图形化前端。它提供精致的界面，可用于浏览游戏合集、展示元数据以及启动各种模拟器。

该程序常用于 RetroPie、Batocera 及其他复古游戏发行版。它支持主题、抓取游戏元数据和封面图片，并支持手柄导航，带来类似游戏机的体验。

# CONFIGURATION

```
~/.emulationstation/
├── es_systems.cfg     # System definitions
├── es_settings.cfg    # Application settings
├── gamelists/         # Per-system game metadata
└── themes/            # Visual themes
```

# CAVEATS

需要单独配置模拟器。首次设置需要 es_systems.cfg。主题兼容性参差不齐。元数据抓取需要网络连接。手柄映射可能需要手动配置。

# HISTORY

EmulationStation 由 **Alec Lofquist**（Aloshi）于 **2012 年**创建。它成为流行的 Raspberry Pi 复古游戏发行版 RetroPie 的默认前端。该项目还衍生出 EmulationStation-DE 等 fork 以继续开发。

# INSTALL

```aur: yay -S emulationstation```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[retroarch](/man/retroarch)(1), [mame](/man/mame)(1)
