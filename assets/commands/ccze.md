# TAGLINE

强大的日志着色器

# TLDR

**为日志文件着色**

```cat [/var/log/syslog] | ccze```

**跟随日志并着色**

```tail -f [/var/log/syslog] | ccze```

**输出原始 ANSI 供 less 使用**

```cat [logfile] | ccze -A | less -R```

**HTML 输出**

```cat [logfile] | ccze -h > [output.html]```

**禁用查询以提速**

```cat [logfile] | ccze -A -o nolookups | less -R```

**列出可用的插件**

```ccze -l```

**只使用指定插件着色**

```cat [logfile] | ccze -p [httpd]```

**使用替代配置文件**

```cat [logfile] | ccze -F [~/.my_cczerc] -A```

# SYNOPSIS

**ccze** [_options_]

# DESCRIPTION

**ccze** 是一个用 C 编写的强大日志着色器，设计为 **colorize** 的即插即用替代品，性能更好、资源占用更低。它从标准输入读取日志数据，并使用 ncurses、原始 ANSI 转义码或 HTML 输出着色后的文本。

该工具采用插件架构来识别不同日志格式并为其着色，包括 syslog、Apache httpd、Postfix、Squid、Exim、fetchmail、procmail 和 vsftpd。每个插件理解其目标日志格式的结构，并为时间戳、主机名、严重级别等字段应用合适的颜色。

输出默认为 ncurses 模式，但 `-A` 标志会产生适合通过管道传给 `less -R` 或其他工具的原始 ANSI 输出。

# PARAMETERS

**-a** _PLUGIN=ARGUMENTS_, **--argument** _PLUGIN=ARGUMENTS_
> 向指定的插件传递以空格分隔的参数。

**-A**, **--raw-ansi**
> 生成原始 ANSI 颜色序列而不使用 ncurses。

**-c** _KEY=COLOR_, **--color** _KEY=COLOR_
> 设置某个关键字的颜色，与配置文件中的写法相同。

**-C**, **--convert-date**
> 将 UNIX 时间戳转换为人类可读的日期格式（例如在 squid 或 oops 日志中）。

**-F** _rcfile_, **--rcfile** _rcfile_
> 读取指定文件作为配置，而不是默认配置。

**-h**, **--html**
> 生成 HTML 输出而不是控制台颜色。

**-l**, **--list-plugins**
> 列出所有可用（已加载）的插件及其类型和描述。

**-m** _mode_, **--mode** _mode_
> 设置输出模式：_curses_、_ansi_ 或 _html_。

**-o** _option_, **--options** _option_
> 切换某项功能。可用选项：**scroll**、**wordcolor**、**lookups**、**transparent**、**cssfile**。加 "no" 前缀表示禁用（例如 **nolookups**）。除 cssfile 外默认全部启用。

**-p** _plugin_, **--plugin** _plugin_
> 只加载指定的插件，以略微提升速度。

**-r**, **--remove-facility**
> 从日志行中移除 syslog-ng 的 facility 级别信息。

**-V**, **--version**
> 显示版本信息。

**--help**
> 显示用法摘要并退出。

# CONFIGURATION

**/etc/cczerc**
> 系统级配置。

**~/.cczerc**
> 每用户配置。

# PLUGINS

位于 /usr/lib/ccze 和 ~/.ccze。支持：
- syslog、httpd、postfix
- squid、exim、fetchmail
- procmail、vsftpd、xferlog
- ulogd、apm

# CAVEATS

处理长日志时使用 **-o nolookups** 可加快处理速度。启用 lookups（默认开启）时会解析用户名和服务名，但会显著拖慢着色速度。

# INSTALL

```apt: sudo apt install ccze```

```dnf: sudo dnf install ccze```

```zypper: sudo zypper install ccze```

```nix: nix profile install nixpkgs#ccze```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tail](/man/tail)(1), [less](/man/less)(1), [multitail](/man/multitail)(1), [journalctl](/man/journalctl)(1)
