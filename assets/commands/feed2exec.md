# TAGLINE

RSS/Atom 源自动化工具

# TLDR

**抓取所有已配置的源**

```feed2exec fetch```

**添加新源**

```feed2exec add [feedname] [https://example.com/feed.xml]```

**列出已配置的源**

```feed2exec ls```

**移除一个源**

```feed2exec rm [feedname]```

**使用自定义配置运行**

```feed2exec --config [~/.config/feed2exec.ini] fetch```

# SYNOPSIS

**feed2exec** [_options_] _command_ [_args_]

# PARAMETERS

**fetch**
> 抓取并处理所有源。

**add** _name_ _url_
> 添加新源。

**rm** _name_
> 移除源。

**ls**
> 列出已配置的源。

**parse** _url_
> 只解析源而不处理。

**--config** _file_
> 配置文件路径。

**--verbose**, **-v**
> 详细输出。

**--debug**
> 调试输出。

# CONFIGURATION

**~/.config/feed2exec.ini**
> 主配置文件，定义源、输出格式和处理命令。

# DESCRIPTION

**feed2exec** 抓取 RSS/Atom 源，并对每个新条目执行命令。它是一个灵活的源处理器，可以根据源更新发送邮件、运行脚本、保存文件或触发任意命令。

与订阅阅读器不同，feed2exec 面向自动化设计。常见用途包括邮件通知、归档，以及在源更新时触发 webhook。

# CAVEATS

每个源都需要单独配置。状态记录在 SQLite 数据库中。发送邮件需要配置好的 MTA。复杂的输出可能需要自定义插件。

# HISTORY

feed2exec 由 **Antoine Beaupré** 编写，作为 rss2email 及类似工具的灵活替代品。它强调 Unix 哲学：通过执行外部命令而非在内部实现所有功能来完成工作。

# SEE ALSO

[rss2email](/man/rss2email)(1), [newsboat](/man/newsboat)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://gitlab.com/anarcat/feed2exec)```

```[Documentation](https://feed2exec.readthedocs.io/)```

<!-- verified: 2026-07-15 -->
