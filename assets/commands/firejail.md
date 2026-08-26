# TAGLINE

基于 Linux 命名空间的应用沙箱

# TLDR

**把 firejail 集成**到桌面环境

```sudo firecfg```

打开一个**受限的** Firefox

```firejail [firefox]```

在特定**网络**上启动受限的 Apache

```firejail --net=[eth0] --ip=[192.168.1.244] [/etc/init.d/apache2] [start]```

**列出**正在运行的沙箱

```firejail --list```

列出沙箱的**网络活动**

```firejail --netstats```

**关闭**一个正在运行的沙箱

```firejail --shutdown=[7777]```

运行**高度受限的** Firefox 会话

```firejail --seccomp --private --private-dev --private-tmp --protocol=inet firefox --new-instance --no-remote --safe-mode --private-window```

使用**自定义 hosts** 文件

```firejail --hosts-file=[~/myhosts] [curl http://mysite.arpa]```

# SYNOPSIS

**firejail** [_options_] [_program_] [_arguments_]

# DESCRIPTION

**firejail** 使用 Linux 命名空间、seccomp-bpf 和 capabilities 安全地把进程关进沙箱。出于安全考虑，它会将应用程序与系统的其余部分隔离。

它为 Firefox、VLC 等常见程序提供按应用划分的 profile。

# PARAMETERS

**--list**
> 列出正在运行的沙箱

**--netstats**
> 显示网络活动

**--shutdown** _pid_
> 按 PID 停止沙箱

**--net** _interface_
> 使用网络命名空间

**--ip** _address_
> 分配 IP 地址

**--seccomp**
> 启用 seccomp 过滤

**--private**
> 使用私有的主目录

**--private-tmp**
> 使用私有的 /tmp

**--private-dev**
> 使用私有的 /dev

# CONFIGURATION

**/etc/firejail/[application].profile**
> 应用专属的沙箱 profile，定义各项限制和权限。

**~/.config/firejail/[application].profile**
> 用户级自定义 profile，会覆盖系统默认配置。

# CAVEATS

某些应用在沙箱中可能无法正常运行。系统级 profile 位于 /etc/firejail/。可用 firecfg 完成与桌面环境的集成。

# INSTALL

```apt: sudo apt install firejail```

```dnf: sudo dnf install firejail```

```pacman: sudo pacman -S firejail```

```zypper: sudo zypper install firejail```

```nix: nix profile install nixpkgs#firejail```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bubblewrap](/man/bubblewrap)(1), [systemd-nspawn](/man/systemd-nspawn)(1)

# RESOURCES

```[Source code](https://github.com/netblue30/firejail)```

<!-- verified: 2026-07-15 -->
