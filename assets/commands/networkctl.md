# TAGLINE

查询并控制 systemd-networkd 所见网络链路的状态

# TLDR

列出所有网络**链路**及其状态

```networkctl list```

显示整体**网络状态**

```networkctl status```

**启用**网络设备

```networkctl up eth0```

**停用**网络设备

```networkctl down eth0```

**续租** DHCP 租约

```networkctl renew eth0```

**重新加载**网络配置文件

```networkctl reload```

**重新配置**网络接口

```networkctl reconfigure eth0```

# SYNOPSIS

**networkctl** [_OPTIONS_] _COMMAND_ [_LINK_...]

# DESCRIPTION

**networkctl** 用于查询并控制 systemd-networkd 所见网络链路的状态。它提供对 systemd 网络守护进程所管理网络接口的管理控制能力。

# COMMANDS

**list [PATTERN]**
> 显示现有链路及其状态；支持模式匹配

**status [LINK]**
> 显示链路的详细信息，包括类型、状态、DNS 和 IP 地址

**lldp [LINK]**
> 显示发现的 LLDP 邻居信息

**label**
> 显示用于地址选择的数值型地址标签

**delete LINK**
> 移除虚拟网络设备

**up LINK**
> 启用网络设备

**down LINK**
> 停用网络设备

**renew LINK**
> 刷新动态配置（DHCP 地址）

**forcerenew LINK**
> 触发已连接客户端的 DHCP 重新配置

**reconfigure LINK**
> 重新应用网络接口设置

**reload**
> 重新加载 .netdev 和 .network 配置文件

**edit FILE**
> 修改网络配置文件

**cat FILE**
> 显示网络配置文件的内容

# PARAMETERS

**-a, --all**
> 显示所有链路及其状态

**-s, --stats**
> 包含链路统计信息

**-l, --full**
> 禁止截断输出

**-n, --lines=NUM**
> 控制 journal 输出行数（默认：10）

**--json=MODE**
> 将输出格式化为 JSON（short/pretty/off）

**--drop-in=NAME**
> 编辑 drop-in 配置文件

**--no-reload**
> 编辑后跳过服务重新加载

# CAVEATS

该工具通过 systemd-networkd 而非 NetworkManager 管理接口。配置文件保存在 /etc/systemd/network/。通过 **reload** 进行的更改需要执行 **reconfigure** 才能在运行中的接口上生效。

# HISTORY

作为 **systemd** 的组成部分，networkctl 的引入为 systemd-networkd 的网络配置提供了命令行管理方式，为服务器和嵌入式系统提供了 NetworkManager 之外的另一种选择。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8)
