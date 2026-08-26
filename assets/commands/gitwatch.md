# TAGLINE

文件被修改时自动提交更改

# TLDR

**监视目录并自动提交**

```gitwatch [path]```

使用自定义信息进行监视

```gitwatch -m "[Auto commit]" [path]```

监视并推送

```gitwatch -r [remote] -b [branch] [path]```

监视特定分支

```gitwatch -b [branch] [path]```

# SYNOPSIS

**gitwatch** [_options_] _path_

# PARAMETERS

**-s** _seconds_
> 检测到更改后提交前的延迟时间（默认：2 秒）。

**-d** _format_
> 默认提交信息中使用的时间戳格式字符串（参见 `man date`）。

**-r** _remote_
> 每次提交后推送到的远程仓库（默认：不推送）。

**-R**
> 推送前先运行 `git pull --rebase`。

**-b** _branch_
> 要推送提交到的分支。

**-g** _path_
> `.git` 目录的位置（默认自动检测）。

**-m** _message_
> 提交信息模板；`%d` 会被替换为时间戳。

**-c** _command_
> 以该命令的输出作为提交信息，取代 `-m`。

**-C**
> 将已更改文件的列表通过 stdin 管道传给 `-c` 命令。

**-l** _lines_, **-L** _lines_
> 在提交信息中包含已更改的行，带颜色（`-l`）或不带颜色（`-L`）；`0` 表示包含所有行。

**-e** _events_
> 用于监视更改的 inotifywait 事件。

**-x** _pattern_
> 排除匹配模式的路径，不进行监视。

**-f**
> 启动时立即提交所有待处理的更改。

**-M**
> 在 git 合并进行期间跳过自动提交。

**-v**
> 详细/调试输出。

**-h**
> 显示帮助信息。

# DESCRIPTION

**gitwatch** 监视一个目录，每当文件被修改时自动提交更改。它使用 inotifywait（Linux 上，通过 inotify-tools）或 fswatch（macOS/BSD 上）实时检测文件变化，然后在提交前等待一小段延迟，以便将快速连续的编辑合并为单次提交。

该工具适用于对笔记、配置文件或任何希望完整追踪每个变更而无需手动提交的目录进行自动版本控制，并且可以选择将每次提交推送到远程仓库。

# CAVEATS

需要在 Linux 上安装 **inotify-tools** 或在 macOS/BSD 上安装 **fswatch**。只跟踪 gitwatch 运行期间自身观察到的变化；不会补录其停止运行期间发生的变化。

# INSTALL

```brew: brew install gitwatch```

```nix: nix profile install nixpkgs#gitwatch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inotifywait](/man/inotifywait)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/gitwatch/gitwatch)```

<!-- verified: 2026-07-17 -->
