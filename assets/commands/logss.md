# TAGLINE

用于日志流拆分与可视化的 CLI 工具

# TLDR

**按多个正则表达式模式拆分日志**

```tail -f [logfile] | logss -c "[pattern1]" -c "[pattern2]"```

**将匹配的模式写入文件**

```tail -f [logfile] | logss -c "[pattern]" -o [output_dir/]```

**从命令而非 stdin 获取输入**

```logss -C "[command]" -c "[pattern]"```

**使用配置文件**

```logss -f [config.yaml]```

**以垂直视图模式启动**

```tail -f [logfile] | logss -c "[pattern]" -V```

# SYNOPSIS

**logss** [_options_]

# PARAMETERS

**-c** _PATTERN_
> 指定用于匹配和拆分日志的正则表达式模式。可以是 `pattern`，也可以是 `pattern,command,timeout`，以便在每次匹配时触发 shell 命令。

**-C** _COMMAND_
> 从 shell 命令获取输入而不是 stdin。

**-f** _FILE_
> 从 YAML 文件加载配置（覆盖命令行参数）。

**-o** _OUTPUT_PATH_
> 将匹配的行写入指定输出路径下的文件。

**-r** _MS_
> 定义渲染速度（毫秒）。默认：100。

**-s**
> 以单视图模式启动。

**-t** _N_
> 每个容器的触发器线程数。默认：1。

**-V**
> 以垂直视图模式启动。

**-e**
> 输入为空时退出。

**-h**
> 打印帮助。

# DESCRIPTION

**logss** 是一款实时可视化与拆分日志流的 CLI/TUI 工具。它可以定义多个正则表达式模式，并在各自独立的窗格中查看匹配的日志条目，同时自动进行颜色编码，渲染速度可调。

该工具从 stdin 读取输入（或通过 `-C` 从命令读取），并根据模式匹配将日志行分发到不同的视图。每个模式容器可以选择在匹配发生时触发一个 shell 命令，用 `__line__` 作为匹配行的占位符。另有一个专门的容器显示未经筛选的原始流。

交互控制包括暂停/恢复、滚动、缩放、显示/隐藏容器以及切换自动换行。

# CAVEATS

默认从 stdin 读取；必须通过管道传入日志源或使用 `-C` 指定。用 `-f` 指定的配置文件会覆盖所有命令行参数。

# HISTORY

**logss** 由 **todoesverso** 创建，采用 **Rust** 编写。

# INSTALL

```aur: yay -S logss```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [tail](/man/tail)(1), [multitail](/man/multitail)(1)
