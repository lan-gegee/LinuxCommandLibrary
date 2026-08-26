# TAGLINE

使用 video4linux 设备或网络摄像头进行移动侦测

# TLDR

**以默认配置启动移动侦测**

```motion```

**使用指定的配置文件**

```motion -c [/etc/motion/motion.conf]```

**在前台运行（非守护进程模式）**

```motion -n```

**作为后台守护进程运行**

```motion -b```

**以指定级别进行详细日志记录**

```motion -d [1-9]```

**记录到指定文件**

```motion -l [/var/log/motion.log]```

**以暂停模式启动（在被激活前禁用移动侦测）**

```motion -m```

**设置进程 ID 文件**

```motion -p [/var/run/motion.pid]```

# SYNOPSIS

**motion** [**-hbnsm**] [**-c** _config_file_] [**-d** _level_] [**-k** _level_] [**-p** _pid_file_] [**-l** _log_file_]

# PARAMETERS

**-c** _FILE_
> 指定配置文件的路径。

**-n**
> 以非守护进程模式（前台）运行。

**-b**
> 作为后台守护进程运行。

**-s**
> 启用 setup 模式；强制以非守护进程方式执行。

**-d** _level_
> 设置 1 到 9 之间的调试详细程度级别。

**-k** _level_
> 设置 1 到 9 之间的消息日志类型。

**-l** _FILE_
> 指定日志文件路径。

**-p** _FILE_
> 指定进程 ID 文件的位置。

**-m**
> 以暂停模式启动（初始禁用移动侦测）。

**-h**
> 显示帮助信息。

# DESCRIPTION

**motion** 是一个使用 Video4Linux 设备或网络摄像头进行移动侦测的程序。它监控视频画面中的运动，在检测到活动时可以捕获图像和视频序列，还可以执行自动化操作来进行通知或抓拍。

该工具支持多个摄像头、实时串流以及可配置的移动侦测灵敏度。命令行参数会覆盖配置文件中对应的设置。

# CAVEATS

视摄像头分辨率和侦测设置而定，可能占用大量 CPU。需要摄像头访问权限（Video4Linux 或网络摄像头）。多摄像头和高级侦测场景下的配置会变得复杂。

# HISTORY

motion 作为一个 **开源** 移动侦测系统而诞生，面向 Linux 的安防和监控应用。它使用 Video4Linux 接口，已被广泛用于家庭安全和野生动物监测。

# INSTALL

```apt: sudo apt install motion```

```pacman: sudo pacman -S motion```

```zypper: sudo zypper install motion```

```nix: nix profile install nixpkgs#motion```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [v4l2-ctl](/man/v4l2-ctl)(1), [vlc](/man/vlc)(1), [fswebcam](/man/fswebcam)(1), [streamer](/man/streamer)(1)
