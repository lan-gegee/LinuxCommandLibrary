# TAGLINE

面向 Wayland 合成器的录屏工具

# TLDR

**录制**为 MP4 文件

```wf-recorder -f [output.mp4]```

带**音频**录制

```wf-recorder -a -f [path/to/file_with_audio.webm]```

录制用 slurp 选择的**区域**

```wf-recorder -g "$(slurp)"```

录制指定的**输出**（显示器）

```wf-recorder -o [DP-1] -f [output.mp4]```

使用指定的**编解码器**录制

```wf-recorder -c h264_vaapi -f [output.mp4]```

以自定义**帧率**录制

```wf-recorder -r [30] -f [output.mp4]```

以**恒定帧率**录制（禁用 damage 优化）

```wf-recorder -D -f [output.mp4]```

录制并**覆盖**已有文件

```wf-recorder -y -f [output.mp4]```

# SYNOPSIS

**wf-recorder** [_OPTIONS_]

# PARAMETERS

**-f, --file** _PATH_
> 输出文件路径

**-a, --audio**
> 在录制中包含音频

**-g, --geometry** _WxH+X+Y_
> 录制指定区域

**-c** _CODEC_
> 要使用的视频编解码器（如 h264_vaapi、libx264）

**-C** _CODEC_
> 要使用的音频编解码器

**-o**, **--output** _NAME_
> 录制指定的 Wayland 输出（显示器）

**-r**, **--framerate** _FPS_
> 设置录制帧率

**-d**, **--device** _PATH_
> 用于硬件编码的 DRM 设备

**-p** _KEY=VALUE_
> 传递编解码器专属参数（如 -p crf=20）

**-F** _FILTER_
> FFmpeg 过滤器字符串（如 scale=1280:720）

**-b** _N_
> 使用的 B 帧最大数量

**-B**, **--buffrate** _FPS_
> 编码器的预估帧率（保留 VFR，修复某些编码器如 svt-av1 的 FPS 上限问题）

**-D**, **--no-damage**
> 禁用 damage 优化；即使屏幕无变化也记录每一帧（产生恒定帧率）

**-y**
> 强制覆盖输出文件而不提示

**-h**
> 打印帮助信息

**-v**
> 打印版本信息

# DESCRIPTION

**wf-recorder** 是一款面向使用 wlroots 库的 Wayland 合成器（如 Sway、Hyprland）的录屏工具。它将屏幕捕获为视频文件，可选包含音频，并通过 FFmpeg 支持多种输出格式和编解码器。默认输出文件是当前目录下的 **recording.mp4**。

使用 Ctrl+C 或发送 SIGINT 停止录制。可以用 **slurp** 交互式地选择区域。通过 VAAPI 编解码器支持硬件加速编码。

默认情况下，wf-recorder 只在屏幕更新时请求新帧，产生可变帧率的输出。改用 **-D** 可以恒定帧率连续录制。

# CAVEATS

仅限 Wayland；需要支持 wlr-screencopy 的基于 wlroots 的合成器。录音需要 PipeWire 或 PulseAudio。某些合成器可能需要特定配置才能进行屏幕捕获。输出格式由传给 **-f** 的文件扩展名决定；无法识别的扩展名会导致命令失败。

# INSTALL

```apt: sudo apt install wf-recorder```

```dnf: sudo dnf install wf-recorder```

```pacman: sudo pacman -S wf-recorder```

```apk: sudo apk add wf-recorder```

```zypper: sudo zypper install wf-recorder```

```nix: nix profile install nixpkgs#wf-recorder```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[slurp](/man/slurp)(1), [grim](/man/grim)(1), [ffmpeg](/man/ffmpeg)(1)
