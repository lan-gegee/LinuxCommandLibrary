# TAGLINE

配置 systemd-resolved DNS 解析器

# TLDR

**编辑 resolved 配置**

```sudo vi /etc/systemd/resolved.conf```

**重启 resolved**

```sudo systemctl restart systemd-resolved```

**检查状态**

```resolvectl status```

# SYNOPSIS

**/etc/systemd/resolved.conf** configuration file

# DESCRIPTION

**resolved.conf** 用于配置 systemd-resolved（系统 DNS 解析器服务）。它管理 DNS 服务器、DNSSEC、DNS-over-TLS 和缓存。

# CONFIGURATION

**/etc/systemd/resolved.conf**
> systemd-resolved 的主配置文件，使用 INI 格式，位于 **[Resolve]** 小节之下。

**DNS=**
> 以空格分隔的 DNS 服务器地址列表，用于名称解析。

**FallbackDNS=**
> 在未配置其他服务器时使用的后备 DNS 服务器。

**Domains=**
> 搜索域和路由域。使用 **~.** 可将所有查询路由到已配置的 DNS 服务器。

**DNSSEC=**
> DNSSEC 验证模式：**yes**、**no** 或 **allow-downgrade**。

**DNSOverTLS=**
> DNS-over-TLS 模式：**yes**、**no** 或 **opportunistic**。

**Cache=**
> 启用或禁用 DNS 应答缓存。

**DNSStubListener=**
> 控制 127.0.0.53 上的本地 stub 解析器监听器。

# EXAMPLES

```bash
# Use Cloudflare DNS
sudo sed -i 's/#DNS=/DNS=1.1.1.1 1.0.0.1/' /etc/systemd/resolved.conf

# Enable DNS-over-TLS
sudo sed -i 's/#DNSOverTLS=/DNSOverTLS=yes/' /etc/systemd/resolved.conf

# Restart
sudo systemctl restart systemd-resolved

# Check status
resolvectl status
```

# CAVEATS

需要 systemd-resolved 正在运行。可能与 NetworkManager 的 DNS 冲突。更改后需要重启服务。

# HISTORY

systemd-resolved 于 **systemd 213** 中引入，是一个集成的 DNS 解析器服务。

# SEE ALSO

[systemd-resolve](/man/systemd-resolve)(1), [resolvectl](/man/resolvectl)(1)
