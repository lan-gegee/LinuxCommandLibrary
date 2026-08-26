# TAGLINE

带有 gRPC、GraphQL、HTTP 和 MPD API 的无头 Rockbox 音频引擎守护进程

# TLDR

在前台**启动**守护进程

```rockboxd```

以 **info 级别日志**启动，查看发现的网络渲染器

```RUST_LOG=info rockboxd```

**安装**为 systemd 用户服务

```rockbox service install```

**检查**服务状态

```rockbox service status```

把它当作 MPD 服务器，从任意 MPD 客户端**与它交互**

```mpc -p 6600 [play]```

# SYNOPSIS

**rockboxd**

**rockbox** **service** {**install** | **uninstall** | **status**}

# DESCRIPTION

**rockboxd** 是一个单二进制文件守护进程，内嵌开源的 **Rockbox** 音频引擎，并通过多种协议同时对外提供服务。开箱即用时它监听端口 **6061** 上的 **gRPC**、**6062** 上的 **GraphQL** 加 Web UI、**6063** 上的 **HTTP REST** API，以及 **6600** 端口上与 **MPD 兼容**的服务器，因此同一媒体库和播放状态可以通过 Web、移动端、脚本或任何现有 MPD 客户端控制。

播放继承了 Rockbox 的能力：无缝衔接、replay-gain、软件 DSP 以及支持 20 多种编解码器的解码器。音频可以在本地通过 **CPAL** 渲染，也可以串流到远程输出端，包括 **Snapcast**、**AirPlay**、**Squeezelite**、**Chromecast** 和 **UPnP/DLNA** 渲染器，这使它非常适合作为多房间音响系统的核心。

配套的 **rockbox** 命令可将该守护进程作为 systemd 用户服务进行安装和管理。**rockboxd** 不同于原始的 **Rockbox** 固件（面向便携音乐播放器），也不同于 **rockboxdev.sh** 工具链辅助脚本。

# CONFIGURATION

配置从 **~/.config/rockbox.org/settings.toml** 读取。该文件控制音乐库路径、启用的输出端和监听端口。

```
[library]
music_dir = "~/Music"

[outputs.local]
enabled = true

[outputs.snapcast]
enabled = true
host = "snapserver.lan"
port = 1704

[server]
mpd_port = 6600
grpc_port = 6061
graphql_port = 6062
http_port = 6063
```

日志详细程度由 **RUST_LOG** 环境变量控制（`error`、`warn`、`info`、`debug`、`trace`）。

# CAVEATS

使用 **Chromecast** 输出时，本地端口 **7881** 必须能被局域网中的渲染器访问。**rockboxd** 与 Rockbox 固件无关；不要把它刷写到 DAP 上。配置仅支持 TOML——没有传统的基于标志的 CLI。

# HISTORY

**rockboxd** 是 **Tsiry Sandratraina** 创建的 **rockbox-zig** 项目的一部分。它围绕上游 Rockbox 音频引擎以 Rust 和 Zig 编写，目前活跃维护，已为 Ubuntu、Fedora、Arch、Homebrew 和 Docker 提供软件包。

# SEE ALSO

[mpd](/man/mpd)(1)
