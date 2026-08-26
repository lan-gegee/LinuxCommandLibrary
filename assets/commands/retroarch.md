# TAGLINE

多系统模拟器和游戏前端

# TLDR

以**菜单**模式启动

```retroarch```

使用特定核心**加载 ROM**

```retroarch -L [path/to/core.so] [path/to/rom]```

以**全屏**方式启动

```retroarch -f```

使用特定的**配置**文件

```retroarch -c [path/to/config]```

带详细日志**加载内容**

```retroarch -v -L [path/to/core.so] [path/to/rom]```

列出**编译时特性**

```retroarch --features```

显示**帮助**

```retroarch -h```

# SYNOPSIS

**retroarch** [**-f**] [**-c** _config_] [**-L** _core_] [_content_]

# PARAMETERS

**-f, --fullscreen**
> 以全屏模式启动

**-c, --config _file_**
> 使用指定的配置文件

**-L, --libretro _core_**
> 加载指定的 libretro 核心

**--features**
> 列出编译时特性

**--menu**
> 直接进入菜单

**-v, --verbose**
> 详细日志输出

**-s, --save _slot_**
> 从指定存档槽加载即时存档

**--appendconfig _file_**
> 追加额外的配置文件（覆盖主配置中的值）

**-h, --help**
> 显示帮助

# DESCRIPTION

**retroarch** 是基于 libretro API 的模拟器、游戏引擎和媒体播放器前端。它提供统一的界面，可在众多平台上游玩复古游戏。

该工具为不同系统（NES、SNES、PlayStation 等）使用可互换的"核心"，并提供着色器、联机对战、成就和输入重映射等功能。

# CONFIGURATION

**~/.config/retroarch/retroarch.cfg**
> 主配置文件，控制视频、音频、输入、目录路径和默认核心设置。

**~/.config/retroarch/cores/**
> 存放各模拟系统所用 libretro 核心共享库（.so 文件）的目录。

**~/.config/retroarch/config/**
> 每核心与每游戏的覆盖配置文件，用于补充主配置。

# CAVEATS

核心需要单独下载。不包含游戏 ROM（需自行合法备份）。性能因核心和系统而异。配置可能比较复杂。

# HISTORY

**RetroArch** 是 **libretro** API 的参考实现，由 libretro 团队开发。它由 SSNES 演化而来，现已成为最受欢迎的多系统模拟器前端。

# INSTALL

```apt: sudo apt install retroarch```

```dnf: sudo dnf install retroarch```

```pacman: sudo pacman -S retroarch```

```apk: sudo apk add retroarch```

```zypper: sudo zypper install retroarch```

```nix: nix profile install nixpkgs#retroarch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[emulationstation](/man/emulationstation)(1), [mame](/man/mame)(1)
