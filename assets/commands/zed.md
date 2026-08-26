# TAGLINE

ZFS 事件监控守护进程

# TLDR

**以前台模式启动 zed**

```sudo zed -F```

**以详细输出启动 zed**

```sudo zed -v```

**在前台运行且不使用状态文件**

```sudo zed -M```

**指定替代的配置目录**

```sudo zed -d [/etc/zfs/zed.d]```

# SYNOPSIS

**zed** [**-FhMvV**] [**-c** _conffile_] [**-d** _confdir_] [**-I** _idle_] [**-p** _pidfile_] [**-P** _path_] [**-s** _statefile_]

# PARAMETERS

**-c** _conffile_
> 从指定的文件读取配置

**-d** _confdir_
> 从目录读取已启用的脚本（默认：/etc/zfs/zed.d）

**-F**
> 在前台运行，不守护进程化

**-h**
> 显示帮助信息

**-I** _idle_
> 脚本执行的空闲超时时间（秒）

**-M**
> 忽略缺失的状态文件

**-p** _pidfile_
> 将进程 ID 写入文件

**-P** _path_
> 为脚本执行设置 PATH

**-s** _statefile_
> 将状态写入文件

**-v**
> 详细模式，将事件记录到 stderr

**-V**
> 显示版本

# DESCRIPTION

**zed**（ZFS Event Daemon）监控 ZFS 内核事件并执行脚本作为响应。它监听诸如 scrub 完成、设备故障、存储池导入和数据错误等事件，然后运行相应的处理脚本。

脚本存放在 **/etc/zfs/zed.d/** 中，命名约定为 **事件名.sh**。被启用的脚本通过符号链接激活。常见事件包括：

- **resilver.finish** - 重建（resilver）完成
- **scrub.finish** - 清理（scrub）完成
- **statechange** - 存储池状态改变
- **data** - 检测到数据错误

zed 可以自动响应 ZFS 事件，例如在出错时发送电子邮件通知或运行自定义维护脚本。

# CAVEATS

zed 必须 root 身份运行才能接收内核事件和访问存储池信息。

脚本执行默认是串行的。长时间运行的脚本会延迟后续事件的处理。

编写不佳的事件脚本可能导致系统问题。启用前请充分测试脚本。

在 systemd 系统上，zed 通常作为 systemd 服务运行（zfs-zed.service）。

# INSTALL

```pacman: sudo pacman -S zed```

```apk: sudo apk add zfs```

```nix: nix profile install nixpkgs#zfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zfs](/man/zfs)(8), [zpool](/man/zpool)(8), [zpool-events](/man/zpool-events)(8)
