# TAGLINE

将 RSS 订阅源转换为邮件

# TLDR

**将 RSS 转换为邮件**

```r2e run```

**添加订阅源**

```r2e add [name] [url] [email]```

**列出订阅源**

```r2e list```

**删除订阅源**

```r2e delete [name]```

**创建配置**

```r2e new [email]```

# SYNOPSIS

**r2e** _command_ [_options_]

# PARAMETERS

**run**
> 处理订阅源。

**add** _NAME_ _URL_ _EMAIL_
> 添加订阅源。

**list**
> 列出订阅源。

**delete** _NAME_
> 移除订阅源。

**new** _EMAIL_
> 初始化配置。

# DESCRIPTION

**r2e**（rss2email）监控 RSS 和 Atom 订阅源，并将新条目以独立邮件的形式发送到指定地址。它在基于 Web 的内容聚合与基于邮件的阅读工作流之间架起桥梁，让用户能够通过现有的邮件客户端关注博客、新闻网站和其他订阅源。

该工具会在多次运行之间维护状态，记录哪些条目已经发送过，因此每次执行 **r2e run** 只会投递新条目。订阅源通过 **add**、**list** 和 **delete** 子命令管理；由 **r2e new** 创建的初始配置会设定默认收件地址。它支持 SMTP 投递和本地 sendmail 两种发信方式。

# CAVEATS

需要先配置好邮件。Python 软件包。

# HISTORY

rss2email 为 **RSS 转邮件**投递而生。

# INSTALL

```dnf: sudo dnf install rss2email```

```pacman: sudo pacman -S rss2email```

```apk: sudo apk add rss2email```

```zypper: sudo zypper install rss2email```

```nix: nix profile install nixpkgs#rss2email```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feed2exec](/man/feed2exec)(1), [newsboat](/man/newsboat)(1)
