# TAGLINE

轻量级 BitTorrent 客户端套件

# TLDR

**启动 GTK 客户端**

```transmission-gtk```

**启动 Qt 客户端**

```transmission-qt```

**启动守护进程**

```transmission-daemon```

**控制守护进程**

```transmission-remote```

**下载种子**

```transmission-cli [file.torrent]```

**向守护进程添加种子**

```transmission-remote -a [file.torrent]```

**列出种子**

```transmission-remote -l```

# SYNOPSIS

**transmission-gtk** | **transmission-qt** | **transmission-daemon** | **transmission-remote** | **transmission-cli**

# COMMANDS

**transmission-gtk**
> GTK 图形客户端。

**transmission-qt**
> Qt 图形客户端。

**transmission-daemon**
> 后台守护进程。

**transmission-remote**
> 远程控制。

**transmission-cli**
> 命令行客户端。

**transmission-create**
> 创建种子。

**transmission-show**
> 显示种子信息。

**transmission-edit**
> 修改现有的种子文件。

# DESCRIPTION

**Transmission** 是一个轻量级的跨平台 BitTorrent 客户端，以简洁和低资源占用著称。其所有界面变体——GTK、Qt、Web、CLI 和守护进程——共享同一核心后端引擎，无论以何种方式访问，行为都保持一致。

桌面图形客户端（transmission-gtk 和 transmission-qt）提供管理种子的图形界面。对于无头服务器，transmission-daemon 在后台运行，可通过内置 Web 界面或 transmission-remote 命令行工具控制。独立的 transmission-cli 提供简单的单种子下载功能，无需守护进程。

其他实用工具包括用于构建新种子文件的 transmission-create、检查种子元数据的 transmission-show，以及修改现有种子文件的 transmission-edit。该套件支持节点交换、DHT、磁力链接、加密和带宽调度等功能。

# CAVEATS

每种界面由不同的软件包提供。守护进程需要配置。可能需要设置端口转发。

# HISTORY

**Transmission** 创建于 **2005 年**，专注于简洁和低资源占用。凭借简洁的设计和跨平台支持而广受欢迎。

# INSTALL

```dnf: sudo dnf install transmission```

```zypper: sudo zypper install transmission```

```brew: brew install transmission```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-remote](/man/transmission-remote)(1), [aria2c](/man/aria2c)(1), [qbittorrent](/man/qbittorrent)(1)
