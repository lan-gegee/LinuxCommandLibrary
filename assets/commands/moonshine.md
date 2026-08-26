# TAGLINE

面向 Moonlight 客户端的无头（headless）游戏串流服务器

# TLDR

**从** Arch 用户仓库（AUR）**安装**

```yay -S moonshine```

**启用**用户级服务（立即启动并开机自启）

```sudo systemctl enable --now moonshine@$USER```

**允许**服务在你未登录时继续运行

```sudo loginctl enable-linger $USER```

使用配置文件**直接运行**服务器（从源码构建）

```moonshine [/path/to/config.toml]```

提交 PIN 码以**配对** Moonlight 客户端

```curl -X POST "http://localhost:47989/submit-pin" -d "uniqueid=0123456789ABCDEF&pin=[PIN]"```

# SYNOPSIS

**moonshine** _config.toml_

# DESCRIPTION

**moonshine** 是一个仅限 Linux 的无头串流主机，与 [Moonlight](https://moonlight-stream.org/) 客户端兼容。它把游戏（或任何应用）从你的电脑串流到手机、平板等设备，并将键盘、鼠标和手柄输入回传给主机。

与桌面共享类主机不同，每条串流都运行在各自隔离的 Wayland 合成器会话中，与本地桌面相互独立。串流时主机仍可正常使用，且无需物理显示器或 HDMI 假负载。

视频通过 Vulkan 在 NVIDIA RTX、AMD RDNA2+ 或 Intel Arc GPU 上进行硬件编码（H.264、H.265 以及实验性的 AV1）。音频使用低延迟 Opus（立体声或 5.1/7.1）。当游戏和客户端支持时，还支持 HDR（10 位）。客户端需要 Moonlight v6.0.0 或更新版本。启动和管理应用进程需要 systemd。

# PARAMETERS

_config.toml_

> TOML 配置文件的路径。若文件不存在，会自动以默认配置创建。AUR 软件包默认路径为 **$XDG_CONFIG_HOME/moonshine/config.toml**。

**-V**, **--version**

> 输出版本信息并退出。

# CONFIGURATION

**$XDG_CONFIG_HOME/moonshine/config.toml**（通常是 **~/.config/moonshine/config.toml**）

> 主配置文件。定义应用和可选的扫描器。

应用条目示例：

```
[[application]]
title = "Steam"
boxart = "/path/to/steam.png"
command = ["/usr/bin/steam", "steam://open/bigpicture"]
pre_command = [
    ["/usr/bin/systemctl", "stop", "conflicting.service"],
]
post_command = [
    ["/usr/bin/nvidia-smi", "pstate", "performance"],
]
```

Steam 库扫描器（自动发现已安装的游戏）：

```
[[application_scanner]]
type = "steam"
library = "$HOME/.local/share/Steam"
command = ["/usr/bin/steam", "-bigpicture", "steam://rungameid/{game_id}"]
```

桌面扫描器（基于 .desktop 文件）：

```
[[application_scanner]]
type = "desktop"
directories = [
  "$HOME/.local/share/applications",
  "/usr/share/applications",
]
include_terminal = false
resolve_icons = true
```

**MOONSHINE_LOG**

> 用于追踪的日志过滤器环境变量（默认级别：**error**）。传递给 Rust 的 tracing EnvFilter。

首次配对：先用 Moonlight 连接，然后在主机上打开 **http://localhost:47989/pin**（或使用上文的 curl 示例）提交 PIN 码。

# CAVEATS

仅支持 Linux 和 systemd。需要一块支持 Vulkan 视频编码的 GPU。AV1 编码尚属实验性，在某些 NVIDIA 驱动上帧大小可能随时间增长；在修复前建议优先使用 H.264 或 H.265。在公共网络上并不安全：GameStream 协议在应用层并未完全加密——远程访问请使用 VPN（**tailscale**、**wg**/WireGuard），切勿将端口暴露到互联网。

# HISTORY

**Moonshine** 是一个与 Moonlight 兼容的主机的 Rust 重实现，专注于 Linux 上隔离的无头会话。它借鉴了 Sunshine（GameStream 主机 API）、Inputtino（输入设备）和 magic-mirror（Vulkan/Wayland 合成器串流）的思路。

# INSTALL

```aur: yay -S moonshine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [loginctl](/man/loginctl)(1), [steam](/man/steam)(1), [tailscale](/man/tailscale)(1), [wg](/man/wg)(8), [yay](/man/yay)(8)

# RESOURCES

```[Source code](https://github.com/hgaiser/moonshine)```

```[Homepage](https://github.com/hgaiser/moonshine)```

```[Documentation](https://github.com/hgaiser/moonshine#readme)```

<!-- verified: 2026-07-20 -->
