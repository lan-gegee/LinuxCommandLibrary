# TAGLINE

为内核密钥环解析 DNS 密钥

# TLDR

**解析 DNS 密钥**

```key.dns_resolver [domain]```

**解析 DNSSEC 密钥**

```key.dns_resolver -t DNSKEY [domain]```

# SYNOPSIS

**key.dns_resolver** [_options_] _domain_

# PARAMETERS

_DOMAIN_
> 要为其解析密钥的域。

**-t** _TYPE_
> 密钥类型（DNSKEY、DS）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**key.dns_resolver** 是一个 Linux 内核工具，用于解析 DNS 安全密钥并将其存储在内核密钥环中。它主要用于 DNSSEC 验证，从 DNS 服务器获取 DNSKEY 和 DS 记录，供需要验证 DNS 响应真实性的内核子系统使用。

该工具作为内核密钥管理设施（request-key）调用的辅助程序运行，在大多数情况下并不由用户直接调用。当内核出于认证目的需要某个 DNS 密钥时，它会触发 key.dns_resolver 执行查询并自动填充密钥环。这一机制支持基于 DNS 的命名实体认证（DANE）以及其他依赖 DNS 中发布的加密密钥的安全协议。

# CAVEATS

依赖内核密钥环集成。需要 DNSSEC 基础设施。仅限 Linux。

# HISTORY

key.dns_resolver 是 **Linux 内核** 密钥环实用程序的一部分，为 DNSSEC 提供基于 DNS 的密钥解析支持。

# INSTALL

```apt: sudo apt install keyutils```

```dnf: sudo dnf install keyutils```

```pacman: sudo pacman -S keyutils```

```apk: sudo apk add keyutils```

```zypper: sudo zypper install keyutils```

```brew: brew install keyutils```

```nix: nix profile install nixpkgs#keyutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[keyctl](/man/keyctl)(1), [dig](/man/dig)(1)
