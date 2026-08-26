# TAGLINE

跨平台文件变化监控器

# TLDR

**监视目录**的变化

```fswatch [/path/to/directory]```

**监视并在变化时执行命令**

```fswatch -o [/path/to/directory] | xargs -n1 -I{} [command]```

以递归方式**监视**

```fswatch -r [/path/to/directory]```

**监视特定文件类型**

```fswatch --include ".*\\.txt$" --exclude ".*" [/path/to/directory]```

每次变化只产生一个事件地**监视**

```fswatch -1 [/path/to/directory]```

**监视多个路径**

```fswatch [/path/dir1] [/path/dir2]```

带时间戳的**详细输出**

```fswatch -t [/path/to/directory]```

带延迟（防抖）地**监视**

```fswatch -l [2] [/path/to/directory]```

# SYNOPSIS

**fswatch** [_options_] _paths_...

# DESCRIPTION

**fswatch** 是一个跨平台的文件变化监控器，检测文件系统变化并输出受影响的路径。它使用各平台的原生 API（Linux 上的 inotify、macOS 上的 FSEvents、BSD 上的 kqueue）实现高效监控。

该工具将发生变化的文件路径输出到 stdout，可以通过管道传给其他命令，构建重建项目、运行测试或重载服务等自动化工作流。它支持递归监控和按文件模式过滤。

fswatch 适用于开发工作流、构建自动化、备份触发以及任何需要由文件修改触发操作的场景。

# PARAMETERS

**-o**, **--one-per-batch**
> 每批只输出一个事件（便于计数）。

**-r**, **--recursive**
> 递归进入子目录。

**-t**, **--timestamp**
> 为事件附带时间戳。

**-l** _seconds_, **--latency=** _seconds_
> 设置延迟（防抖周期）。

**-1**, **--one-event**
> 第一个事件发生后退出。

**-0**, **--print0**
> 用 NUL 字符分隔路径。

**--event** _type_
> 按事件类型过滤。

**--include** _regex_
> 只包括匹配的文件。

**--exclude** _regex_
> 排除匹配的文件。

**-m** _monitor_, **--monitor=** _monitor_
> 使用指定的监控后端。

**-v**, **--verbose**
> 详细输出。

**-n**, **--numeric**
> 输出数字形式的事件代码。

# CAVEATS

系统对 inotify watch 数量的限制可能影响大目录的监控（可通过 /proc/sys/fs/inotify/max_user_watches 调整）。不同后端的能力不同。延迟设置影响响应速度与批量处理的权衡。

# HISTORY

**fswatch** 由 **Enrico M. Crisostomo** 于 **2014** 年创建，旨在提供统一的跨平台文件监控方案。它被设计为使用原生 API 的单一工具来取代平台专用工具。该项目仍在持续维护，支持 Linux、macOS、Windows 和 BSD 系统。

# INSTALL

```apt: sudo apt install fswatch```

```dnf: sudo dnf install fswatch```

```zypper: sudo zypper install fswatch```

```brew: brew install fswatch```

```nix: nix profile install nixpkgs#fswatch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inotifywait](/man/inotifywait)(1), [entr](/man/entr)(1), [watchexec](/man/watchexec)(1), [watchman](/man/watchman)(1)

# RESOURCES

```[Source code](https://github.com/emcrisostomo/fswatch)```

<!-- verified: 2026-07-15 -->
