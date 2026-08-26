# TAGLINE

Unbound DNS 解析器的远程控制接口

# TLDR

**检查服务器状态**

```unbound-control status```

**查看统计数据**

```unbound-control stats```

**重新加载配置**

```unbound-control reload```

**清空整个缓存**

```unbound-control flush_zone [.]```

**清除特定域名**

```unbound-control flush [example.com]```

**添加本地区域**

```unbound-control local_zone [example.com] [static]```

**添加本地数据**

```unbound-control local_data "[example.com. A 192.168.1.1]"```

**列出转发区域**

```unbound-control list_forwards```

# SYNOPSIS

**unbound-control** [_options_] _command_

# COMMANDS

**start**: 启动服务器。

**stop**: 停止服务器。

**reload**: 重新加载配置。

**status**: 显示服务器状态。

**stats**: 显示统计数据。

**stats_noreset**: 查看统计但不重置计数器。

**flush** _name_: 从缓存中清除指定名称。

**flush_type** _name_ _type_: 清除特定的 RR 类型。

**flush_zone** _name_: 清除整个区域。

**local_zone** _name_ _type_: 添加本地区域。

**local_data** _RR_: 添加本地数据。

**local_data_remove** _name_: 移除本地数据。

**forward_add** _zone_ _addr_: 添加转发区域。

**forward_remove** _zone_: 移除转发区域。

**list_forwards**: 列出转发区域。

**list_stubs**: 列出存根（stub）区域。

**dump_cache**: 将缓存转储到 stdout。

**load_cache**: 从 stdin 加载缓存。

# PARAMETERS

**-c** _file_
> 配置文件路径。

**-s** _server_
> 要连接的服务器地址。

**-q**
> 安静模式。

**-h**
> 显示帮助。

# DESCRIPTION

**unbound-control** 是用于管理 Unbound DNS 解析器守护进程的工具。它通过使用 TLS 证书的安全通道与运行中的 unbound 服务器通信。

使用前，先运行 **unbound-control-setup** 生成所需的证书和密钥。必须在 unbound.conf 中启用 remote-control 部分。

该工具支持运行时配置更改，包括缓存管理、添加本地区域和数据，以及修改转发设置而无需重启服务器。

# CAVEATS

需要先运行 unbound-control-setup 生成初始证书。服务器必须启用远程控制。通过 unbound-control 所做的更改在重启后不会保留，除非同时写入配置文件。

# HISTORY

**unbound-control** 是由 NLnet Labs 开发的 Unbound DNS 解析器的一部分。Unbound 是一个验证型递归缓存 DNS 解析器，专为高性能和安全设计，支持 DNSSEC。

# INSTALL

```apt: sudo apt install unbound```

```dnf: sudo dnf install unbound```

```pacman: sudo pacman -S unbound```

```apk: sudo apk add unbound```

```zypper: sudo zypper install unbound```

```brew: brew install unbound```

```nix: nix profile install nixpkgs#unbound```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unbound](/man/unbound)(8), [unbound-checkconf](/man/unbound-checkconf)(8), [unbound-host](/man/unbound-host)(1)
