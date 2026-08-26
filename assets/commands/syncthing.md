# TAGLINE

点对点的持续文件同步

# TLDR

**启动 syncthing**

```syncthing```

**启动时不打开浏览器**

```syncthing --no-browser```

**以指定的主目录启动**

```syncthing --home=[/path/to/config]```

**生成密钥和配置**

```syncthing --generate=[/path/to/config]```

**重置为默认配置**

```syncthing --reset-deltas```

**显示设备 ID**

```syncthing --device-id```

**显示版本**

```syncthing --version```

# SYNOPSIS

**syncthing** [_--home dir_] [_--no-browser_] [_--gui-address addr_] [_options_]

# PARAMETERS

**--home** _DIR_
> 配置目录。

**--config** _DIR_
> 配置文件路径。

**--data** _DIR_
> 数据目录路径。

**--no-browser**
> 启动时不打开浏览器。

**--gui-address** _ADDR_
> GUI 监听地址。

**--gui-apikey** _KEY_
> 覆盖 GUI API 密钥。

**--no-restart**
> 升级后不重启。

**--device-id**
> 打印设备 ID 并退出。

**--generate** _DIR_
> 生成密钥和配置。

**--reset-database**
> 重置数据库。

**--reset-deltas**
> 重置增量索引。

**--logfile** _FILE_
> 记录日志到文件。

**--logflags** _FLAGS_
> 日志标志。

**--paused**
> 以所有设备暂停的状态启动。

**--verbose**
> 详细输出。

# DESCRIPTION

**Syncthing** 是一个持续文件同步程序。它在设备之间实时、点对点地同步文件，无需中央服务器。

设备通过本地网络、全局发现服务器或手动配置相互发现。数据使用 TLS 加密在设备之间直接传输。任何第三方服务器都无法访问文件内容。

Web GUI（默认：localhost:8384）提供配置和监控功能。通过交换 Device ID（一长串加密标识符）来添加设备。共享文件夹按设备配置，并使用特定的文件夹 ID。

当同一文件在多台设备上于同步前被修改时，冲突处理会创建副本。版本历史可以保留旧版本文件以供恢复。

选择性同步支持通过模式忽略文件。文件监视可在大多数平台上立即检测到变更，周期性扫描则可捕捉任何遗漏的更改。

Syncthing 以守护进程方式运行，通常在登录时或作为系统服务启动。可以使用不同的主目录运行多个实例。

# CONFIGURATION

**~/.config/syncthing/config.xml**
> 主配置文件，定义设备、共享文件夹和同步设置。

**STTRACE**
> 环境变量，用于启用特定子系统的调试跟踪。

# CAVEATS

大数据集的初始同步耗时较长。冲突文件需要手动解决。持续同步会占用带宽。发现服务器是公开的（但数据不是）。某些文件系统不支持所需特性。移动端电量消耗可能相当可观。

# HISTORY

**Syncthing** 由 **Jakob Borg** 于 **2013 年**创建，定位为 Dropbox 等专有同步服务的开源替代品。它强调隐私（无中央服务器）、安全（所有数据加密）与开放（开源、开放协议）。该项目已发展为广泛使用的同步方案。

# INSTALL

```apt: sudo apt install syncthing```

```dnf: sudo dnf install syncthing```

```pacman: sudo pacman -S syncthing```

```apk: sudo apk add syncthing```

```zypper: sudo zypper install syncthing```

```brew: brew install syncthing```

```nix: nix profile install nixpkgs#syncthing```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [rclone](/man/rclone)(1), [unison](/man/unison)(1)
