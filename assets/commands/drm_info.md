# TAGLINE

显示 DRM 设备信息

# TLDR

以格式化输出**显示所有 DRM 设备的信息**

```drm_info```

**查询指定的 DRM 设备**

```drm_info [/dev/dri/card0]```

以 JSON 格式**输出设备信息**

```drm_info -j```

向 DRM 数据库**提交 GPU 信息**

```drm_info -j | curl -d @- https://drmdb.emersion.fr/submit```

# SYNOPSIS

**drm_info** [**-j**] [**--**] [_path_...]

# PARAMETERS

**-j**
> 以 JSON 格式输出信息。否则输出为美化打印的格式。

**path**
> 零个或多个要查询的设备路径，如 /dev/dri/card0。省略时，工具会自动扫描 /dev/dri/card* 下的所有可用设备。

**--**
> 选项结束分隔符。

# DESCRIPTION

**drm_info** 是一个用于转储 DRM（Direct Rendering Manager，直接渲染管理器）设备信息的小型实用工具。它查询 Linux 内核的 DRM 子系统，显示可用 GPU 的详细信息，包括其能力、支持的格式、连接器、编码器、CRTC 和平面。

该工具适用于调试显示问题、检查 GPU 功能支持情况，以及为社区 DRM 数据库贡献硬件信息。它能揭示 DRM 驱动为每个图形设备暴露了哪些能力。

# CAVEATS

需要适当的权限才能访问 /dev/dri/ 下的 DRM 设备文件。可能需要以 root 运行或属于 video 组。该工具依赖已安装的 libdrm 和 json-c 库。

# HISTORY

**drm_info** 由 Simon Ser（emersion）创建，托管在 freedesktop.org GitLab 上。它是 drmdb 的数据采集工具——drmdb 是一个跟踪不同硬件上 GPU 和 DRM 驱动功能支持的社区数据库。

# INSTALL

```apt: sudo apt install drm-info```

```dnf: sudo dnf install drm_info```

```pacman: sudo pacman -S drm-info```

```apk: sudo apk add drm_info```

```zypper: sudo zypper install drm_info```

```nix: nix profile install nixpkgs#drm_info```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[amdgpu_top](/man/amdgpu_top)(1), [nvidia-smi](/man/nvidia-smi)(1), [lspci](/man/lspci)(8), [xrandr](/man/xrandr)(1), [modetest](/man/modetest)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/emersion/drm_info)```

<!-- verified: 2026-07-14 -->
