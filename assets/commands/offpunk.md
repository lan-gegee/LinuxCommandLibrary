# TAGLINE

离线优先的命令行浏览器，支持 Gemini、Gopher 和 Web

# TLDR

**以交互方式启动浏览器**

```offpunk```

**打开指定 URL**

```offpunk [gemini://example.com]```

**同步所有收藏内容**以便离线阅读

```offpunk --sync```

**以指定深度同步链接页面**

```offpunk --sync [2]```

**访问内置教程**

```offpunk --tutorial```

# SYNOPSIS

**offpunk** [_options_] [_url_]

# PARAMETERS

**--sync** [_depth_]
> 同步收藏的内容供离线使用。可选的深度参数控制要跟随多少层链接（默认 0）。

**--tutorial**
> 打开内置教程页面。

**--assume-yes**
> 对提示自动回答 yes（适用于基于 cron 的同步）。

**--disable-http**
> 禁用 HTTP/HTTPS 内容抓取。

**--version**
> 显示版本信息。

# DESCRIPTION

**offpunk** 是一款命令行、离线优先的浏览器和订阅阅读器，支持 Gemini、Gopher、Spartan 和 Web 协议。你只需同步一次内容，之后即可在断网状态下浏览和整理这些内容。

在交互式 Shell 中，输入 URL 或链接编号即可导航。使用 `ls` 列出书签，`add` 收藏页面，`help` 查看完整命令列表。内容以 ANSI 格式在终端中渲染。

离线内容以纯文本文件形式缓存在 **~/.cache/offpunk/** 中。该工具包含若干子组件：**netcache** 负责网络缓存，**ansicat** 负责终端渲染，**opnk** 负责文件处理。

# CAVEATS

网页渲染基于文本，可能无法准确显示复杂页面。正确渲染网页内容需要 **python-readability** 和 **python-html2text**。在终端中显示图片需要 **chafa** 或 **timg**。

# HISTORY

**offpunk** 由 **Ploum**（Lionel Dricot）创建，是 **AV-98** Gemini 浏览器的一个分支，使用 **Python** 编写。它强调离线优先浏览和数字极简主义。

# INSTALL

```apk: sudo apk add offpunk```

```nix: nix profile install nixpkgs#offpunk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lynx](/man/lynx)(1), [w3m](/man/w3m)(1), [bombadillo](/man/bombadillo)(1)
