# TAGLINE

显示 VA-API 视频加速信息

# TLDR

显示默认设备的 **VA-API 信息**

```vainfo```

**显示指定 DRM 设备的信息**

```vainfo --display drm --device [/dev/dri/renderD128]```

通过 X11 显示器显示 **VA-API 信息**

```vainfo --display x11```

通过 Wayland 显示器显示 **VA-API 信息**

```vainfo --display wayland```

# SYNOPSIS

**vainfo** [_--display type_] [_--device path_] [_options_]

# PARAMETERS

**--display** _TYPE_
> 显示后端类型：drm、x11 或 wayland。

**--device** _PATH_
> DRM 设备路径（如 /dev/dri/renderD128）。仅与 --display drm 配合使用。

**-a**, **--all**
> 显示每个配置文件/入口点对支持的全部属性。

**--help**
> 显示帮助。

# DESCRIPTION

**vainfo** 显示系统上可用的 Video Acceleration API（VA-API）支持情况。它会查询 GPU 驱动，并报告支持哪些视频编解码配置文件，例如 H.264、HEVC、VP9 和 AV1。

输出内容包括 VA-API 驱动名称、版本，以及支持的配置文件及其入口点（编码、解码、视频处理）列表。这些信息对于诊断硬件视频加速问题以及确认 GPU 加载了正确的 VA-API 驱动至关重要。

# CAVEATS

需要安装 VA-API 驱动（如 intel-media-driver、mesa-va-drivers）。输出内容因 GPU 和驱动而异。属于 libva-utils 软件包。

# HISTORY

**vainfo** 属于 **libva-utils**，用于提供 VA-API（Video Acceleration API）支持的相关信息。

# INSTALL

```apt: sudo apt install vainfo```

```dnf: sudo dnf install libva-utils```

```pacman: sudo pacman -S libva-utils```

```apk: sudo apk add libva-utils```

```zypper: sudo zypper install libva-utils```

```nix: nix profile install nixpkgs#libva-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vdpauinfo](/man/vdpauinfo)(1), [glxinfo](/man/glxinfo)(1), [vulkaninfo](/man/vulkaninfo)(1), [ffmpeg](/man/ffmpeg)(1)
