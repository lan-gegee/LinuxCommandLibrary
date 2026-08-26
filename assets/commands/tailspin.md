# TAGLINE

零配置的日志文件高亮工具

# TLDR

带高亮地**查看日志文件**

```tspin [application.log]```

像 tail -f 一样**跟踪日志文件**

```tspin -f [/var/log/syslog]```

将实时日志通过管道传给 tailspin

```kubectl logs -f [pod_name] | tspin```

# SYNOPSIS

**tspin** [_options_] [_file_]

# DESCRIPTION

**tailspin** 会自动识别日期、IP 地址、UUID、URL、严重级别关键词、数字等模式，从而高亮显示日志文件。它无需任何设置，对任意日志格式都能一致工作。默认使用 **less** 作为分页器。

# HISTORY

**tailspin** 由 **Ben Sadeh**（bensadeh）创建，采用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S tailspin```

```brew: brew install tailspin```

```nix: nix profile install nixpkgs#tailspin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lnav](/man/lnav)(1), [ccze](/man/ccze)(1), [multitail](/man/multitail)(1)
