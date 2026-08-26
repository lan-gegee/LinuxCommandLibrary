# TAGLINE

基于无头 Firefox 的文本网页浏览器

# TLDR

**启动 browsh**

```browsh```

打开指定的 URL

```browsh --startup-url [https://example.com]```

以 HTTP 服务器模式运行

```browsh --http-server-mode --port [4333]```

使用指定的 Firefox 可执行文件

```browsh --firefox.path [/path/to/firefox]```

# SYNOPSIS

**browsh** [_options_]

# PARAMETERS

**--startup-url** _URL_
> 启动时打开指定 URL。

**--http-server-mode**
> 以 HTTP 服务器方式运行，将页面渲染为文本。

**--port** _PORT_
> 设置 HTTP 服务器模式的端口（默认：4333）。

**--firefox.path** _PATH_
> Firefox 可执行文件的路径。

**--time-limit** _SECONDS_
> 限制会话时长。

# DESCRIPTION

**browsh** 是一款完全现代化的文本网页浏览器。它在后台运行无头 **Firefox** 实例来渲染网页，并将视觉输出转换为文本和 ANSI 字符画以便在终端中显示。这意味着它支持 JavaScript、CSS、视频以及几乎所有现代 Web 标准。

该浏览器提供交互式终端模式和 HTTP 服务器模式，后者可将文本渲染的网页提供给任意客户端。它支持标签页、滚动、链接导航和文本输入。

# CAVEATS

需要完整的 **Firefox** 安装（版本 57+）作为后端，因此与传统的文本浏览器相比资源占用较高。渲染质量取决于终端能力和字体支持。由于需要初始化 Firefox，启动速度较慢。

# HISTORY

**browsh** 由 **Thomas Sherwood** 创建，于 **2018** 年发布。它因使用真实浏览器引擎驱动终端界面的新颖思路而备受关注，实现了 Lynx 等传统文本浏览器无法达到的完整 Web 兼容性。

# INSTALL

```aur: yay -S brows```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[browsh](/man/browsh)(1), [lynx](/man/lynx)(1), [w3m](/man/w3m)(1), [links](/man/links)(1), [elinks](/man/elinks)(1)
