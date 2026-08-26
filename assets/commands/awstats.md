# TAGLINE

生成高级的 Web 服务器统计信息

# TLDR

**更新统计信息**针对某个虚拟主机

```awstats -config [virtualhostname] -update```

**生成 HTML 报告**针对某个虚拟主机

```awstats -config [virtualhostname] -output```

一条命令中同时**更新统计信息并生成报告**

```awstats -config [virtualhostname] -update -output```

**生成指定月份的报告**

```awstats -config [virtualhostname] -output -month [01] -year [2024]```

**显示帮助**和用法信息

```awstats -h```

# SYNOPSIS

**awstats** **-config** _virtualhostname_ [_OPTIONS_]

# PARAMETERS

**-config** _virtualhostname_
> 指定虚拟主机名以选择配置文件。

**-update**
> 从日志文件更新统计信息（默认动作）。

**-output**
> 生成主 HTML 报告。只有同时指定了 -update 时才会更新统计信息。

**-month** _MM_
> 指定报告输出的月份（01-12）。

**-year** _YYYY_
> 指定报告输出的年份。

**-h**
> 显示用法信息。

# DESCRIPTION

**AWStats**（Advanced Web Statistics）是一款强大的日志文件分析器，能以图形化网页的形式生成高级的 Web、流媒体、FTP 或邮件服务器统计信息。它处理日志文件，提供关于访客、页面、点击量、搜索引擎、关键词、机器人、失效链接等的详细信息。

AWStats 既可作为 CGI 脚本运行，也可从命令行运行。它使用部分信息文件来高效地增量处理大型日志文件。该工具支持主流服务器软件的日志格式，包括 Apache（NCSA combined/XLF/ELF 或 common/CLF 格式）、IIS（W3C 日志格式），以及各种代理、流媒体和邮件服务器。

配置文件按以下顺序查找：**awstats._virtualhostname_.conf**、**awstats.conf**，或完整路径。它们必须位于 /etc/awstats、/usr/local/etc/awstats 或 /etc 中。

# ENVIRONMENT

**AWSTATS_FORCE_CONFIG**
> 如果定义了此变量，AWStats 无论命令行如何都会使用该值作为配置。

# CONFIGURATION

**/etc/awstats/awstats.conf**
> 默认的全局配置文件。

**/etc/awstats/awstats.MODEL.conf**
> 各虚拟主机的配置文件，其中 MODEL 是通过 -config 指定的虚拟主机名。

**/usr/local/etc/awstats/awstats.conf**
> 某些系统上可选的全局配置位置。

# CAVEATS

AWStats 需要带有 Encode 模块的 Perl。运行前必须正确设置配置文件中的日志文件路径和站点信息。统计信息是累加式的，因此除非使用 AWStats 内置的已处理条目跟踪，否则多次处理同一批日志条目会产生错误的结果。

# HISTORY

AWStats 由 Laurent Destailleur 创建，首次发布于 **2000** 年。在 Google Analytics 等基于 JavaScript 的分析工具兴起之前，它曾是最流行的开源 Web 分析工具之一。该项目目前仍在 SourceForge 和 GitHub 上维护，提供无需 JavaScript 或客户端跟踪的服务端日志分析。

# INSTALL

```pacman: sudo pacman -S awstats```

```nix: nix profile install nixpkgs#awstats```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[goaccess](/man/goaccess)(1), [apache2](/man/apache2)(8)
