# TAGLINE

支持 DNSSEC 的 DNS 查询工具

# TLDR

**查询 A 记录**

```drill [example.com]```

**查询指定类型**的记录

```drill [example.com] [MX]```

**使用指定的 DNS** 服务器

```drill @[8.8.8.8] [example.com]```

**追踪委托路径**

```drill -T [example.com]```

**显示 DNSSEC** 信息

```drill -D [example.com]```

用 **TCP 替代 UDP**

```drill -t [example.com]```

**反向 DNS 查询**

```drill -x [8.8.8.8]```

# SYNOPSIS

**drill** [_options_] _name_ [@_server_] [_type_]

# PARAMETERS

_NAME_
> 要查询的域名。

@_SERVER_
> 要查询的 DNS 服务器。

_TYPE_
> 记录类型：A、AAAA、MX、NS、TXT 等。

**-T**
> 从根服务器开始追踪直到得到答案。

**-D**
> 启用 DNSSEC，在查询中设置 DO（DNSSEC OK）位。

**-S**
> 沿签名链向上验证答案，直至已知密钥或信任锚（需要 OpenSSL 支持）。

**-t**
> 使用 TCP 而非 UDP。

**-x**
> 反向 DNS 查询。

**-k** _FILE_
> DNSSEC 的信任锚文件。

**-v**
> 详细输出。

# DESCRIPTION

**drill** 是 ldns 库自带的 DNS 查询工具，定位为 dig 的现代化替代品。它执行 DNS 查询，特别强调 DNSSEC 验证能力。

该工具提供关于 DNS 响应的详细输出，包括标志、各区和耗时。-T 追踪选项沿着从根服务器开始的委托链逐级解析，直观展示 DNS 解析的工作过程。

drill 的 DNSSEC 支持包括签名验证和信任链验证，因此非常适合调试安全的 DNS 配置。

# CAVEATS

装机量不如 dig 普及。输出格式与 dig 存在一些差异。DNSSEC 验证需要正确配置信任锚。

# HISTORY

drill 作为 **ldns** 库的一部分由 **NLnet Labs** 开发，该公司也是 Unbound DNS 的缔造者。它被设计为 dig 的替代品，提供更好的 DNSSEC 支持和更清爽的输出。

# INSTALL

```apt: sudo apt install ldnsutils```

```apk: sudo apk add drill```

```brew: brew install drill```

```nix: nix profile install nixpkgs#drill```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [nslookup](/man/nslookup)(1), [dog](/man/dog)(1), [unbound](/man/unbound)(8)
