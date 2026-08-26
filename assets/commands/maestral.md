# TAGLINE

面向 Linux 和 macOS 的轻量级 Dropbox 客户端

# TLDR

**关联 Dropbox 账户**

```maestral link```

**开始同步**

```maestral start```

**停止同步**

```maestral stop```

**显示同步状态**

```maestral status```

**暂停同步**

```maestral pause```

**恢复同步**

```maestral resume```

**列出同步活动**

```maestral activity```

**排除文件夹**不参与同步

```maestral excluded add [/path/to/folder]```

# SYNOPSIS

**maestral** [_start_] [_stop_] [_status_] [_link_] [_excluded_] [_options_] [_command_]

# PARAMETERS

**start**
> 启动同步守护进程。

**stop**
> 停止同步守护进程。

**restart**
> 重启同步守护进程。

**status**
> 显示当前同步状态。

**pause**
> 暂停同步。

**resume**
> 恢复同步。

**link**
> 关联 Dropbox 账户。

**unlink**
> 解除 Dropbox 账户的关联。

**activity**
> 显示最近的同步活动。

**excluded add** _PATH_
> 将文件夹排除出同步范围。

**excluded remove** _PATH_
> 将先前排除的文件夹重新纳入同步。

**excluded list**
> 列出被排除的文件夹。

**ls** _PATH_
> 列出文件夹内容。

**notify** _LEVEL_
> 设置通知级别。

**autostart**
> 配置自动启动。

**config**
> 显示配置。

**-c, --config-name** _NAME_
> 用于管理多个 Dropbox 账户的配置名称。

# DESCRIPTION

**maestral** 是一款面向 Linux 和 macOS 的轻量级 Dropbox 客户端。它提供文件同步功能，而没有官方客户端那样的高资源占用。

守护进程在后台运行，监控本地更改并与 Dropbox 同步。选择性同步可以排除不需要的文件夹以节省磁盘空间。

与官方客户端不同，Maestral 是开源的，占用更少的系统资源。它支持核心的同步功能，但不包含相机上传或截图等附加功能。

可以使用不同的配置名称配置多个 Dropbox 账户。每个账户作为独立的守护进程运行，拥有各自的同步文件夹。

status 命令显示同步进度、冲突和错误。activity 显示最近的文件更改。通知会在同步事件发生时提醒用户。

# CAVEATS

默认没有 GUI——仅提供 CLI（可选装 GUI）。不支持部分 Dropbox 功能。需要 Python。大型账户的初次同步耗时较长。

# HISTORY

**Maestral** 由 **Sam Schott** 于 **2018 年**前后创建，作为 Linux 上官方 Dropbox 客户端的轻量替代品。名字来源于密史脱拉风（Mistral）。它在希望获得 Dropbox 同步又不想依赖 Electron 或繁重依赖的 Linux 用户中广受欢迎。

# INSTALL

```nix: nix profile install nixpkgs#maestral```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rclone](/man/rclone)(1), [syncthing](/man/syncthing)(1)
