# TAGLINE

Linux 动态防火墙守护进程

# TLDR

**启动 firewalld** 守护进程

```sudo systemctl start firewalld```

**设置 firewalld 开机自启**

```sudo systemctl enable firewalld```

**检查 firewalld 状态**

```sudo systemctl status firewalld```

**以调试模式运行 firewalld**（前台）

```sudo firewalld --debug```

**运行 firewalld** 但不 fork 到后台

```sudo firewalld --nofork```

**运行 firewalld** 而不加载模块

```sudo firewalld --nopid```

# SYNOPSIS

**firewalld** [**--debug**] [**--debug-gc**] [**--nofork**] [**--nopid**] [**--system-config** _DIR_] [**--default-config** _DIR_]

# PARAMETERS

**--debug**
> 将日志级别设为 debug 并在前台运行。

**--debug-gc**
> 显示垃圾回收器的内存泄漏信息。

**--nofork**
> 不派生到后台运行（保持在前台）。

**--nopid**
> 不写 PID 文件。

**--system-config** _DIR_
> 系统配置目录的路径。

**--default-config** _DIR_
> 默认配置目录的路径。

**-h**, **--help**
> 显示帮助信息。

# CONFIGURATION

**/etc/firewalld/firewalld.conf**
> 守护进程的主配置，包括默认区域、清理设置和后端选择。

**/etc/firewalld/zones/*.xml**
> 区域定义，控制各网络的信任级别。

**/etc/firewalld/services/*.xml**
> 服务定义，描述端口与协议的映射关系。

# DESCRIPTION

**firewalld** 是一个动态防火墙守护进程，充当 nftables 的前端（也可以选用 iptables 作为传统后端）。它动态地管理防火墙规则，无需打断现有连接或整体重启就能应用变更。

Firewalld 通过**区域（zone）**的概念来定义网络连接的信任级别（public、home、work、trusted 等）。每个区域都有针对允许服务和端口的预置规则。**服务（service）**则为常见应用（ssh、http、https）定义端口和协议。

用户主要通过命令行客户端 **firewall-cmd** 来操作 firewalld。修改可以即时生效（临时），也可以持久化保存（跨重启保留）。守护进程负责规则翻译，并管理底层的包过滤。

# CAVEATS

不要将 firewalld 与 ufw 或直接操作 iptables 等其他防火墙管理方式同时使用。调试模式会生成冗长的输出，仅供排障使用。该守护进程需要 root 权限，通常由 systemd 管理。

# HISTORY

firewalld 由 Red Hat 开发，随 **Fedora 15**（2011 年）推出，用来取代静态的 system-config-firewall 工具。它支持动态管理，无需重启服务。**2018 年**，firewalld 将默认后端从 iptables 切换为 nftables，不过 iptables 支持因兼容性得以保留。

# INSTALL

```dnf: sudo dnf install firewalld```

```pacman: sudo pacman -S firewalld```

```apk: sudo apk add firewalld```

```zypper: sudo zypper install firewalld```

```nix: nix profile install nixpkgs#firewalld```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firewall-cmd](/man/firewall-cmd)(1), [nft](/man/nft)(8), [iptables](/man/iptables)(8)
