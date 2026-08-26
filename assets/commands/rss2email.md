# TAGLINE

将 RSS 订阅源条目转发到电子邮箱

# TLDR

**初始化配置**

```r2e new [email@example.com]```

**添加订阅源**

```r2e add [feed_name] [https://example.com/feed.xml]```

**运行（发送邮件）**

```r2e run```

**列出订阅源**

```r2e list```

**删除订阅源**

```r2e delete [feed_name]```

# SYNOPSIS

**r2e** _command_ [_options_]

# COMMANDS

**new** _email_
> 用默认邮箱地址进行初始化。

**add** _name_ _url_
> 添加订阅源。

**run**
> 处理订阅源并发送邮件。

**list**
> 列出订阅源。

**delete** _name_
> 移除订阅源。

**reset** _name_
> 重置订阅源的日期。

**opmlimport** _file_
> 导入 OPML。

# DESCRIPTION

**rss2email**（r2e）把 RSS/Atom 订阅源转换为电子邮件。它会检查各个订阅源并把新条目发送到你的邮箱，让你可以直接在邮件客户端里阅读订阅内容。

# EXAMPLES

```bash
# Initialize
r2e new user@example.com

# Add feeds
r2e add hackernews https://news.ycombinator.com/rss
r2e add lwn https://lwn.net/headlines/rss

# List feeds
r2e list

# Run manually
r2e run

# Reset feed (resend all)
r2e reset hackernews

# Import OPML
r2e opmlimport feeds.opml
```

# CONFIGURATION

```ini
# ~/.config/rss2email.cfg
[DEFAULT]
from = rss2email@example.com
to = user@example.com
smtp-server = localhost
```

# CRON

```bash
# Run every hour
0 * * * * r2e run
```

# CAVEATS

需要可用的邮件设置（SMTP 或本地投递）。状态保存在 ~/.local/share/rss2email/ 目录中。请通过 cron 定期运行。

# HISTORY

rss2email 由 **Aaron Swartz** 于 2004 年创建，目前由社区维护。

# INSTALL

```dnf: sudo dnf install rss2email```

```pacman: sudo pacman -S rss2email```

```zypper: sudo zypper install rss2email```

```nix: nix profile install nixpkgs#rss2email```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fetchmail](/man/fetchmail)(1), [procmail](/man/procmail)(1), [mutt](/man/mutt)(1)
