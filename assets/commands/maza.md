# TAGLINE

通过修改 /etc/hosts 工作的本地广告拦截器

# TLDR

**启用广告拦截**

```maza start```

**禁用广告拦截**

```maza stop```

**更新屏蔽列表**

```maza update```

**显示状态**

```maza status```

# SYNOPSIS

**maza** [_start_] [_stop_] [_update_] [_status_]

# PARAMETERS

**start**
> 启用广告拦截。

**stop**
> 禁用广告拦截。

**update**
> 更新屏蔽列表。

**status**
> 显示当前状态。

# DESCRIPTION

**maza** 是一个通过修改 /etc/hosts 工作的本地广告拦截器。它将广告和跟踪域名重定向到 127.0.0.1，从而阻止连接。

该工具从 Steven Black 的 hosts 项目等来源下载屏蔽列表，该项目聚合了多个来源。更新操作会获取最新的列表。

start 模式会备份现有的 hosts 文件并追加拦截条目。stop 模式恢复原始 hosts 文件，移除所有拦截规则。

这种方式在整个系统范围内生效，能拦截所有应用中的广告，而不仅仅是浏览器。它非常轻量，无需守护进程或浏览器扩展。

DNS 缓存可能会延迟更改生效。刷新 DNS 缓存或重启网络服务可以加快传播。

# CAVEATS

需要 root/sudo 权限。过大的 hosts 文件可能会略微减慢 DNS 解析速度。部分网站会检测广告拦截。无法拦截与内容同域提供的广告。VPN 可能绕过 hosts 文件。

# HISTORY

**maza** 创建于 **2019 年**前后，是 Pi-hole 及其他广告拦截方案的简单 shell 脚本替代品。它提供基础功能，无需额外的服务或基础设施。

# SEE ALSO

[pihole](/man/pihole)(1), [dnsmasq](/man/dnsmasq)(8), [unbound](/man/unbound)(8)
