# TAGLINE

HandBrake 视频转码器的 GTK 图形界面

# TLDR

**启动 HandBrake 图形界面**

```ghb```

**直接在图形界面中打开视频文件**

```ghb [video.mkv]```

打开图形界面并**预选一个预设**

```ghb --preset="[Fast 1080p30]"```

**加载 DVD/蓝光设备或目录**

```ghb --device [/dev/dvd]```

启动时**自动开始转码队列**

```ghb --auto-start-queue [video.mkv]```

**启用输出到终端的详细调试日志**

```ghb --debug --console```

# SYNOPSIS

**ghb** [_options_] [_file_]

# PARAMETERS

**-d**, **--device** _file_
> 启动时加载用于转码的设备、目录或文件。

**-p**, **--preset** _name_
> 启动时选择的预设。

**-x**, **--debug**
> 启用详细（调试级）日志。

**-c**, **--console**
> 将调试输出写入控制台，而不是在内部捕获。

**-o**, **--config** _dir_
> 覆盖用户配置目录。

**--auto-start-queue**
> 启动时自动开始转码队列。

**--clear-queue**
> 启动时清除之前排队的项目。

# DESCRIPTION

**HandBrake** 是一款开源视频转码器。**ghb** 是其原生 GTK 图形界面，在 Linux 上用于选择来源、挑选预设、配置视频/音频/字幕设置，并以交互方式管理转码队列。

ghb 与 [HandBrakeCLI](/man/handbrakecli)(1) 共享相同的底层 libhb 编码引擎和预设格式：在 ghb 中创建或调整的预设可以导出，并在 HandBrakeCLI 中复用于脚本化或无头转码，反之亦然。

在 Linux 上，ghb 通过发行版的软件包安装（如 Arch 上的 `handbrake`、Debian/Ubuntu 上的 `handbrake-gtk`），也可以作为 `fr.handbrake.ghb` Flatpak 安装。

# CAVEATS

需要图形会话（GTK4/Wayland 或 X11）；在没有显示转发的纯 SSH 连接下无法使用。DVD/蓝光解密需要 libdvdcss。硬件编码需要兼容的 GPU 及驱动。

# HISTORY

HandBrake 最初由 **Eric Petit** 于 **2003 年**为 BeOS 创建，当时名为 "MediaFork"，后来更名并移植到其他平台。GTK 界面是在开源社区复兴该项目之后为 Linux 用户编写的，现在面向 GTK 4。

# INSTALL

```apt: sudo apt install handbrake```

```pacman: sudo pacman -S handbrake```

```brew: brew install handbrake```

```nix: nix profile install nixpkgs#handbrake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[handbrakecli](/man/handbrakecli)(1), [ffmpeg](/man/ffmpeg)(1), [vlc](/man/vlc)(1)

# RESOURCES

```[Source code](https://github.com/HandBrake/HandBrake)```

```[Homepage](https://handbrake.fr/)```

```[Documentation](https://handbrake.fr/docs/)```

<!-- verified: 2026-07-17 -->
