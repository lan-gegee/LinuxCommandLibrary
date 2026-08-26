# TAGLINE

从 Newsbeuter 分叉而来的终端 RSS/Atom 阅读器

# TLDR

**启动 newsboat**

```newsboat```

**导入 OPML 订阅列表**

```newsboat -i [feeds.opml]```

**将订阅导出为 OPML**

```newsboat -e > [feeds.opml]```

**使用替代的配置文件**

```newsboat -C [/path/to/config]```

**使用替代的 URL 文件**

```newsboat -u [/path/to/urls]```

**刷新订阅后退出**

```newsboat -x reload```

**指定缓存文件**

```newsboat -c [/path/to/cache.db]```

# SYNOPSIS

**newsboat** [_-C config_] [_-u urls_] [_-c cache_] [_-i opml_] [_-e_] [_options_]

# PARAMETERS

**-C**, **--config-file** _file_
> 替代的配置文件。

**-u**, **--url-file** _file_
> 替代的 URL 文件。

**-c**, **--cache-file** _file_
> 替代的缓存数据库。

**-i**, **--import-from-opml** _file_
> 从 OPML 导入订阅。

**-e**, **--export-to-opml**
> 将订阅以 OPML 格式导出到 stdout。

**-r**, **--refresh-on-start**
> 启动时刷新订阅。

**-x** _command_, **--execute** _command_
> 执行命令（reload、print-unread）。

**-l** _level_, **--log-level** _level_
> 日志级别（1-6）。

**-q**, **--quiet**
> 静默启动。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# KEYBOARD SHORTCUTS

**r**
> 重新加载当前订阅。

**R**
> 重新加载所有订阅。

**Enter**
> 打开选中的条目。

**o**
> 在浏览器中打开。

**n / p**
> 下一条 / 上一条未读。

**j / k**
> 向下 / 向上移动。

**q**
> 退出 / 返回。

**A**
> 全部标记为已读。

**s**
> 保存文章。

**/**
> 搜索。

**?**
> 显示帮助。

# DESCRIPTION

**Newsboat** 是一款终端 RSS/Atom 订阅阅读器，从 Newsbeuter 分叉而来。它通过可自定义的文本界面展示订阅内容，并采用类 vim 的按键绑定。

订阅在 **~/.newsboat/urls** 中配置，每行一个 URL。可以在 URL 后添加标签以便分类。查询订阅（query feed）允许按未读状态或文章年龄等条件跨多个订阅进行过滤。

配置文件（~/.newsboat/config）控制外观和行为：颜色、按键绑定、浏览器命令、刷新设置以及宏。可定制程度非常高。

文章缓存在本地 SQLite 中，支持离线阅读。自动清理功能会删除旧文章。缓存可以在多台机器之间共享。

与外部工具的集成包括：在浏览器中打开链接、保存文章、将内容管道传给脚本，以及对文章执行 shell 命令。播客支持可以下载附件。

过滤器表达式可按日期、作者、标题或内容筛选文章。书签功能可将文章发送到外部服务或脚本。

# CAVEATS

纯文本界面可能无法很好地渲染所有 HTML 内容。不显示图片（需要外部查看器）。订阅解析质量取决于源的质量。订阅数量过多会拖慢刷新速度。不支持某些动态网页内容。

# HISTORY

**Newsboat** 于 **2017 年**从被放弃的 **Newsbeuter** 分叉而来。Newsbeuter（德语意为"新闻海盗"）由 **Andreas Krennmair** 于 **2007 年**前后创建。该分支保持了活跃开发，在保留极简主义、键盘驱动理念的同时不断新增功能。如今它已成为 Linux 用户事实上的终端订阅阅读器。

# INSTALL

```apt: sudo apt install newsboat```

```dnf: sudo dnf install newsboat```

```pacman: sudo pacman -S newsboat```

```apk: sudo apk add newsboat```

```zypper: sudo zypper install newsboat```

```brew: brew install newsboat```

```nix: nix profile install nixpkgs#newsboat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rss2email](/man/rss2email)(1), [elfeed](/man/elfeed)(1), [snownews](/man/snownews)(1), [rsstail](/man/rsstail)(1)
