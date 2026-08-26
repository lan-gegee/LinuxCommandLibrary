# TAGLINE

DNS 委派追踪工具

# TLDR

追踪 DNS **解析路径**

```dnstracer [www.example.com]```

从**指定的 DNS 服务器**开始追踪

```dnstracer -s [dns.example.org] [www.example.com]```

只查询 **IPv4 服务器**

```dnstracer -4 [www.example.com]```

失败时**重试** 5 次

```dnstracer -r [5] [www.example.com]```

显示**所有步骤**

```dnstracer -v [www.example.com]```

显示应答的**概览**

```dnstracer -o [www.example.com]```

# SYNOPSIS

**dnstracer** [_options_] _name_

# DESCRIPTION

**dnstracer** 通过追踪从根服务器到权威域名服务器的 DNS 解析路径，确定某个 DNS 服务器的信息来源。

可用于调试 DNS 问题以及理解 DNS 委派机制。

# PARAMETERS

**-s** _server_
> 从指定的 DNS 服务器开始追踪

**-4**
> 只查询 IPv4 服务器

**-6**
> 只查询 IPv6 服务器

**-r** _count_
> 失败时的重试次数

**-v**
> 详细输出

**-o**
> 显示所有收到的应答概览

# CAVEATS

需要能够访问 DNS 服务器的网络。对于复杂的委派链，追踪可能耗时较长。某些 DNS 服务器可能会阻止追踪查询。

# INSTALL

```apt: sudo apt install dnstracer```

```dnf: sudo dnf install dnstracer```

```apk: sudo apk add dnstracer```

```zypper: sudo zypper install dnstracer```

```brew: brew install dnstracer```

```nix: nix profile install nixpkgs#dnstracer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [nslookup](/man/nslookup)(1), [host](/man/host)(1)

# RESOURCES

```[Homepage](https://www.mavetju.org/unix/dnstracer.php)```

<!-- verified: 2026-07-11 -->
