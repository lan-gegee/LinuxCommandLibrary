# TAGLINE

列出可用的内核跟踪事件

# TLDR

列出可用的**跟踪器**

```sudo trace-cmd list -t```

列出可用的**插件**

```sudo trace-cmd list -p```

列出可用的**事件**

```sudo trace-cmd list -e```

列出可用的**函数**

```sudo trace-cmd list -f```

列出匹配**模式**的事件

```sudo trace-cmd list -e [sched:*]```

列出可用的**事件选项**

```sudo trace-cmd list -o```

列出匹配**正则表达式**的函数

```sudo trace-cmd list -f [tcp_send*]```

# SYNOPSIS

**trace-cmd list** [_OPTIONS_]

# PARAMETERS

**-t**
> 列出可用的跟踪器

**-p**
> 列出可用的插件

**-e** [_regex_]
> 列出可用事件，可按子系统或正则表达式模式过滤。

**-f** [_regex_]
> 列出可用于跟踪的函数，可按正则表达式过滤。

**-o**
> 列出可用的事件选项（如 noprint-fmt、sym-offset）。

**-B** _buffer_
> 从指定的缓冲区实例列出。

# DESCRIPTION

**trace-cmd list** 显示可与 Ftrace 跟踪框架配合使用的跟踪器、事件、插件和函数。这有助于了解当前系统上可以跟踪哪些内容。

输出取决于内核配置和已加载的模块。在内核符号较多的系统上，函数列表可能非常庞大。

# CAVEATS

需要 root 权限。可用条目取决于内核构建配置。函数列表可能极其庞大。

# INSTALL

```apt: sudo apt install trace-cmd```

```dnf: sudo dnf install trace-cmd```

```pacman: sudo pacman -S trace-cmd```

```zypper: sudo zypper install trace-cmd```

```nix: nix profile install nixpkgs#trace-cmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trace-cmd](/man/trace-cmd)(1), [trace-cmd-record](/man/trace-cmd-record)(1), [trace-cmd-report](/man/trace-cmd-report)(1), [perf](/man/perf)(1)
