# TAGLINE

配置路由器上的 UPnP 端口转发

# TLDR

将外部端口**转发**到本地

```upnpc -a [192.168.0.1] 8080 80 tcp```

**删除**端口转发

```upnpc -d 80 tcp```

获取**设备**信息

```upnpc -s```

**列出**已有的端口重定向

```upnpc -l```

# SYNOPSIS

**upnpc** [_OPTIONS_] [_COMMAND_]

# PARAMETERS

**-a** _IP_ _INTERNAL_PORT_ _EXTERNAL_PORT_ _PROTOCOL_
> 添加端口映射

**-d** _EXTERNAL_PORT_ _PROTOCOL_
> 删除端口映射

**-s**
> 显示 UPnP 设备信息

**-l**
> 列出已有的端口重定向

# DESCRIPTION

**upnpc** 使用 UPnP（Universal Plug and Play，通用即插即用）协议在路由器上配置端口转发规则。它让应用程序可以自动建立端口转发，无需手动配置路由器。

该工具能够添加、删除和列出端口映射，还可以查询网络中支持 UPnP 的设备信息。

# CAVEATS

路由器必须支持并已启用 UPnP。一些 ISP 提供的路由器出于安全考虑禁用了 UPnP。端口映射可能是临时的。UPnP 本身存在安全风险。

# HISTORY

**upnpc** 是 **miniupnpc** 库的一部分，通过命令行提供对 UPnP Internet Gateway Device 功能的访问。

# INSTALL

```apt: sudo apt install miniupnpc```

```dnf: sudo dnf install miniupnpc```

```pacman: sudo pacman -S miniupnpc```

```apk: sudo apk add miniupnpc```

```zypper: sudo zypper install miniupnpc```

```brew: brew install miniupnpc```

```nix: nix profile install nixpkgs#miniupnpc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8)
