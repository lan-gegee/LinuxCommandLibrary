# TAGLINE

面向 Linux 桌面音频的声音服务器

# TLDR

**检查**是否正在运行

```pulseaudio --check```

**启动**守护进程

```pulseaudio --start```

**终止**守护进程

```pulseaudio -k```

列出可用的**模块**

```pulseaudio --dump-modules```

**加载**一个模块

```pulseaudio -L "[module_name] [args]"```

# SYNOPSIS

**pulseaudio** [**--start**] [**-k**|**--kill**] [**--check**] [**-L** _module_]

# PARAMETERS

**--start**
> 在后台启动守护进程

**-k, --kill**
> 终止正在运行的守护进程

**--check**
> 检查守护进程是否在运行（通过退出码）

**--dump-modules**
> 列出可用模块

**-L, --load _module_**
> 将模块加载到运行中的守护进程

**--dump-conf**
> 导出默认配置

**-D, --daemonize**
> 启动后转为守护进程

# DESCRIPTION

**pulseaudio** 是一个声音服务器，在应用程序和音频硬件之间提供软件混音层。它允许多个应用程序共享音频设备，并提供按应用程序控制音量等特性。

该守护进程以每个用户为单位运行，通常由桌面会话自动启动。它支持网络音频流传输和各种音频处理模块。

# CONFIGURATION

**~/.config/pulse/default.pa**
> 每用户启动脚本，用于加载模块、设置默认的 sink/source 并配置音频路由。

**/etc/pulse/daemon.conf**
> 系统级守护进程设置，控制采样率、缓冲区大小、重采样方法和资源限制。

**/etc/pulse/default.pa**
> 系统级启动脚本，定义要加载哪些模块及其配置。

# CAVEATS

在现代系统上正被 PipeWire 取代。可能与专业音频领域的 JACK 冲突。默认是用户级守护进程，而非系统级。配置位于 ~/.config/pulse/。

# HISTORY

**PulseAudio** 由 Red Hat 的 **Lennart Poettering** 创建，旨在为 Linux 桌面提供现代化的声音服务器。在 PipeWire 出现并成为其继任者之前，它是大多数发行版的默认音频系统。

# INSTALL

```apt: sudo apt install pulseaudio```

```dnf: sudo dnf install pulseaudio```

```pacman: sudo pacman -S pulseaudio```

```apk: sudo apk add pulseaudio```

```zypper: sudo zypper install pulseaudio```

```brew: brew install pulseaudio```

```nix: nix profile install nixpkgs#pulseaudio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pactl](/man/pactl)(1), [pavucontrol](/man/pavucontrol)(1), [pipewire](/man/pipewire)(1)
