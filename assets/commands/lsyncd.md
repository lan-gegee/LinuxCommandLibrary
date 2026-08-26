# TAGLINE

监视目录变化并实时同步

# TLDR

**本地同步目录**

```lsyncd -rsync [/source/] [/destination/]```

**同步到远程服务器**

```lsyncd -rsyncssh [/local/] [user@host] [/remote/]```

**使用配置文件**

```lsyncd [config.lua]```

**以前台模式运行并记录日志**

```lsyncd -log all [config.lua]```

**试运行**（显示将同步的内容）

```lsyncd -nodaemon -log all [config.lua]```

**指定日志文件**

```lsyncd -logfile [/var/log/lsyncd.log] [config.lua]```

# SYNOPSIS

**lsyncd** [_-rsync source dest_] [_-rsyncssh source host dest_] [_-log level_] [_options_] [_config.lua_]

# PARAMETERS

**-rsync** _SOURCE_ _DEST_
> 简单的 rsync 同步模式。

**-rsyncssh** _SOURCE_ _HOST_ _DEST_
> 通过 SSH 向远程主机进行 rsync。

**-nodaemon**
> 以前台运行，不守护进程化。

**-log** _LEVEL_
> 设置日志级别（all、scarce、normal、error）。

**-logfile** _FILE_
> 将日志写入文件。

**-pidfile** _FILE_
> 写入 PID 文件。

**-delay** _SECONDS_
> 同步前的延迟（聚合窗口）。

**-insist**
> 启动出错时持续重试。

**-version**
> 显示版本号。

**-help**
> 显示帮助。

# DESCRIPTION

**lsyncd**（Live Syncing Daemon）监视目录变化并实时同步。它在 Linux 上使用 inotify 高效检测文件变化。

当变化发生时，lsyncd 会短暂等待（延迟），聚合多个变化，然后触发 rsync 进行同步。这种方式能高效处理突发写入，同时保持近乎实时的同步。

配置文件使用 Lua 脚本以获得灵活性。它们定义同步对、排除模式和 rsync 选项，还可以实现自定义同步逻辑。

该工具既适用于本地目录，也可通过 SSH 与远程服务器配合工作。多个同步对可以从单一配置同时运行。

常见用途包括备份系统、集群文件同步，以及在开发环境中让文件在多台机器间保持同步。

# CAVEATS

大型目录的初始同步可能耗时。对于庞大的目录树，可能需要调高 inotify watch 上限。高频变化可能导致延迟。符号链接和特殊文件需要谨慎处理。

# HISTORY

**lsyncd** 由 **Axel Kittenberger** 于 **2008 年**左右创建。它将 inotify 高效的变更通知与 rsync 可靠的文件同步相结合。该项目在版本 2 中引入 Lua 配置，支持了更复杂的同步场景。

# INSTALL

```apt: sudo apt install lsyncd```

```dnf: sudo dnf install lsyncd```

```apk: sudo apk add lsyncd```

```zypper: sudo zypper install lsyncd```

```brew: brew install lsyncd```

```nix: nix profile install nixpkgs#lsyncd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [inotifywait](/man/inotifywait)(1), [unison](/man/unison)(1), [syncthing](/man/syncthing)(1)
