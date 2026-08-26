# TAGLINE

终端中的 Hacker News 客户端

# TLDR

以交互方式**浏览** Hacker News

```clx```

启用 Nerd Fonts 图标进行**浏览**

```clx -n```

将评论宽度**设置**为 80 字符

```clx -c 80```

按 ID **阅读**某个提交的评论

```clx comments [33192518]```

按 URL 在阅读模式（Reader Mode）中**阅读**文章

```clx url [https://example.com/article]```

将一个提交**添加**到收藏夹

```clx add [33192518]```

**清除**浏览历史

```clx clear```

只**显示**指定的分类

```clx --categories="ask,show"```

# SYNOPSIS

**clx** [_flags_]
**clx** [_command_] [_arguments_]

# PARAMETERS

**-a**, **--auto-expand**
> 自动展开评论线程中的所有回复。

**--categories=**_string_
> 设置可见的分类（默认："top,best,ask,show"）。

**-c**, **--comment-width=**_int_
> 以字符为单位设置评论宽度（默认：70）。

**-e**, **--disable-emojis**
> 禁用输出中的 emoji 转换。

**-d**, **--disable-history**
> 禁用将提交标记为已读。

**-t**, **--hide-indent**
> 隐藏评论中的缩进引导线。

**-n**, **--nerdfonts**
> 启用 Nerd Fonts 图标。

**-o**, **--plain-comments**
> 禁用评论中的语法高亮。

**-p**, **--plain-headlines**
> 禁用标题中的语法高亮。

**-v**, **--version**
> 显示版本号。

# SUBCOMMANDS

**add** _id_
> 按 Hacker News ID 将一个提交添加到收藏夹。

**comments** _id_
> 直接跳转到某个提交的评论区。

**article** _id_
> 在阅读模式中阅读所链接的文章。

**url** _url_
> 在阅读模式中打开任意 URL。

**clear**
> 删除浏览历史。

# DESCRIPTION

**circumflex**（二进制名为 **clx**）是一个基于终端的 Hacker News 客户端，使用 Bubble Tea TUI 框架构建。它让你无需离开终端即可浏览新闻、以语法感知的格式阅读评论线程，并在阅读模式中查看链接的文章。

评论会经过美化排版并通过管道传给 **less**，代码片段、@提及、变量和 URL 均有语法高亮。彩虹色的缩进引导线用于区分嵌套层级。该工具会跟踪已读历史、高亮自上次访问以来的新评论，并支持将收藏保存为美化排版的 JSON 文件至 **~/.config/circumflex/favorites.json**。

# CAVEATS

需要较新版本的 **less** 作为分页器。依赖 Algolia 的 Hacker News Search API 和 cheeaun 的非官方 HN API；任一服务宕机都会影响功能。它使用不可见的 Unicode 字符在 less 中实现自定义快捷键，这在某些终端配置下可能引发问题。可通过 **CLX_BROWSER** 环境变量覆盖默认浏览器。

# HISTORY

**circumflex** 由 **bensadeh** 创建，于 **2022 年 10 月**在 Hacker News 上公开发布。使用 Go 编写，基于 Bubble Tea TUI 框架，采用 AGPL-3.0 许可证。

# INSTALL

```brew: brew install circumflex```

```nix: nix profile install nixpkgs#circumflex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [newsboat](/man/newsboat)(1), [w3m](/man/w3m)(1), [lynx](/man/lynx)(1)
