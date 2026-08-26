# TAGLINE

利用 Linux 的 inotify API 高效监视文件和目录的变化

# TLDR

**监视**特定文件的事件，首个事件发生后退出

```inotifywait [path/to/file]```

**持续监视**文件的事件

```inotifywait -m [path/to/file]```

**递归**监视目录的事件

```inotifywait -m -r [path/to/directory]```

监视目录但**排除**匹配正则表达式的文件

```inotifywait -m -r --exclude "[regex]" [path/to/directory]```

以 30 秒为**超时**进行监视

```inotifywait -m -t 30 [path/to/file]```

只监视**特定事件**（modify）

```inotifywait -e modify [path/to/file]```

**安静地**监视（无状态消息）

```inotifywait -q [path/to/file]```

文件被访问时运行一条**命令**

```inotifywait -e access [path/to/file] && [command]```

# SYNOPSIS

**inotifywait** [_options_] _file_...

# PARAMETERS

**-m**, **--monitor**
> 持续运行，第一个事件发生后不退出

**-r**, **--recursive**
> 递归监视目录

**-e**, **--event** _EVENT_
> 只监视特定事件（access、modify、create、delete 等）

**-t**, **--timeout** _SECONDS_
> 超时且无事件时退出

**-q**, **--quiet**
> 抑制信息性消息

**--exclude** _PATTERN_
> 排除匹配正则表达式模式的文件

**--format** _FMT_
> 自定义输出格式

**-c**, **--csv**
> 以 CSV 格式输出

# DESCRIPTION

**inotifywait** 利用 Linux 的 inotify API 高效监视文件和目录的变化。它会阻塞直到发生文件系统事件，非常适合在文件变化时触发操作。

可用事件包括：
- **access** - 文件被读取
- **modify** - 文件被写入
- **create** - 文件/目录被创建
- **delete** - 文件/目录被删除
- **move** - 文件被移动
- **attrib** - 元数据发生变化
- **close_write** - 写入后文件关闭

它常用于脚本中：源文件变化时重新构建项目、同步文件或触发部署。

# CAVEATS

仅限 Linux（使用 inotify 内核子系统）。监视数量有上限（可通过 /proc/sys/fs/inotify/max_user_watches 配置）。递归监视会为每个目录创建一个 watch。不适合非常大的目录树。

# HISTORY

inotifywait 是 inotify-tools 的一部分，旨在为 Linux 的 inotify API 提供用户空间访问方式。该 API 于内核 2.6.13（**2005 年**）引入，取代了较旧的 dnotify 机制。

# INSTALL

```apt: sudo apt install inotify-tools```

```dnf: sudo dnf install inotify-tools```

```pacman: sudo pacman -S inotify-tools```

```apk: sudo apk add inotify-tools```

```zypper: sudo zypper install inotify-tools```

```brew: brew install inotify-tools```

```nix: nix profile install nixpkgs#inotify-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[entr](/man/entr)(1), [fswatch](/man/fswatch)(1), [fatrace](/man/fatrace)(1)
