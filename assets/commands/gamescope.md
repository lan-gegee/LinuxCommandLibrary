# TAGLINE

Wayland 游戏微合成器

# TLDR

用 **gamescope** 运行程序

```gamescope -- [program]```

通过 **Steam** 用 gamescope 运行游戏

```gamescope -- %command%```

以整数缩放将 720p 游戏**放大**到 1440p

```gamescope -h 720 -H 1440 -S integer -- [command]```

将开启垂直同步的游戏**限制**到 30 FPS

```gamescope -r 30 -- [command]```

以 gamescope 集成方式**在 Big Picture 模式下启动 Steam**

```gamescope -e -- /usr/bin/steam -tenfoot```

指定优先使用的**显示器**

```gamescope -O [HDMI-A-1|DP-3|...] -- [program]```

切换**全屏**

```Super+f```

显示**帮助**

```gamescope --help```

# SYNOPSIS

**gamescope** [_options_] **--** _command_ [_arguments_]

# PARAMETERS

**-h**, **--nested-height** _HEIGHT_
> 设置内部（嵌套）分辨率高度

**-H**, **--output-height** _HEIGHT_
> 设置输出分辨率高度

**-w**, **--nested-width** _WIDTH_
> 设置内部（嵌套）分辨率宽度

**-W**, **--output-width** _WIDTH_
> 设置输出分辨率宽度

**-r**, **--nested-refresh** _RATE_
> 设置内部刷新率（对开启垂直同步的游戏相当于 FPS 上限）

**-S**, **--scaler** _SCALER_
> 缩放滤镜：auto、integer、fit、fill、stretch

**-e**, **--steam**
> 启用 Steam 集成模式

**-O**, **--prefer-output** _OUTPUT_
> 优先使用的显示输出

**-f**, **--fullscreen**
> 以全屏模式启动

**-b**, **--borderless**
> 以无边框窗口模式启动

**-F**, **--filter** _FILTER_
> 放大算法：linear、nearest、fsr、nis、pixel。

**--hdr-enabled**
> 启用 HDR 输出（需要兼容的显示器和硬件）。

**--mangoapp**
> 与 gamescope 一起启动 MangoHud 覆盖层（mangoapp）。

**--force-grab-cursor**
> 始终使用相对鼠标模式，而不是在相对与绝对之间来回切换。

**--adaptive-sync**
> 在支持的输出上启用自适应同步 / VRR。

# DESCRIPTION

**gamescope** 是 Valve 开发的面向游戏的 Wayland 微合成器。它充当游戏与显示服务器之间的中间层，提供分辨率缩放、帧率限制、HDR 支持以及更好的游戏兼容性等特性。

主要功能包括 FSR（FidelityFX Super Resolution）放大、适合复古游戏的整数缩放、独立的刷新率控制以及无缝的全屏管理。它是 Steam Deck 游戏模式合成器的基础。

与 Steam 配合使用（**-e** 标志）时，它可直接集成 Steam 的覆盖层和游戏管理功能。

# KEYBOARD SHORTCUTS

**Super+F** - 切换全屏
**Super+S** - 截图
**Super+G** - 切换 FPS 限制器

# CAVEATS

需要 Vulkan 支持。某些游戏可能存在兼容性问题。HDR 支持需要相应的硬件和显示器。性能开销很小，但确实存在。

# HISTORY

gamescope 由 Valve Software 开发，首次发布于 **2020 年**。它主要为 Steam Deck 掌上游戏机而创建，是 SteamOS 3.0 游戏模式合成器的基础。该项目由更早的 steamcompmgr 合成器演进而来。

# INSTALL

```dnf: sudo dnf install gamescope```

```pacman: sudo pacman -S gamescope```

```apk: sudo apk add gamescope```

```zypper: sudo zypper install gamescope```

```nix: nix profile install nixpkgs#gamescope```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[steam](/man/steam)(1), [cage](/man/cage)(1), [sway](/man/sway)(1), [weston](/man/weston)(1), [Xwayland](/man/Xwayland)(1)
