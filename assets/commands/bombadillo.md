# TAGLINE

支持 Gopher、Gemini 和 Finger 协议的终端浏览器

# TLDR

**启动** Bombadillo

```bombadillo```

**打开**指定的 Gopher URL

```bombadillo [gopher://example.com]```

**打开** Gemini URL

```bombadillo [gemini://example.com]```

# SYNOPSIS

**bombadillo** [_options_] [_url_]

# DESCRIPTION

**bombadillo** 是一款专为终端设计的非 Web 浏览器。它支持 **Gopher**、**Gemini** 和 **Finger** 协议以及本地文件浏览。它提供类似 vim 的模式化界面和命令行导航，用于探索"小互联网"——现代 Web 之外的替代协议。

该浏览器直接在终端中渲染文本内容，支持书签、历史记录导航和可配置的设置。它可以处理 Gemini 的 TLS 连接，并提供不受干扰的阅读体验。

# PARAMETERS

**-v**
> 显示版本信息并退出。

**-t**
> 将终端窗口标题设置为 "Bombadillo"。

**-h**
> 显示用法帮助并退出。

# CONFIGURATION

配置存储在 **~/.config/bombadillo/config.ini** 中。设置项包括默认协议、主页 URL、证书处理和显示偏好。也可以在运行时使用 **:set** 命令更改设置。

# CAVEATS

不原生支持 HTTP/HTTPS——它是专为替代协议设计的，不过可以通过配置的外部处理器打开 HTTP/HTTPS 链接。Gemini TLS 证书处理采用首次使用即信任（TOFU）机制。媒体文件会交给外部处理器处理。导航使用类 vim 键绑定：`j`/`k` 滚动，`b` 后退，`f` 前进，`g`/`G` 跳转到顶部/底部，`q` 退出。

# HISTORY

**Bombadillo** 由 **sloum**（在 tildegit 上）创建，于 **2019 年**前后首次发布。它以 **Go** 编写，是人们对 Gemini 协议和小互联网运动日益浓厚的兴趣的产物。名字来源于托尔金作品中的角色 Tom Bombadil。

# INSTALL

```apt: sudo apt install bombadillo```

```apk: sudo apk add bombadillo```

```brew: brew install bombadillo```

```nix: nix profile install nixpkgs#bombadillo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lynx](/man/lynx)(1), [w3m](/man/w3m)(1)
