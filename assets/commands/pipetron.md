# TAGLINE

面向 Electron 音频流的 PipeWire 节点管理器

# TLDR

**启动** pipetron 守护进程

```pipetron --daemon```

仅**启动**音量守护进程

```pipetron --volume-daemon```

**启动**音频守护进程（实验性）

```pipetron --audio-daemon```

**显示**版本信息

```pipetron --version```

# SYNOPSIS

**pipetron** [**-d**|**-vd**|**-ad**] [**-h**] [**-v**]

# PARAMETERS

**-d**, **--daemon**
> 按配置文件中的指定启动守护进程。

**-vd**, **--volume-daemon**
> 专门启动音量守护进程。

**-ad**, **--audio-daemon**
> 启动音频守护进程（实验性）。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本详情。

# DESCRIPTION

**pipetron** 是一个 PipeWire 节点管理器，用于修复 Electron 应用的一个长期问题：在基于 PipeWire 的音频管理器中，它们的所有音频流都显示为 "Chromium"。这导致在 **pavucontrol** 等音量控制器中无法区分不同的 Electron 应用。

Pipetron 以每个 Electron 应用实际的名称和图标复制其音频流，然后从复制的流到对应的 Electron 流执行单向音量同步。这样，**WirePlumber** 就能正确保存每个应用的音量设置。

该工具通常以 **systemd 用户服务**的形式在后台运行，并在登录时自动启动。

# CONFIGURATION

配置存储在 **~/.config/pipetron/config.toml** 中。该 TOML 文件指定要运行的守护进程类型及相关设置。

# CAVEATS

需要 **PipeWire** 作为音频服务器。只对基于 Electron 的应用有效。音频守护进程模式为实验性功能。该工具以后台服务方式运行，不提供交互式终端界面。

# HISTORY

**pipetron**（PipeWire 与 Electron 的合成词）的诞生是为了解决 Electron 应用无法在 PipeWire 下设置正确音频流名称这一普遍问题。该项目托管在 **Codeberg** 并镜像到 GitHub，已打包进 **Arch Linux AUR**。

# INSTALL

```aur: yay -S pipetron```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pavucontrol](/man/pavucontrol)(1), [wireplumber](/man/wireplumber)(1)
