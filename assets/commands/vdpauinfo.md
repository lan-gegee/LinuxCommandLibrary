# TAGLINE

显示 VDPAU 视频加速能力

# TLDR

**显示 VDPAU 能力**

```vdpauinfo```

**查询特定的 X display**

```DISPLAY=:0 vdpauinfo```

**仅显示解码器能力**

```vdpauinfo | grep -A20 "Decoder capabilities"```

# SYNOPSIS

**vdpauinfo**

# DESCRIPTION

**vdpauinfo** 查询并显示 VDPAU（Video Decode and Presentation API for Unix）驱动的能力。它会显示哪些视频编解码器可以硬解加速，以及支持的最大分辨率。

输出内容包括 API 版本、支持的解码器配置（MPEG1、MPEG2、H.264、VC1、HEVC、VP9、AV1）、每个编解码器的最大分辨率和宏块限制、视频表面格式以及输出表面能力。

该工具用于验证 VDPAU 是否配置正确，并帮助判断哪些视频内容可以在 NVIDIA 硬件上受益于 GPU 加速。

# OUTPUT SECTIONS

**API version**: VDPAU API 与驱动实现版本。

**Decoder capabilities**: 支持的编解码器及其分辨率限制。

**Video surface formats**: 解码支持的颜色格式。

**Output surface formats**: 视频输出格式。

**Bitmap surface formats**: 叠加层与 OSD 能力。

# ENVIRONMENT

**DISPLAY**
> 要查询的 X display。默认为当前 display。

**VDPAU_DRIVER**
> 覆盖 VDPAU 后端驱动（例如 nvidia、r600、radeonsi）。当有多个 GPU 驱动可用时很有用。

# CAVEATS

不限于 NVIDIA；AMD GPU 通过 Mesa 的 va_gl 或 radeonsi 后端也支持 VDPAU。需要正在运行的 X 服务器。一些较新的编解码器（VP9、AV1）需要较新的驱动和 GPU 支持。输出因 GPU 代际和驱动版本而异。

# HISTORY

**vdpauinfo** 是为 NVIDIA 的 VDPAU API 创建的诊断工具，该 API 于 2009 年随 GeForce 8 系列 GPU 推出。VDPAU 在 Linux 上实现了 GPU 加速视频解码，显著降低了视频播放的 CPU 占用。该工具帮助用户和开发者验证硬件能力。

# INSTALL

```apt: sudo apt install vdpauinfo```

```dnf: sudo dnf install vdpauinfo```

```pacman: sudo pacman -S vdpauinfo```

```apk: sudo apk add vdpauinfo```

```nix: nix profile install nixpkgs#vdpauinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vainfo](/man/vainfo)(1), [nvidia-smi](/man/nvidia-smi)(1), [nvidia-settings](/man/nvidia-settings)(1), [glxinfo](/man/glxinfo)(1), [vulkaninfo](/man/vulkaninfo)(1)
