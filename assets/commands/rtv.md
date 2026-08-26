# TAGLINE

在终端中浏览 Reddit

# TLDR

**启动 Reddit Terminal Viewer**

```rtv```

**打开特定 subreddit**

```rtv -s [linux]```

**打开用户页面**

```rtv -s /u/[username]```

**按 URL 打开帖子**

```rtv [https://reddit.com/r/...]```

# SYNOPSIS

**rtv** [_options_] [_link_]

# PARAMETERS

**-s**, **--subreddit** _name_
> 打开 subreddit。

**-l**, **--link** _url_
> 打开帖子。

**--log** _file_
> 日志文件。

**--config** _file_
> 配置文件。

**--ascii**
> 仅 ASCII 模式。

**--theme** _name_
> 颜色主题。

# DESCRIPTION

**rtv**（Reddit Terminal Viewer）是 Reddit 的终端界面。它在文本界面中显示 subreddit、帖子和评论，并提供类 vim 的导航方式。

注意：该项目已停止维护；可以考虑使用 tuir 分支。

# EXAMPLES

```bash
# Launch default
rtv

# Specific subreddit
rtv -s programming

# Multireddit
rtv -s linux+python+vim

# User profile
rtv -s /u/spez

# Direct link
rtv https://reddit.com/r/linux/comments/...
```

# KEYBINDINGS

```
j/k     - Move down/up
l/h     - Open/back
o       - Open in browser
c       - Compose
/       - Search
r       - Refresh
q       - Quit
?       - Help
```

# CONFIGURATION

**~/.config/rtv/rtv.cfg**
> 主配置文件，控制默认 subreddit、按键绑定、浏览器、编辑器和显示偏好。

# CAVEATS

已停止维护——请改用 tuir。部分功能需要 Reddit 账户。需要 OAuth 登录。

# HISTORY

rtv 由 **Michael Lazar** 创建，是一个终端 Reddit 客户端。开发于 2019 年停止；**tuir** 是社区分支。

# SEE ALSO

[tuir](/man/tuir)(1), [w3m](/man/w3m)(1), [lynx](/man/lynx)(1)
