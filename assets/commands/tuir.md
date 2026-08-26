# TAGLINE

Reddit 的终端用户界面

# TLDR

**启动 Reddit 浏览器**

```tuir```

**打开指定的 subreddit**

```tuir -s [programming]```

**通过 URL 打开**

```tuir [https://reddit.com/r/linux]```

**打开评论**

```tuir -l [post-url]```

**使用其他主题**

```tuir --theme [molokai]```

# SYNOPSIS

**tuir** [_-s subreddit_] [_--theme name_] [_options_] [_url_]

# PARAMETERS

**-s** _SUBREDDIT_
> 打开 subreddit。

**-l** _URL_
> 打开链接。

**--theme** _NAME_
> 颜色主题。

**--config** _FILE_
> 配置文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**tuir**（Terminal UI for Reddit）在终端中提供功能完整的 Reddit 浏览体验。它以 ncurses 界面显示 subreddit、帖子和嵌套评论，并可用 vim 风格的按键导航。

该工具支持 Reddit 的核心交互，包括投票、评论、订阅 subreddit，以及在外部浏览器或媒体查看器中打开链接。可以浏览多个 subreddit，帖子可按 hot、new、top 和 controversial 排序。

通过 OAuth 身份验证可访问订阅、收藏帖子和用户专属功能。主题可以自定义以匹配终端配色方案。

# KEY BINDINGS

- **j/k** - 导航
- **l/h** - 进入/返回
- **a/z** - 赞/踩
- **c** - 评论

# CAVEATS

受 Reddit API 限制。需要 OAuth 身份验证。是 rtv 的分支。

# HISTORY

**tuir**（Terminal UI for Reddit）是 **rtv**（Reddit Terminal Viewer）被弃用后的持续维护分支。

# INSTALL

```nix: nix profile install nixpkgs#tuir```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rtv](/man/rtv)(1), [newsboat](/man/newsboat)(1)
