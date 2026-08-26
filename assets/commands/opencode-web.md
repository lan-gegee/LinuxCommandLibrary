# TAGLINE

以 Web 界面启动 OpenCode

# TLDR

在随机本地端口上**以 Web UI 启动 OpenCode**

```opencode web```

**绑定到所有网络接口**并使用固定端口（用于远程访问）

```opencode web --hostname 0.0.0.0 --port [4096]```

**通过 mDNS/Bonjour 广播服务**

```opencode web --mdns```

为跨源浏览器客户端**启用 CORS**

```opencode web --cors```

将服务器日志**流式输出到终端**

```opencode web --print-logs --log-level debug```

# SYNOPSIS

**opencode web** [_options_]

# PARAMETERS

**--hostname** _HOST_
> 要绑定的网络接口（默认 **127.0.0.1**）。

**--port** _PORT_
> TCP 端口（默认 **0** —— 自动选择临时端口）。

**--mdns**
> 通过 mDNS 在本地网络上宣告该服务器。

**--mdns-domain** _DOMAIN_
> 覆盖 mDNS 服务域名（默认 **.local**）。

**--cors**
> 允许来自浏览器的跨源请求。

**--print-logs**
> 将服务端日志打印到终端。

**--log-level** _LEVEL_
> 日志详细程度：**trace**、**debug**、**info**、**warn**、**error**。

**-h**, **--help**, **-v**, **--version**
> 显示帮助或版本信息。

# DESCRIPTION

**opencode web** 启动一个无头 OpenCode 服务器，提供基于 Web 的界面而非终端 TUI。这样可以通过浏览器与 OpenCode 交互，适用于远程访问、共享会话，或在你更倾向于图形界面而非终端时使用。启用 **--mdns** 后，无需知道 IP 地址即可在本地网络上发现该服务。

# INSTALL

```pacman: sudo pacman -S opencode```

```brew: brew install opencode```

```nix: nix profile install nixpkgs#opencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opencode](/man/opencode)(1), [opencode-session](/man/opencode-session)(1)
