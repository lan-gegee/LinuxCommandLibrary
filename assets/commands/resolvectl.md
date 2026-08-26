# TAGLINE

查询和管理 systemd-resolved 的 DNS 设置

# TLDR

显示 **DNS 设置**

```resolvectl status```

**解析**域名

```resolvectl query domain1 domain2```

对 IP 地址进行**反向查询**

```resolvectl query 8.8.8.8```

**刷新** DNS 缓存

```resolvectl flush-caches```

显示 DNS **统计信息**

```resolvectl statistics```

查询域名的 **MX 记录**

```resolvectl --type MX query domain```

查询 **SRV 记录**

```resolvectl service _xmpp-server._tcp example.com```

查询 **TLS 密钥**

```resolvectl tlsa tcp example.com:443```

# SYNOPSIS

**resolvectl** [_OPTIONS_] _COMMAND_ [_NAME_...]

# DESCRIPTION

**resolvectl** 解析域名、IPv4 和 IPv6 地址、DNS 资源记录以及服务。它通过 systemd-resolved 内省并重新配置 DNS 解析器。

# COMMANDS

**query HOSTNAME|ADDRESS**
> 解析主机名或对地址进行反向查询

**service [[NAME] TYPE] DOMAIN**
> 解析 DNS-SD 或 SRV 服务

**openpgp EMAIL**
> 查询 OpenPGP 密钥

**tlsa [FAMILY] DOMAIN[:PORT]**
> 查询 TLS 服务器证书

**status [LINK]**
> 显示每个接口的 DNS 设置

**statistics**
> 显示解析器统计信息

**reset-statistics**
> 重置解析器统计信息

**flush-caches**
> 刷新所有本地 DNS 缓存

**reset-server-features**
> 重置已学习的服务器特性

**dns [LINK [SERVER...]]**
> 获取/设置每个链路的 DNS 服务器

**domain [LINK [DOMAIN...]]**
> 获取/设置每个链路的搜索域

**dnssec [LINK [MODE]]**
> 获取/设置 DNSSEC 模式

**nta [LINK [DOMAIN...]]**
> 获取/设置 DNSSEC 负信任锚点

# PARAMETERS

**-4, --ipv4**
> 只查询 IPv4 地址

**-6, --ipv6**
> 只查询 IPv6 地址

**-t, --type TYPE**
> 查询指定的 DNS 记录类型

**--class CLASS**
> 查询指定的 DNS 类

**--legend yes|no**
> 显示/隐藏结果图例

**--cname yes|no**
> 跟随 CNAME 重定向

**-p, --protocol**
> 指定协议（dns、llmnr、mdns）

# CAVEATS

需要 **systemd-resolved** 正在运行，且 `/etc/resolv.conf` 指向其 stub 解析器（`127.0.0.53`），主机名解析才会实际使用它。每个链路的设置（`dns`、`domain`、`dnssec`）只在接口下次启用前生效，除非通过 `systemd-networkd` 的 .network 文件或 NetworkManager 持久化。`flush-caches` 会丢弃缓存的应答，但不会更改已配置的上游服务器。

# HISTORY

**resolvectl** 是 **systemd** 的一部分，通过 systemd-resolved 提供 DNS 解析。它取代了较旧的 systemd-resolve 命令。

# INSTALL

```apt: sudo apt install systemd-resolved```

```dnf: sudo dnf install systemd-resolved```

```zypper: sudo zypper install systemd-resolved```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [nslookup](/man/nslookup)(1), [resolved.conf](/man/resolved.conf)(5)
