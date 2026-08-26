# TAGLINE

安全地运行带 GUI 的 Docker 容器

# TLDR

**运行 GUI 应用**

```x11docker [image] [command]```

**启用 GPU 加速**

```x11docker --gpu [image] [command]```

**共享家目录**

```x11docker --home [image]```

**启用音频**

```x11docker --pulseaudio [image]```

**共享剪贴板**

```x11docker --clipboard [image]```

# SYNOPSIS

**x11docker** [_--gpu_] [_--home_] [_--pulseaudio_] [_options_] _image_ [_command_]

# PARAMETERS

**--gpu**
> 启用硬件 OpenGL 加速。

**--home**
> 在主机上为容器提供一个持久的独立家目录。

**--pulseaudio**
> 启用 PulseAudio 声音支持。

**--alsa**
> 启用 ALSA 声音支持。

**--pipewire**
> 启用 PipeWire 声音支持。

**--clipboard**
> 在主机和容器之间共享剪贴板。

**--desktop**
> 运行完整的桌面环境而不是单个应用程序。

**--xephyr**
> 使用 Xephyr 嵌套 X 服务器（默认回退方案）。

**--xpra**
> 使用 Xpra 作为 X 服务器后端。

**--nxagent**
> 使用 nxagent 作为 X 服务器后端。

**--wayland**
> 在 Wayland 合成器中运行。

**--hostdisplay**
> 共享主机的 X socket（安全性较低，作为回退方案）。

**--share** _PATH_
> 将主机的文件或文件夹共享给容器。

**--network**, **-I**
> 允许容器访问网络。

**--init** _SYSTEM_
> 使用 init 系统（如 systemd、runit、tini）。

**--backend** _BACKEND_
> 选择容器后端：docker、podman 或 host。

**--webcam**
> 与容器共享摄像头。

**--printer**
> 共享主机的 CUPS 打印机。

**--user** _USER_
> 以指定用户身份运行容器。

# DESCRIPTION

**x11docker** 从 Docker 容器中运行图形应用，并提供安全的 X11 显示转发。它使用 Xephyr、Xpra 和 nxagent 等多种后端提供隔离的显示访问，防止容器直接访问主机的 X 服务器。

该工具支持 GPU 硬件加速、PulseAudio 集成以及容器与主机之间的剪贴板共享。这种注重安全的方式允许在容器中运行不可信的 GUI 应用，同时保持其与主机桌面环境的显示隔离。

# CAVEATS

需要 Docker 或 Podman。主机上至少要安装一个嵌套 X 服务器后端（Xephyr、Xpra、nxagent 或 Xwayland）。使用 **--hostdisplay** 会降低隔离性。GPU 加速要求容器内有兼容的驱动。

# HISTORY

**x11docker** 由 **Martin Viereck** 创建，目的是在保护主机安全的前提下运行带 GUI 应用的 Docker 容器。它早于现代 Wayland 原生的容器化工作流出现，至今仍是桌面容器化的常用方案。

# INSTALL

```dnf: sudo dnf install x11docker```

```nix: nix profile install nixpkgs#x11docker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [xhost](/man/xhost)(1), [xephyr](/man/xephyr)(1)
