# TAGLINE

Stack Overflow 的终端界面

# TLDR

**使用默认设置搜索**

```so [how do i reverse a list in python]```

**搜索特定的 StackExchange 站点**

```so --site [tex] [how to put tilde over character]```

**通过 Google 搜索多个站点**

```so -e google -s [askubuntu] -s [unix] [how do i install linux]```

# SYNOPSIS

**so** [_options_] _query_

# PARAMETERS

**--site**, **-s** _SITE_
> 要搜索的 StackExchange 站点。可以多次指定。

**-e** _ENGINE_
> 搜索后端：stackexchange、google 或 duckduckgo。

# DESCRIPTION

**so** 是一个 TUI 工具，让你可以直接在终端中搜索并浏览整个 StackExchange 网络的答案。它支持多种搜索后端（StackExchange API、Google、DuckDuckGo）、同时查询多个站点、可配置主题以及系统集成剪贴板。

# HISTORY

**so** 由 **Sam Tay** 创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install so```

```nix: nix profile install nixpkgs#so```

<!-- packages: 2026-07-22 -->

# SEE ALSO
