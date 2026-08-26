# TAGLINE

Cinnamon 桌面环境的默认文件管理器

# TLDR

**打开**主目录

```nemo```

在**独立窗口中打开**指定目录

```nemo [path/to/directory1] [path/to/directory2]```

在**标签页中打开**目录

```nemo --tabs [path/to/directory1] [path/to/directory2]```

以指定**窗口尺寸打开**

```nemo --geometry=[600]x[400] [path/to/directory]```

**关闭所有**窗口

```nemo --quit```

# SYNOPSIS

**nemo** [**--tabs**] [**--geometry** _WxH_] [**--quit**] [_URI_...]

# PARAMETERS

**--tabs**
> 以标签页而不是窗口的方式打开目录

**--geometry _WxH_**
> 设置初始窗口大小（宽 x 高）

**--new-window**
> 总是打开新窗口

**--quit, -q**
> 关闭所有 Nemo 窗口

**--no-desktop**
> 不管理桌面

**--no-default-window**
> 仅为显式指定的 URI 创建窗口

**--version**
> 显示版本信息

**--help**
> 显示帮助信息

# DESCRIPTION

**Nemo** 是 Cinnamon 桌面环境的默认文件管理器。它是 Nautilus（GNOME Files）的分支，增加了额外功能并提供更传统的界面。

功能包括双栏视图、可配置工具栏、侧边栏树状视图以及丰富的插件支持。Nemo 可以管理桌面图标，并与 Cinnamon 的系统服务集成。

# CAVEATS

桌面管理可能与其他文件管理器冲突。部分功能需要 Cinnamon 桌面集成。扩展需要单独于主软件包安装。

# HISTORY

在 Nautilus 于 3.6 版移除多项功能后，**Linux Mint** 团队于 2012 年从 **Nautilus 3.4** 分支出 **Nemo**。它以儒勒·凡尔纳小说中的尼摩船长命名，延续了海洋主题的命名传统。

# INSTALL

```apt: sudo apt install nemo```

```dnf: sudo dnf install nemo```

```pacman: sudo pacman -S nemo```

```apk: sudo apk add nemo```

```zypper: sudo zypper install nemo```

```nix: nix profile install nixpkgs#nemo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nautilus](/man/nautilus)(1), [thunar](/man/thunar)(1), [dolphin](/man/dolphin)(1), [caja](/man/caja)(1)
