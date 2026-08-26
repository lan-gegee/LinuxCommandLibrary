# TAGLINE

基于终端的 BitTorrent 客户端

# TLDR

**启动 rtorrent** 并加载种子文件或磁力链接

```rtorrent [path/to/file.torrent]```

**开始一个下载**（在 rtorrent 内）

```Ctrl+s```

**停止一个下载**（在 rtorrent 内）

```Ctrl+d```

**查看**选中种子的**详情**

```Right Arrow```

安全**关闭** rtorrent

```Ctrl+q```

启动时**设置下载目录**

```rtorrent -d [path/to/download/directory]```

# SYNOPSIS

**rtorrent** [_options_] [_torrent_|_magnet_]

# PARAMETERS

**-d** _directory_
> 设置默认下载目录。

**-n**
> 启动时不加载 ~/.rtorrent.rc 配置文件。

**-o** _key=value_
> 直接从命令行设置某个配置项。

**-s** _directory_
> 会话目录，用于在重启之间保存种子状态。

# DESCRIPTION

**rtorrent** 是一个在终端中运行的文本界面 BitTorrent 客户端。它基于 curses 界面提供种子下载功能，便于监控和管理下载任务。

使用键盘快捷键控制下载：Ctrl+s 开始，Ctrl+d 停止或移除（按两次可连同数据一起删除），Ctrl+q 安全退出。按右方向键可查看所选种子的详细信息，按左方向键返回主视图。

# CONFIGURATION

**~/.rtorrent.rc**
> 主配置文件，控制下载目录、连接数限制、端口范围、DHT 设置和限速速率。

**/etc/rtorrent/rtorrent.rc**
> 系统级配置文件，在没有用户配置时作为后备使用。

# CAVEATS

通过 ~/.rtorrent.rc 文件进行配置。要获得最佳速度需要正确的端口转发。支持磁力链接需要启用 DHT。

# HISTORY

用 C++ 编写的高性能控制台 BitTorrent 客户端。在无头服务器和脚本化环境中广受欢迎。

# INSTALL

```apt: sudo apt install rtorrent```

```dnf: sudo dnf install rtorrent```

```pacman: sudo pacman -S rtorrent```

```apk: sudo apk add rtorrent```

```zypper: sudo zypper install rtorrent```

```brew: brew install rtorrent```

```nix: nix profile install nixpkgs#rtorrent```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-cli](/man/transmission-cli)(1), [aria2c](/man/aria2c)(1), [deluge](/man/deluge)(1)
