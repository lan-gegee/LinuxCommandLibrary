# TAGLINE

面向终端的现代文本网页浏览器

# TLDR

**启动 browsh**

```browsh```

**打开指定的** URL

```browsh [https://example.com]```

以可见的 Firefox **图形界面窗口**运行而非无头模式

```browsh --firefox.with-gui```

**使用自定义的** Firefox **可执行文件路径**

```browsh --firefox.path [/path/to/firefox]```

以 HTTP 服务器模式运行，供浏览器访问

```browsh --http-server-mode```

连接到已在运行的 Firefox 实例

```browsh --firefox.use-existing```

# SYNOPSIS

**browsh** [_options_] [_url_]

# DESCRIPTION

**browsh** 是一款完全现代化的文本浏览器，可渲染到 TTY 终端。它使用无头的 Mozilla Firefox 获取并渲染网页，然后将输出转换为 ANSI 或 Unicode 字符以便在终端显示。

该浏览器支持 HTML5、CSS3、JavaScript、图片、WebGL 内容以及在终端内播放视频。

# PARAMETERS

**--firefox.path** _path_
> Firefox 可执行文件的路径。默认为 "firefox"。

**--firefox.use-existing**
> 连接到已在运行的 Firefox 实例而不是启动新实例。Firefox 必须已用 --marionette 标志启动。

**--firefox.with-gui**
> 以可见的图形界面窗口运行 Firefox，而非无头模式。

**--http-server-mode**
> 以 HTTP 服务器模式运行，供浏览器访问。

**--startup-url** _url_
> 启动时打开的 URL。默认为 "https://google.com"。

**--time-limit** _seconds_
> 在指定秒数后终止 browsh。

**--debug**
> 启用调试日志，输出到 ./debug.log。

# KEY BINDINGS

**ALT+SHIFT+p**
> 截取屏幕截图。

**ALT+m**
> 切换单色模式（有助于解决渲染问题）。

**ALT+u**
> 在桌面版和移动版用户代理之间切换。

**CTRL+q**
> 退出 browsh。

**F1**
> 显示帮助。

# REQUIREMENTS

系统需安装 Firefox 57 或更新版本。浏览器以无头模式运行 Firefox，并通过一个 webextension 捕获并转换渲染输出。

# CAVEATS

由于要运行完整的 Firefox 实例，资源占用较高。最适合在 SSH 连接中用于节省带宽。公共演示服务器（ssh brow.sh）上的会话限制为 5 分钟且会被记录。

# HISTORY

Browsh 的诞生是为了替代 Lynx 等文本浏览器，能够渲染重度依赖 JavaScript 和 CSS 的现代网站。

# INSTALL

```nix: nix profile install nixpkgs#browsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lynx](/man/lynx)(1), [w3m](/man/w3m)(1), [links](/man/links)(1), [elinks](/man/elinks)(1), [firefox](/man/firefox)(1)
