# TAGLINE

在终端中进行网络搜索

# TLDR

使用默认搜索引擎（presearch）**进行网络搜索**

```s [query]```

**使用指定搜索引擎搜索**，例如 Google

```s -p google [query]```

在 Amazon 上**搜索商品**

```s -p amazon [wireless keyboard]```

**按标签搜索**（例如视频网站）

```s -t video [query]```

**列出所有可用的**搜索引擎

```s -l```

只输出搜索 URL 而**不打开浏览器**

```s -o [query]```

**使用指定的浏览器程序**搜索

```s -b "[firefox --private-window]" [query]```

**启动 Web 服务器**界面

```s -s --port [8080]```

# SYNOPSIS

**s** [_options_] [_query_]

# PARAMETERS

**-p**, **--provider** _name_
> 指定搜索引擎（默认：presearch）。支持部分匹配。

**-t**, **--tag** _tag_
> 使用按标签筛选的引擎进行搜索（如 video、images、code）

**-b**, **--binary** _path_
> 用于打开搜索结果的浏览器或应用程序

**-o**, **--output**
> 仅输出模式；打印 URL 而不启动浏览器

**-l**, **--list-providers**
> 显示所有可用的搜索引擎

**--list-tags**
> 显示可用的标签类别

**-s**, **--server**
> 启动 Web 服务器界面，以便通过浏览器搜索

**--port** _number_
> 服务器端口号（默认：8080）

**-c**, **--cert** _file_
> 服务器模式下 TLS 证书文件的路径

**-k**, **--key** _file_
> 服务器模式下 TLS 密钥文件的路径

**-v**, **--verbose**
> 启用详细输出

**--completion** _shell_
> 生成 Shell 补全脚本（bash、zsh、fish）

**--version**
> 显示版本信息

# DESCRIPTION

**s** 是一款可直接在终端执行网络搜索的命令行工具。它会在你的默认浏览器中打开搜索结果，支持超过 100 个搜索引擎，包括 Google、DuckDuckGo、Wikipedia、YouTube、GitHub、Amazon、Reddit 和 Stack Overflow。

该工具支持对引擎名称的部分匹配，因此可以使用 **s -p g query** 这样的快捷方式调用 Google。还可以按 **video**、**images** 或 **code** 等标签筛选引擎，一次搜索多个相关网站。

配置以 UCL 格式存储在 **~/.config/s/config** 中。你可以设置默认引擎、将引擎加入黑名单/白名单、定义自定义引擎，以及配置浏览器偏好。

# CAVEATS

**s** 命令需要浏览器来显示结果。在无显示器的环境中，请改用 **-o** 输出 URL。可用引擎取决于所安装的版本；部分引擎可能随时间变化或不再可用。

# HISTORY

**s** 由 **Josh Ellithorpe**（zquestz）创建，约于 **2016 年**首次发布在 **GitHub** 上。它采用 **Go** 编写，旨在简化开发者工作流中的网络搜索。该项目现已支持超过 100 个搜索引擎。

# INSTALL

```aur: yay -S s```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ddgr](/man/ddgr)(1), [googler](/man/googler)(1), [surfraw](/man/surfraw)(1)
