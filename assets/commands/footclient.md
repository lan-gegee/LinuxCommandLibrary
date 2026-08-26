# TAGLINE

foot 终端服务器的客户端

# TLDR

通过 foot 服务器**打开新的终端窗口**

```footclient```

**打开运行特定命令的终端**

```footclient [command]```

**在指定目录中打开终端**

```footclient -D [path/to/directory]```

**打开带自定义标题的终端**

```footclient -T "[My Terminal]"```

**连接到自定义套接字**路径

```footclient --server-socket=[path/to/foot.sock]```

**打开最大化的终端**窗口

```footclient --maximized```

**打开全屏的终端**窗口

```footclient --fullscreen```

# SYNOPSIS

**footclient** [_OPTIONS_] [_COMMAND_ [_ARGS_...]]

# PARAMETERS

**-D**, **--working-directory**=_DIR_
> 在指定目录中启动终端。

**-T**, **--title**=_TITLE_
> 设置初始窗口标题。

**-a**, **--app-id**=_ID_
> 设置 Wayland app-id（供窗口管理器匹配）。

**-m**, **--maximized**
> 以最大化方式启动窗口。

**-F**, **--fullscreen**
> 以全屏模式启动窗口。

**-s**, **--server-socket**=_PATH_
> 连接到指定套接字路径上的 foot 服务器。

**-H**, **--hold**
> 命令退出后保持终端开启。

**-N**, **--no-wait**
> 立即与服务器断开（不等待窗口关闭）。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**footclient** 是 foot 终端模拟器服务器模式的客户端。当 foot 以服务器模式运行（**foot --server**）时，footclient 连接到它以打开新终端窗口。这种架构提供了更快的启动速度和更低的内存占用，因为字体、字形缓存和配置在所有终端窗口之间共享。

服务器监听一个 Unix 套接字，默认为 **$XDG_RUNTIME_DIR/foot-$WAYLAND_DISPLAY.sock**。除非指定 **--no-wait**，footclient 会一直运行到关联的终端窗口关闭为止。

典型用法是在登录时启动 **foot --server**（通常借助 systemd socket activation），之后所有终端都通过 footclient 启动。

# CAVEATS

需要 foot 服务器正在运行。所有终端共享同一个服务器进程，因此服务器崩溃会影响所有窗口。多终端高负载时性能可能不如独立运行的 foot 实例。仅支持 Wayland；foot 不支持 X11。

# HISTORY

Foot 由 Daniel Eklöf 创建，是专为 Wayland 合成器设计的快速轻量终端模拟器。实现服务器/客户端架构是为了解决启动多个终端实例时的启动时间和内存开销问题。Foot 凭借其性能与简洁性在 Wayland 生态中广受欢迎。

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

[foot](/man/foot)(1), [alacritty](/man/alacritty)(1), [kitty](/man/kitty)(1), [wezterm](/man/wezterm)(1)

# RESOURCES

```[Source code](https://codeberg.org/dnkl/foot)```

<!-- verified: 2026-07-15 -->
