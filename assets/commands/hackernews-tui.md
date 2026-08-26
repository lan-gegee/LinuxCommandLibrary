# TAGLINE

浏览 Hacker News 的终端界面应用

# TLDR

**启动 hackernews-tui** 浏览首页文章

```hackernews-tui```

**浏览指定页面的**文章

```hackernews-tui --page [page_type]```

# SYNOPSIS

**hackernews-tui** [_options_]

# DESCRIPTION

**hackernews-tui** 是一款快速且可定制的浏览 Hacker News 的终端应用程序。它提供完整的 TUI 和**类 vim 的按键绑定**，用于浏览文章、评论和讨论。该应用内置阅读视图，无需网页浏览器即可直接在终端中查看文章。

它使用 **HN Algolia API** 和 **HN Official API** 获取数据，支持首页文章、最新文章、Ask HN、Show HN 以及职位列表。文章可以在外部浏览器中打开，评论则以嵌套线程的形式展示。

# KEY BINDINGS

**j/k** — Move down/up
**Enter** — Open story/comment
**o** — Open link in browser
**b** — Go back
**/** — Search
**q** — Quit

# CONFIGURATION

配置存储于 **$XDG_CONFIG_HOME/hackernews-tui/config.toml**。可配置项包括自定义按键绑定、配色主题和外部浏览器命令。

# CAVEATS

需要联网获取文章。阅读视图可能无法完美渲染所有网页。HN API 的速率限制可能影响重度使用。

# HISTORY

**hackernews-tui** 由 **aome510** 创建，使用 **Rust** 编写，基于 **Cursive** TUI 库。它于 **2021 年**首次发布，为 Hacker News 读者提供原生的终端体验。

# INSTALL

```nix: nix profile install nixpkgs#hackernews-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[circumflex](/man/circumflex)(1), [curl](/man/curl)(1)
