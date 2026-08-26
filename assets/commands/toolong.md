# TAGLINE

查看、追踪、合并和搜索日志文件

# TLDR

**打开并查看日志文件**

```tl [access.log]```

**按时间戳合并并查看多个日志**

```tl [server.log] [app.log] --merge```

**将实时输出管道传入 toolong**

```tail -f [/var/log/syslog] | tl```

**追踪日志文件**（从末尾开始）

```tl --tail [access.log]```

# SYNOPSIS

**tl** [_options_] [_files_...]

# PARAMETERS

**--merge**
> 按时间戳合并多个日志文件。

**--tail**
> 从文件末尾开始。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**toolong** 是一个用于查看和分析日志文件（包括 JSONL）的终端应用。它可以即时打开数 GB 大小的文件、实时追踪日志、自动检测时间戳以合并多个文件、处理压缩的 .bz/.bz2 文件，并对常见日志格式进行语法高亮。

# HISTORY

**toolong** 由 **Will McGugan**（Textualize）创建，使用 Textual 框架以 **Python** 编写。

# INSTALL

```nix: nix profile install nixpkgs#toolong```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lnav](/man/lnav)(1), [less](/man/less)(1), [multitail](/man/multitail)(1)
