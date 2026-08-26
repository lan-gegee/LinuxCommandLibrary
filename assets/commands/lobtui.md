# TAGLINE

在终端浏览 lobste.rs 的 TUI 工具

# TLDR

**启动 lobste.rs 浏览器**

```lobtui```

# SYNOPSIS

**lobtui** [_options_]

# DESCRIPTION

**lobtui** 是一个用于浏览 lobste.rs 网站的终端用户界面。它抓取站点订阅源，并以可滚动列表的形式显示带主题标签的文章标题。

导航采用类 vim 的按键绑定：**n** 下一页、**p** 上一页、**r** 重新加载、**gg** 跳到顶部、**G** 跳到底部、**o** 在浏览器中打开文章。

# CAVEATS

需要联网以获取 lobste.rs 订阅源。打开文章会启动外部浏览器。

# HISTORY

**lobtui** 由 **pythops** 创建，采用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#lobtui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hackernews-tui](/man/hackernews-tui)(1)
