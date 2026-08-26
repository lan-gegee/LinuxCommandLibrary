# TAGLINE

使用 Linux 的 inotify 接口等待文件系统事件

# TLDR

**监视文件的变更**

```inotifywait [file]```

**递归监视目录**

```inotifywait -r [directory]```

**只等待特定事件**

```inotifywait -e [modify,create,delete] [path]```

**持续监视**

```inotifywait -m [path]```

**以 CSV 格式输出**

```inotifywait -m --csv [path]```

**带超时地监视**

```inotifywait -t [30] [path]```

# SYNOPSIS

**inotifywait** [_options_] _path_...

# PARAMETERS

**-m**, **--monitor**
> 持续监视（第一个事件发生后不退出）。

**-r**, **--recursive**
> 递归监视目录。

**-e** _EVENT_
> 要监视的事件（access、modify、create、delete、move）。

**-t** _SECONDS_
> 超时时间（秒）。

**--csv**
> 以 CSV 格式输出。

**--format** _FMT_
> 自定义输出格式。

**-q**, **--quiet**
> 抑制非必要输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**inotifywait** 使用 Linux 的 inotify 接口等待文件系统事件。当被监视路径上发生指定事件时即退出。

该工具让脚本能以事件驱动的方式响应文件变化，支持监视文件、目录以及递归监视。

# CAVEATS

仅限 Linux（inotify）。可能需要调整监视数量上限。不适用于 NFS/远程文件系统。

# HISTORY

inotifywait 是 **inotify-tools** 的一部分，旨在为 Linux 的 inotify 文件监视 API 提供命令行访问方式。

# SEE ALSO

[fswatch](/man/fswatch)(1), [entr](/man/entr)(1), [watch](/man/watch)(1)
