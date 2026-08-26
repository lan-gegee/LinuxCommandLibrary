# TAGLINE

快速的 Wayland 终端模拟器

# TLDR

**启动**一个终端

```foot```

**校验**配置文件

```foot -C```

启动**服务器**（用 footclient 启动终端窗口）

```foot -s```

显示**帮助**

```foot -h```

显示**版本**

```foot -v```

# SYNOPSIS

**foot** [_options_] [_command_ [_args_]]

# PARAMETERS

**-c**, **--config=**_FILE_
> 使用配置文件 _FILE_ 而非默认文件

**-C**, **--check-config**
> 校验配置文件并退出

**-s**, **--server**
> 以服务器模式运行；用 footclient 启动终端

**-t**, **--term=**_TERM_
> 设置 TERM 环境变量的值

**-T**, **--title=**_TITLE_
> 设置初始窗口标题

**-a**, **--app-id=**_ID_
> 设置 Wayland app-id

**-w**, **--window-size-pixels=**_WxH_
> 设置初始窗口大小（像素）

**-W**, **--window-size-chars=**_COLSxROWS_
> 设置初始窗口大小（字符）

**-f**, **--font=**_FONT_
> 覆盖配置中的字体设置

**-h**, **--help**
> 显示帮助信息

**-v**, **--version**
> 显示版本信息

# DESCRIPTION

**foot** 是一个为 Wayland 合成器设计的快速、轻量、极简的终端模拟器。它强调速度、低内存占用和简洁性，同时提供现代特性。

主要特性包括 sixel 图像支持、防止画面撕裂的同步渲染、字体连字、回滚搜索以及 URL 检测。它可以以服务器模式运行：单个守护进程通过 **footclient** 管理多个终端窗口，从而降低内存开销。

配置通过 **~/.config/foot/foot.ini** 完成，可为颜色、字体、按键绑定和行为提供大量自定义选项。

# CONFIGURATION

**~/.config/foot/foot.ini**
> 主配置文件，涵盖颜色、字体、按键绑定、回滚及终端行为。

**~/.config/foot/colors.ini**
> 可选的独立配色方案配置，可从 foot.ini 中包含进来。

# CAVEATS

foot 仅支持 Wayland，不支持 X11。某些依赖 xterm 特定行为的应用可能无法正常工作。服务器模式下需要用 footclient 来启动额外的终端。

# HISTORY

foot 由 Daniel Eklof 开发，于 **2020** 年首次发布。它从零开始专为 Wayland 设计，避免了 X11 终端模拟器的历史包袱，同时实现了卓越的性能。

# INSTALL

```apt: sudo apt install foot```

```dnf: sudo dnf install foot```

```pacman: sudo pacman -S foot```

```apk: sudo apk add foot```

```zypper: sudo zypper install foot```

```brew: brew install foot```

```nix: nix profile install nixpkgs#foot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[footclient](/man/footclient)(1), [alacritty](/man/alacritty)(1), [kitty](/man/kitty)(1), [wezterm](/man/wezterm)(1)

# RESOURCES

```[Source code](https://codeberg.org/dnkl/foot)```

<!-- verified: 2026-07-15 -->
