# TAGLINE

用于浏览 Gopher 协议的快捷终端客户端

# TLDR

**以默认 Gopher 页面启动**

```phetch```

**打开指定的 Gopher URL**

```phetch [gopher://example.com]```

**为音频/视频指定自定义媒体播放器**

```phetch -m [mpv]```

**以 TLS 加密打开 URL**

```phetch -s [gopher://example.com]```

**通过 Tor 打开 URL**

```phetch -o [gopher://example.com]```

**打印原始 Gopher 响应而不进入交互模式**

```phetch -r [gopher://example.com]```

**连接本地 Gopher 服务器**

```phetch -l```

# SYNOPSIS

**phetch** [_options_] [_url_]

# PARAMETERS

**-s**, **--tls**
> 尝试通过 TLS 安全地打开 Gopher URL。

**-o**, **--tor**
> 使用本地 Tor 代理打开所有页面。

**-S**, **-O**
> 禁用 TLS 或 Tor。

**-w**, **--wrap** _COLUMN_
> 在文本视图中于第 COLUMN 列折行显示长文本。

**-m**, **--media** _PROGRAM_
> 设置用于打开音视频文件的媒体播放器。

**-M**, **--no-media**
> 只下载媒体文件，不播放。

**-a**, **--autoplay**
> 自动播放媒体文件而不询问。

**-A**, **--no-autoplay**
> 播放媒体文件前先询问。

**-r**, **--raw**
> 只打印原始 Gopher 响应。

**-p**, **--print**
> 只打印渲染后的 Gopher 响应。

**-l**, **--local**
> 连接 127.0.0.1:7070。

**-e**, **--encoding** _ENCODING_
> 以 CP437 或 UTF8 渲染文本文档。

**-c**, **--config** _FILE_
> 使用 FILE 而不是 ~/.config/phetch/phetch.conf。

**-C**, **--no-config**
> 不使用任何配置文件。

**-t**, **--theme** _FILE_
> 使用 FILE 作为配色主题，或打印当前主题。

**-h**, **--help**
> 显示帮助界面。

**-v**, **--version**
> 显示版本。

# DESCRIPTION

**phetch** 是一个用 Rust 编写的小巧快速的终端 Gopher 协议客户端。它支持 Gopher 搜索、文本与菜单页面、文件下载、可选的历史记录、TLS 加密以及 Tor 支持。导航完全由键盘驱动，同时提供跳转到链接和增量搜索两种方式。

# HISTORY

**phetch** 由 **xvxx** 创建，用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#phetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lynx](/man/lynx)(1), [curl](/man/curl)(1), [w3m](/man/w3m)(1)
