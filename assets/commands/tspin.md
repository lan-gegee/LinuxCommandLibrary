# TAGLINE

日志文件语法高亮查看器

# TLDR

**查看日志文件**

```tspin [logfile.log]```

**跟踪并高亮显示**

```tspin -f [logfile.log]```

**从标准输入读取**

```cat [log] | tspin```

**不使用分页器**

```tspin --no-pager [logfile.log]```

# SYNOPSIS

**tspin** [_-f_] [_--no-pager_] [_options_] [_file_]

# PARAMETERS

**-f**
> 跟随模式。

**--no-pager**
> 禁用分页器。

**--config** _FILE_
> 配置文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**tspin** 是一个日志文件查看器，会自动应用语法高亮，让日志更易读。它能识别常见的日志格式，为时间戳、日志级别、IP 地址、URL 和 JSON 结构等元素着色，无需手动配置。

跟随模式（**-f**）实时监控日志文件，在新条目出现时立即高亮，类似于带颜色的 **tail -f**。该工具还可以通过管道从标准输入读取，融入现有的日志处理管道。

内置分页器支持交互式滚动浏览日志文件。对于非标准日志格式，可以通过配置文件定义自定义高亮规则。

# CAVEATS

使用 Rust 实现。自定义格式需通过配置。需要终端颜色支持。

# HISTORY

**tspin** 作为一个日志文件高亮工具而创建，通过自动格式检测让日志更易读。

# INSTALL

```apt: sudo apt install tailspin```

```pacman: sudo pacman -S tailspin```

```brew: brew install tailspin```

```nix: nix profile install nixpkgs#tailspin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [lnav](/man/lnav)(1), [tail](/man/tail)(1)
