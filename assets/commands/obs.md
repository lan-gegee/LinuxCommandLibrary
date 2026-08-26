# TAGLINE

OBS Studio，一款开源的直播和录屏程序

# TLDR

**启动 OBS Studio**

```obs```

**以特定场景启动**

```obs --scene "[scene_name]"```

**启动并开始录制**

```obs --startrecording```

**启动并开始推流**

```obs --startstreaming```

**启动虚拟摄像头**

```obs --startvirtualcam```

**最小化启动**

```obs --minimize-to-tray```

**使用特定的配置文件与场景集合**

```obs --profile "[profile_name]" --collection "[collection_name]"```

# SYNOPSIS

**obs** [_options_]

# PARAMETERS

**--scene** _NAME_
> 以指定场景启动。

**--profile** _NAME_
> 使用指定配置文件。

**--startrecording**
> 启动时立即开始录制。

**--startstreaming**
> 启动时立即开始推流。

**--startvirtualcam**
> 启动时立即开启虚拟摄像头。

**--startreplaybuffer**
> 启动时立即开启回放缓存。

**--collection** _NAME_
> 使用指定的场景集合。

**--minimize-to-tray**
> 最小化到系统托盘启动。

**--studio-mode**
> 启用工作室模式。

**--multi**, **-m**
> 允许多实例运行而不发出警告。

**--portable**, **-p**
> 使用便携模式（设置保存在应用程序目录中）。

**--always-on-top**
> 以窗口置顶模式启动。

**--verbose**
> 使日志输出更详细。

**--version**, **-V**
> 打印版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**obs** 即 OBS Studio，是一款开源的直播和录屏程序。

该应用提供视频采集、场景合成和直播推流功能，支持跨平台。

# CAVEATS

需要图形硬件。资源占用较高。拥有插件生态。

# HISTORY

OBS Studio 由 **Hugh Bailey** 创建，是一款免费开源的直播软件。

# INSTALL

```apt: sudo apt install obs-studio```

```dnf: sudo dnf install obs-studio```

```pacman: sudo pacman -S obs-studio```

```apk: sudo apk add obs-studio```

```zypper: sudo zypper install obs-studio```

```nix: nix profile install nixpkgs#obs-studio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [vlc](/man/vlc)(1)
