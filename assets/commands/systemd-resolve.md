# TAGLINE

已弃用的 DNS 解析器，请改用 resolvectl

# TLDR

**查看**更名后命令的文档

```tldr resolvectl```

# SYNOPSIS

**systemd-resolve** [_options_] [_hostname_|_address_|_record_]

# DESCRIPTION

**systemd-resolve** 在较新版本的 systemd 中已更名为 **resolvectl**。解析域名、IPv4/IPv6 地址、DNS 资源记录以及服务的功能现在由 resolvectl 命令提供。

# CAVEATS

此命令已被弃用。进行 DNS 解析和管理 systemd-resolved 请改用 **resolvectl**。

# SEE ALSO

[resolvectl](/man/resolvectl)(1)
