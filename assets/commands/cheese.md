# TAGLINE

GNOME 网络摄像头拍照录像应用

# TLDR

**启动 Cheese 网络摄像头应用**

```cheese```

**以全屏模式启动**

```cheese --fullscreen```

**以宽屏模式启动（缩略图在右侧）**

```cheese --wide```

**使用特定的视频设备**

```cheese --device=[/dev/video0]```

# SYNOPSIS

**cheese** [**-w**|**--wide**] [**-d**|**--device** _DEVICE_] [**-f**|**--fullscreen**] [**-h**|**--help**] [**-v**|**--version**]

# DESCRIPTION

**Cheese** 是一个 GNOME 网络摄像头应用，可用摄像头拍摄照片和视频。它的功能类似虚拟大头贴机，提供实时预览、视觉特效和便捷的分享能力。

该应用支持超过 20 种视觉特效，包括由 GStreamer 驱动的变形、滤镜和艺术叠加效果。拍摄的照片保存到 **~/Pictures**，视频保存到 **~/Videos**。

# PARAMETERS

**-w, --wide**
> 以宽屏模式启动，缩略图显示在视频预览的右侧

**-d, --device** _DEVICE_
> 使用指定设备作为视频采集设备（例如 /dev/video0）

**-f, --fullscreen**
> 以全屏模式启动

**-h, --help**
> 输出帮助信息并退出

**-v, --version**
> 输出版本信息并退出

# CAVEATS

需要支持 Video4Linux (V4L2) 且工作正常的网络摄像头。可用特效取决于系统安装的 GStreamer 插件。

# HISTORY

**Cheese** 由 Daniel G. Siegel 在 **Google Summer of Code 2007** 期间创建，导师为 Raphaël Slinckx。此后它成为 GNOME 桌面套件的一部分，使用 GStreamer 进行视频处理和特效渲染。

# INSTALL

```apt: sudo apt install cheese```

```zypper: sudo zypper install cheese```

```nix: nix profile install nixpkgs#cheese```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[guvcview](/man/guvcview)(1), [v4l2-ctl](/man/v4l2-ctl)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/cheese)```

<!-- verified: 2026-06-22 -->
