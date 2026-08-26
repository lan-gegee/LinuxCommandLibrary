# TAGLINE

将 Android 设备的音频转发到电脑

# TLDR

**转发音频**（来自已连接的 Android 设备）

```sndcpy```

按序列号从特定设备**转发音频**

```sndcpy [serial]```

**停止音频转发**

> 在终端中按 **Ctrl+C**（Windows 上也可以断开设备）

# SYNOPSIS

**sndcpy** [_serial_]

# PARAMETERS

_serial_
> 要转发音频的 Android 设备序列号。仅连接一台设备时可省略。

**SNDCPY_PORT**
> 用于覆盖默认转发端口的环境变量（默认：28200）。

# DESCRIPTION

**sndcpy** 通过 USB 或 TCP/IP 将 Android 设备的音频转发到电脑。它作为 **scrcpy**（屏幕复制）的配套工具，可同时转发 Android 设备的视频和音频。其名字是"sound"和"copy"的合成词。

该工具会在 Android 设备上安装一个小应用，用于捕获音频输出并将其流式传输到电脑上的 VLC。设备本身仍会继续播放声音，设备和电脑上的音量可以各自独立控制。

由于依赖 Android 10 引入的 AudioPlaybackCapture API，sndcpy 要求 Android 10 或更高版本。电脑上必须安装 VLC 才能接收并播放音频流。

# CAVEATS

这是一个存在局限的概念验证项目。默认情况下无法捕获面向 Android 9 或更早版本的应用的音频。应用也可以在 manifest 中设置 **allowAudioPlaybackCapture="false"** 来显式禁用音频捕获。网络抖动可能导致 VLC 增加缓冲，从而造成音频延迟。若要在所有应用上可靠地转发音频，建议改用设备与电脑之间的蓝牙配对。

# HISTORY

**sndcpy** 由 Romain Vimont（rom1v）创建，他也是 Android 屏幕镜像工具 **scrcpy** 的开发者。该项目作为概念验证发布，用于展示 Android 10 新的音频捕获能力。虽然功能可用，但作者认为对大多数使用场景而言蓝牙音频转发是更实用的方案，因此该项目未再活跃开发。

# SEE ALSO

[scrcpy](/man/scrcpy)(1), [adb](/man/adb)(1), [vlc](/man/vlc)(1)
