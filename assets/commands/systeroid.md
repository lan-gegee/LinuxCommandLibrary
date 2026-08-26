# TAGLINE

带 TUI 的强大 sysctl 替代品

# TLDR

**列出所有内核参数**

```systeroid -A```

以树形格式**显示参数**

```systeroid -T```

**设置内核参数**

```systeroid [kernel.hostname]=[myhost]```

搜索匹配模式的参数

```systeroid -r [net.ipv4]```

连同文档一起**显示参数值**

```systeroid -E [kernel.hostname]```

以 JSON 格式输出参数

```systeroid -A --output json```

**启动 TUI**

```systeroid-tui```

# SYNOPSIS

**systeroid** [_options_] [_variable_[**=**_value_] ...]

# DESCRIPTION

**systeroid** 是 **sysctl** 的一个更强大的替代品，用于通过 procfs 在运行时管理内核参数。它同时提供 CLI 和 TUI 界面，支持树形显示、JSON 输出、正则表达式模式匹配，还能获取参数的官方 Linux 内核文档。

# OPTIONS

**-A**, **--all**
> 列出所有内核参数。

**-T**, **--tree**
> 以树形层次结构显示参数。

**-r**, **--pattern** _REGEX_
> 过滤匹配正则表达式的参数。

**-E**, **--explain**
> 显示某个参数的内核文档。

**--output** _FORMAT_
> 输出格式（default 或 json）。

**-p**, **--load** _FILE_
> 从配置文件加载参数值。

**-q**, **--quiet**
> 抑制正常输出。

**-N**, **--names**
> 只打印参数名，不打印值。

# HISTORY

**systeroid** 由 **Orhun Poyraz**（orhun）创建，采用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S systeroid```

```apk: sudo apk add systeroid```

```nix: nix profile install nixpkgs#systeroid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sysctl](/man/sysctl)(1), [proc](/man/proc)(5), [tuned](/man/tuned)(1)
