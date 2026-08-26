# TAGLINE

Hyprland 官方的壁纸工具

# TLDR

启动 **hyprpaper 服务**

```hyprpaper```

**预加载**一张壁纸

```hyprctl hyprpaper preload "[path/to/image.png]"```

将壁纸**切换**为另一张已预加载的图片

```hyprctl hyprpaper wallpaper "[monitor],[path/to/image.png]"```

**重载**壁纸（无需先预加载即可设置/更换）

```hyprctl hyprpaper reload "[monitor],[path/to/image.png]"```

在**所有显示器**上设置壁纸（monitor 字段留空）

```hyprctl hyprpaper wallpaper ",[path/to/image.png]"```

**卸载**所有已预加载的壁纸

```hyprctl hyprpaper unload all```

列出**已预加载**的壁纸

```hyprctl hyprpaper listloaded```

# SYNOPSIS

**hyprpaper**

通过以下方式控制：**hyprctl hyprpaper** _command_ [_arguments_]

# PARAMETERS

**preload** _PATH_
> 将壁纸载入内存以便快速切换

**wallpaper** _MONITOR,PATH_
> 在指定显示器上设置壁纸

**reload** _MONITOR,PATH_
> 预加载、设置并卸载不再使用的壁纸

**unload** _PATH_
> 将壁纸从内存中移除

**listloaded**
> 显示已预加载的壁纸

**listactive**
> 显示各显示器当前使用的壁纸

# DESCRIPTION

**hyprpaper** 是 Hyprland 官方的壁纸工具。它以后台服务形式运行，支持在不重启的情况下动态更换壁纸。

配置存储在 **~/.config/hypr/hyprpaper.conf** 中，使用如下指令：
```
preload = /path/to/image.png
wallpaper = monitor,/path/to/image.png
```

预加载系统通过将图片保存在内存中来实现快速切换壁纸。使用 **listloaded** 跟踪内存占用，使用 **unload** 释放不用的壁纸。

# CAVEATS

需要 Hyprland 正在运行。预加载的壁纸会占用内存。大图片或大量预加载壁纸可能影响系统资源。显示器名称必须与 Hyprland 的输出名称一致。

# HISTORY

hyprpaper 由 Vaxry 作为 Hyprland 生态的一部分创建。它专为 Hyprland 的 Wayland 实现提供壁纸功能，并通过 IPC 集成实现动态控制。

# INSTALL

```pacman: sudo pacman -S hyprpaper```

```zypper: sudo zypper install hyprpaper```

```nix: nix profile install nixpkgs#hyprpaper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hyprctl](/man/hyprctl)(1), [swaybg](/man/swaybg)(1), [feh](/man/feh)(1)
