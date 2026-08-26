# TAGLINE

在单个终端窗口中查看多个日志文件

# TLDR

**跟踪多个文件**

```multitail [file1.log] [file2.log]```

**水平分屏**

```multitail -s 2 [file1.log] [file2.log]```

**在同一个窗口合并文件**

```multitail -I [file1.log] -I [file2.log]```

**使用配色方案跟踪**

```multitail -cS [apache] [access.log]```

**执行并跟踪命令输出**

```multitail -l "[command]"```

**带时间戳跟踪**

```multitail -ts [file.log]```

# SYNOPSIS

**multitail** [_options_] [_files_...]

# DESCRIPTION

**multitail** 允许在单个终端窗口中查看多个日志文件。它可以分割屏幕显示不同文件，或以颜色编码合并它们。

该工具提供过滤、搜索和高亮功能，便于高效监控日志。

# PARAMETERS

**-s** _n_
> 分割为 n 列。

**-I** _file_
> 将文件并入前一个窗口。

**-l** _cmd_
> 执行命令并跟踪其输出。

**-L** _cmd_
> 与 -l 相同，但命令退出后会重新启动。

**-cS** _scheme_
> 配色方案。

**-ts**
> 添加时间戳。

**-f**
> 跟踪模式。

**-i** _file_
> 在新窗口中添加文件。

**-n** _lines_
> 每个窗口的行数。

**-m** _lines_
> 回滚缓冲区大小。

# CAVEATS

复杂布局需要练习才能掌握。配色方案需要配置。文件过多可能使显示杂乱。资源占用随文件数量增长。

# HISTORY

**multitail** 由 **Folkert van Heusden** 创建，将 tail 的功能扩展到多文件场景。它满足了同时监控多个日志文件的常见需求。

# INSTALL

```apt: sudo apt install multitail```

```dnf: sudo dnf install multitail```

```apk: sudo apk add multitail```

```zypper: sudo zypper install multitail```

```brew: brew install multitail```

```nix: nix profile install nixpkgs#multitail```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tail](/man/tail)(1), [less](/man/less)(1), [lnav](/man/lnav)(1), [watch](/man/watch)(1)
