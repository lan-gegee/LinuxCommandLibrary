# TAGLINE

Deluge BitTorrent 客户端的文本控制台界面

# TLDR

**启动交互式**控制台

```deluge-console```

**连接守护进程**并列出种子

```deluge-console "connect; info"```

**添加种子**文件或磁力链接

```deluge-console "add [file.torrent]"```

**暂停一个种子**

```deluge-console "pause [torrent_id]"```

**恢复一个种子**

```deluge-console "resume [torrent_id]"```

**移除一个种子**

```deluge-console "rm [torrent_id]"```

**显示种子详情**

```deluge-console "info -v [torrent_id]"```

用分号分隔**运行多条命令**

```deluge-console "connect [host:port]; add [file.torrent]; info"```

# SYNOPSIS

**deluge-console** [_options_] [_command_]

# PARAMETERS

_COMMAND_
> 要执行的控制台命令。省略时进入交互式 curses 模式。多条命令可用分号分隔。

**connect** [_HOST_:_PORT_]
> 连接到 Deluge 守护进程。

**info** [**-v**]
> 显示种子信息。使用 **-v** 查看详细内容。

**add** _TORRENT_
> 添加种子文件或磁力链接。

**pause** _ID_
> 暂停一个种子。

**resume** _ID_
> 恢复已暂停的种子。

**rm** _ID_
> 移除一个种子。

**del** _ID_
> 删除一个种子（rm 的别名）。

**move** _ID_ _PATH_
> 移动种子的下载位置。

**recheck** _ID_
> 强制重新校验种子数据。

**reannounce** _ID_
> 强制向 tracker 重新通告。

**config**
> 显示或设置守护进程配置。

**status**
> 显示会话状态和传输速率。

**halt**
> 关闭已连接的守护进程。

**--help**
> 显示帮助信息。

# DESCRIPTION

**deluge-console** 是 Deluge BitTorrent 客户端的文本控制台界面。Deluge 采用客户端/服务器模型，**deluged** 作为守护进程运行，**deluge-console** 则是终端前端。

在交互模式下，它呈现一个基于 curses 的可导航界面，通过键盘快捷键管理种子。在命令模式下，它接受以参数形式传入的命令，实现非交互操作，适合脚本和自动化场景。命令可以直接写在命令行上并用分号串联。

该控制台可以本地或远程连接 Deluge 守护进程，通过终端界面提供与 GTK 客户端相同的功能。

# CAVEATS

需要 **deluged** 守护进程正在运行。交互模式需要支持 curses 的终端。远程连接需要正确配置认证。命令语法与 GTK 界面不同。

# HISTORY

**deluge-console** 是 Deluge 项目的一部分，为 BitTorrent 客户端提供终端访问能力。它满足了无头服务器管理和脚本化种子操作的需求。

# INSTALL

```dnf: sudo dnf install deluge```

```pacman: sudo pacman -S deluge```

```apk: sudo apk add deluge```

```zypper: sudo zypper install deluge```

```nix: nix profile install nixpkgs#deluge```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[deluge](/man/deluge)(1), [deluged](/man/deluged)(1), [transmission-remote](/man/transmission-remote)(1)
