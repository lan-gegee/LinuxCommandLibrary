# TAGLINE

带 Web 界面的开源 BitTorrent 客户端

# TLDR

**启动 qBittorrent 图形界面**

```qbittorrent```

**打开种子文件**

```qbittorrent [file.torrent]```

**运行无界面守护进程**

```qbittorrent-nox```

**Web UI 模式**

```qbittorrent-nox --webui-port=[8080]```

# SYNOPSIS

**qbittorrent** [_options_] [_torrent_files_|_urls_]

**qbittorrent-nox** [_options_]

# PARAMETERS

**--no-splash**
> 启动时禁用启动画面（仅限 GUI）。

**--webui-port=**_port_
> 设置 Web UI 端口（默认：8080）。

**-d**, **--daemon**
> 在后台作为守护进程运行（仅 nox）。

**--version**
> 显示版本号。

**--help**
> 显示帮助。

# DESCRIPTION

**qBittorrent** 是一个免费开源的 BitTorrent 客户端。它提供基于 Qt 的图形界面，以及面向服务器的无界面版本（qbittorrent-nox）并附带 Web 界面。

# EXAMPLES

```bash
# Launch GUI
qbittorrent

# Open specific torrent
qbittorrent file.torrent

# Start headless daemon
qbittorrent-nox -d

# Web UI on custom port
qbittorrent-nox --webui-port=8090

# Add magnet link
qbittorrent "magnet:?xt=urn:btih:..."
```

# WEB UI

Default: http://localhost:8080
- Username: admin
- Password: adminadmin (should be changed on first login)

# CONFIGURATION

**~/.config/qBittorrent/**
> 主配置目录，包含设置、RSS 订阅源和 Web UI 偏好。

**~/.local/share/qBittorrent/**
> 数据目录，存储下载历史、种子续传数据和日志。

# CAVEATS

Web UI 出厂自带默认凭据（admin/adminadmin）；请立即修改密码。要获得最佳下载/上传速度可能需要端口转发。

# HISTORY

qBittorrent 由 **Christophe Dumez** 于 2006 年发起，作为基于 Qt 的 uTorrent 替代品。

# INSTALL

```apt: sudo apt install qbittorrent```

```dnf: sudo dnf install qbittorrent```

```pacman: sudo pacman -S qbittorrent```

```apk: sudo apk add qbittorrent```

```zypper: sudo zypper install qbittorrent```

```nix: nix profile install nixpkgs#qbittorrent```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission](/man/transmission)(1), [deluge](/man/deluge)(1), [aria2c](/man/aria2c)(1), [rtorrent](/man/rtorrent)(1)
