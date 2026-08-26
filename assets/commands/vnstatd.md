# TAGLINE

网络流量统计收集守护进程

# TLDR

**启动守护进程**

```sudo systemctl start vnstat```

**设置开机自启**

```sudo systemctl enable vnstat```

**在前台运行守护进程**

```vnstatd -n```

**带调试输出运行**

```vnstatd -D```

**同步数据库后退出**

```vnstatd --sync```

# SYNOPSIS

**vnstatd** [_options_]

# PARAMETERS

**-d**, **--daemon**
> 以守护进程方式转入后台。

**-n**, **--nodaemon**
> 保持在前台。

**-s**, **--sync**
> 将缓存数据同步到数据库后退出。

**-D**, **--debug**
> 启用调试输出。

**--config** _file_
> 使用指定的配置文件。

**-p**, **--pidfile** _file_
> 使用指定的 PID 文件。

**--noadd**
> 不自动添加新接口。

**-v**, **--version**
> 显示版本。

# DESCRIPTION

**vnstatd** 是 vnStat 的守护进程组件，负责收集网络流量统计信息。它按配置的间隔从内核读取接口计数器，并将数据存储在持久化数据库中。

该守护进程可同时跟踪多个接口，记录 5 分钟、小时、天、月和年级别的统计。它会自动检测新加入数据库的接口，无需重启。

由于 vnstatd 读取的是内核计数器而非捕获数据包，资源占用极低。数据在重启后依然保留，适合长期带宽监控。

# CONFIGURATION

配置文件：/etc/vnstat.conf

关键设置包括被监控的接口、数据库位置、更新间隔和数据保留期限。

# CAVEATS

统计从守护进程启动时才开始，没有历史数据。内核计数器重置（重启、接口变更）可能导致不准确。非正常关机可能损坏数据库。

# HISTORY

**vnstatd** 是 vnStat 的一部分，由 Teemu Toivola 创建，用于轻量级网络流量监控。该项目始于 2002 年，现已成为 Linux 服务器和嵌入式系统上带宽监控的标准工具。

# INSTALL

```apt: sudo apt install vnstat```

```dnf: sudo dnf install vnstat```

```pacman: sudo pacman -S vnstat```

```apk: sudo apk add vnstat```

```zypper: sudo zypper install vnstat```

```brew: brew install vnstat```

```nix: nix profile install nixpkgs#vnstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vnstat](/man/vnstat)(1), [vnstati](/man/vnstati)(1), [iftop](/man/iftop)(8), [nethogs](/man/nethogs)(8)
