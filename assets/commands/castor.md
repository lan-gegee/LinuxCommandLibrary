# TAGLINE

从终端将网络视频流投屏到智能电视

# TLDR

**发现**局域网内的 DLNA/UPnP 投屏目标

```castor scan```

**交互式投屏**（在 TUI 中浏览片名；需要 TMDB API 密钥）

```castor cast```

通过已配置的来源投屏**按 IMDB/TMDB id 指定的电影**

```castor cast movie tt12300742```

按 id 投屏电视**剧集**

```castor cast episode tt2699128 --season 1 --episode 3```

投屏**网页**上正在播放的视频

```castor cast player https://example.com/watch/some-video```

投屏**原始流 URL**

```castor cast url https://example.com/stream.m3u8```

**试运行**投屏（只打印找到的 URL，不发送到电视）

```castor cast movie --dry-run tt33028778```

显示**版本 / 构建**信息

```castor info```

# SYNOPSIS

**castor** [*global-options*] *command* [*args*]

# DESCRIPTION

**castor** 是一个终端工具，它从网页（或直接 URL / 媒体 id）中提取视频流，可选地进行转码，并实时投屏到同一局域网内的智能电视或联网媒体渲染设备。它会启动无头 Chrome，通过 Chrome DevTools Protocol 监听网络流量来定位页面加载的流，然后将该流转发给 DLNA/UPnP 设备（Chromecast 支持为实验性）。

与屏幕镜像不同，Castor 发送的是真实的视频流，因此分辨率和画质得以保留。可选地，基于 whisper 的字幕可以烧录进视频中。Castor 自身**不附带**任何内容目录和内容来源；你在 `config.yaml` 中配置自己有权访问的来源（或直接投屏你已有权访问的页面/URL）。

原生二进制文件需要在 `PATH` 中有 **Chrome/Chromium**、**ffmpeg** 和 **ffprobe**。设备发现使用 SSDP 多播，因此主机必须与电视处于同一网络。

# COMMANDS

**scan**

> 发现局域网内的 DLNA/UPnP（以及实验性的 Chromecast）设备。

**cast**

> 投影片名或流。子命令 / 模式包括交互式浏览（`castor cast`）、`movie`、`episode`、`player`（网页 URL）和 `url`（原始流）。

**info**

> 打印版本和构建信息。

# PARAMETERS

**--config** _file_

> 配置文件路径（默认：当前目录下的 `config.yaml`）。

**--debug**

> 启用详细日志（放在子命令之前的全局标志）。

**--dry-run**

> 配合 `cast movie` 等使用：解析并打印流 URL 而不实际投屏。

**--season** _n_, **--episode** _n_

> `cast episode` 所需的季数和集数。

# CONFIGURATION

Castor 要求工作目录中有 `config.yaml`（或通过 **--config** 指定）。一个最小配置文件需指明目标设备和自己的来源：

```
device:
  name: "Living Room TV"
  type: dlna

sources:
  - proxies: ["https://your-source.example"]
    templates:
      movie: "/embed/movie/{itemID}"
      episode: "/embed/tv/{itemID}/{season}-{episode}"
```

可选的 `tmdb.api_key` 用于启用交互式浏览器。机密信息可以放在同目录的 `config.local.yaml` 中，它会叠加覆盖主配置文件。形如 `CASTOR_SECTION__FIELD` 的环境变量同样可以覆盖设置。自动生成的烧录字幕：

```
whisper:
  enable: true
```

# CAVEATS

设备发现和投屏要求主机与电视处于同一局域网。Docker 只能在真实 Linux 主机上以 `--network host` 方式工作；macOS/Windows 上的 Docker Desktop 无法通过 SSDP 访问局域网。Chromecast 支持为实验性。Castor 是面向流提取与投屏工程的概念验证——它不托管任何内容；只投屏你有权访问的素材。

# INSTALL

```nix: nix profile install nixpkgs#castor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [ffprobe](/man/ffprobe)(1), [chromium](/man/chromium)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/stupside/castor)```

```[Documentation](https://github.com/stupside/castor#readme)```

<!-- verified: 2026-07-19 -->
