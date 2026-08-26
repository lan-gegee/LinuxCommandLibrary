# TAGLINE

硬件加速的屏幕录制工具

# TLDR

通过**桌面门户**选择源并录制

```gpu-screen-recorder -w portal -o [path/to/video.mp4]```

指定**特定的视频源**

```gpu-screen-recorder -w [screen|DP-1|HDMI-A1|...] -o [path/to/video.mp4]```

列出**视频采集**源

```gpu-screen-recorder --list-capture-options```

列出**音频采集**设备

```gpu-screen-recorder --list-audio-devices```

使用**回放缓冲区**录制

```gpu-screen-recorder -w screen -r 30 -c mp4 -ro [path/to/directory] -o whatever```

从回放缓冲区**保存**视频

```pkill -SIGUSR1 -f gpu-screen-recorder```

在**后台**运行 gpu-screen-recorder

```systemctl start --user gpu-screen-recorder```

# SYNOPSIS

**gpu-screen-recorder** [_options_] **-w** _source_ **-o** _output_

# PARAMETERS

**-w** _SOURCE_
> 视频源：窗口 ID、显示器名称、focused、portal、region 或 V4L2 设备路径。可用 | 组合。

**-o** _FILE_
> 输出文件路径，回放模式下为目录。

**-r** _SECONDS_
> 回放缓冲区时长（秒）（2-86400）。仅在收到信号时才保存。

**-ro** _DIR_
> 回放/串流模式下的常规录制输出目录。

**-c** _CONTAINER_
> 容器格式：mp4、mkv、flv、webm。默认根据文件扩展名判断。

**-f** _FPS_
> 帧率（默认：60）。

**-fm** _cfr|vfr|content_
> 帧率模式（默认：vfr）。

**-k** _CODEC_
> 视频编解码器：auto、h264、hevc、av1、vp8、vp9、hevc_hdr、av1_hdr（默认：auto）。

**-q** _QUALITY_
> 质量预设：medium、high、very_high、ultra（默认：very_high）。在 CBR 模式下指定比特率。

**-bm** _auto|qp|vbr|cbr_
> 比特率模式（默认：auto）。回放/串流建议使用 CBR。

**-a** _SOURCE_
> 音频源：default_output、default_input、device:name 或 app:name。可重复使用。

**-ac** _aac|opus|flac_
> 音频编解码器（mp4/mkv 默认为 opus，其他为 aac）。

**-s** _WxH_
> 输出分辨率上限。使用 0x0 表示原始分辨率。

**-cr** _limited|full_
> 色彩范围（默认：limited）。

**-cursor** _yes|no_
> 是否包含鼠标光标（默认：yes）。

**-encoder** _gpu|cpu_
> 编码设备（默认：gpu）。CPU 仅限 H264。

**-keyint** _SECONDS_
> 关键帧间隔（秒）（默认：2.0）。

**--list-capture-options**
> 列出可用的视频采集源。

**--list-audio-devices**
> 列出可用的音频设备。

**--list-application-audio**
> 列出可用的应用程序音频名称。

# DESCRIPTION

**gpu-screen-recorder** 是一个硬件加速的屏幕录制工具，它使用 GPU 编码（NVIDIA NVENC、AMD VAAPI/AMF 或 Intel VAAPI）以将对 CPU 的影响降到最低。它支持 H264、HEVC、AV1、VP8 和 VP9 编解码器。

主要功能包括回放缓冲区（像即时回放一样记录最近 N 秒的内容）、通过门户同时支持 X11 和 Wayland，以及高效的硬件编码。向进程发送 SIGUSR1 即可保存回放缓冲区，发送 SIGINT 可干净地停止录制。该工具支持多显示器、特定窗口捕获、区域捕获，以及系统声音和麦克风的同步录音。还提供 CPU 后备编码器用于 H264。

# CAVEATS

需要支持硬件编码的 GPU（带 NVENC 的 NVIDIA、带 VAAPI/AMF 的 AMD，或带 VAAPI 的 Intel）。Wayland 支持取决于桌面门户的实现。某些桌面环境可能需要额外配置。

# HISTORY

gpu-screen-recorder 的诞生是为了提供一种基于软件的屏幕录制工具之外的高效 GPU 加速替代方案。它以低开销和即时回放能力在 Linux 游戏玩家中尤为流行。

# INSTALL

```pacman: sudo pacman -S gpu-screen-recorder```

```zypper: sudo zypper install gpu-screen-recorder```

```nix: nix profile install nixpkgs#gpu-screen-recorder```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[obs](/man/obs)(1), [ffmpeg](/man/ffmpeg)(1), [wf-recorder](/man/wf-recorder)(1)
