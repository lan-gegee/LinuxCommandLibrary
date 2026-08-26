# TAGLINE

支持多种流媒体协议的实时媒体服务器与代理

# TLDR

以**默认配置**启动 MediaMTX 服务器

```mediamtx```

以**自定义 YAML** 配置路径启动

```mediamtx [path/to/config.yml]```

如果已安装为 unit，则通过 **systemd** 启动

```systemctl start mediamtx```

# SYNOPSIS

**mediamtx** [_config_file_]

# DESCRIPTION

**MediaMTX**（前身为 rtsp-simple-server）是一个支持多种流媒体协议的实时媒体服务器与代理。它可以接收、转码并重新分发来自各种来源的视频/音频流。

支持的协议包括 **RTSP**、**RTMP**、**HLS**、**WebRTC** 和 **SRT**。服务器可以充当 IP 摄像头的代理、转推中心或录制服务器。它支持按需流发布和自动重连。

配置通过 YAML 文件完成，可指定路径、认证、加密以及各协议特有的设置。未提供配置文件时将使用默认设置。

# PARAMETERS

**_config_file_**
> YAML 配置文件的路径（可选；未指定时使用默认配置）

# CAVEATS

需要相应的网络端口可用。默认端口：8554（RTSP/TCP）、8000/8001（RTSP UDP RTP/RTCP）、1935（RTMP）、8888（HLS）、8889（WebRTC HTTP）、8189（WebRTC ICE/UDP）、8890（SRT/UDP）、9997（HTTP API）。对外访问可能需要调整防火墙规则。性能取决于可用于转码操作的 CPU 资源。

# INSTALL

```brew: brew install mediamtx```

```nix: nix profile install nixpkgs#mediamtx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [vlc](/man/vlc)(1)
