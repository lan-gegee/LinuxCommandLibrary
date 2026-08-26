# TAGLINE

监督长时间运行的 LVM 操作的 LVM 轮询守护进程

# TLDR

以前台模式启动守护进程

```lvmpolld -f```

以前台模式和**调试日志**启动

```lvmpolld -f -l debug```

设置**空闲关闭超时**（秒）

```lvmpolld -t [300]```

使用**自定义套接字**路径

```lvmpolld -s [/tmp/lvmpolld.socket]```

使用**自定义 PID 文件**

```lvmpolld -p [/tmp/lvmpolld.pid]```

**转储当前状态**

```lvmpolld --dump```

# SYNOPSIS

**lvmpolld** [_options_]

# PARAMETERS

**-f**, **--foreground**
> 以前台运行而非守护进程化

**-l**, **--log** _level_
> 设置日志级别（debug、info、warn、error）

**-t**, **--timeout** _seconds_
> 设置空闲关闭超时；守护进程空闲这么长时间后退出

**-s**, **--socket** _path_
> 使用自定义 Unix 套接字路径进行通信

**-p**, **--pidfile** _path_
> 使用自定义 PID 文件位置

**--dump**
> 转储守护进程的当前状态并退出

# DESCRIPTION

**lvmpolld** 是 LVM 的轮询守护进程，监督诸如 pvmove、lvconvert 镜像转换和精简池扩展等长时间运行的 LVM 操作。它监视这些操作并更新其进度，使发起操作的命令得以返回，而工作继续在后台进行。

当 LVM 命令启动一个被轮询的操作时，lvmpolld 会跟踪其完成状态。守护进程在需要时自动启动，并在一段可配置的空闲时间后关闭。

守护进程通过 Unix 套接字通信，通常位于 /run/lvm/lvmpolld.socket，并维护活动操作的状态。

# CAVEATS

通常由 LVM 命令自动启动；很少需要手动调用。如果守护进程在某项活动操作期间崩溃，重新运行原始命令即可恢复轮询。**--dump** 选项可用于调试活动操作。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2-lockd```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(1), [pvmove](/man/pvmove)(1), [lvconvert](/man/lvconvert)(1), [lvmconfig](/man/lvmconfig)(1)
