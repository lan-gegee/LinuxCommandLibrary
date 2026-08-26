# TAGLINE

使用 Unbound 解析器的 DNS 查询工具

# TLDR

**查询主机名**

```unbound-host [example.com]```

**查询并显示 DNSSEC 验证状态**

```unbound-host -v [example.com]```

**查询特定记录类型**

```unbound-host -t [MX] [example.com]```

**使用默认根信任锚启用 DNSSEC 验证**

```unbound-host -D [example.com]```

**使用 resolv.conf 中的系统解析器**

```unbound-host -r [example.com]```

**使用自定义配置文件**

```unbound-host -C [/etc/unbound/unbound.conf] [example.com]```

**对 IP 地址进行反向查询**

```unbound-host [93.184.216.34]```

**强制仅用 IPv4**

```unbound-host -4 [example.com]```

# SYNOPSIS

**unbound-host** [**-C** _configfile_] [**-vdhr46D**] [**-c** _class_] [**-t** _type_] [**-y** _key_] [**-f** _keyfile_] [**-F** _namedkeyfile_] _hostname_

# PARAMETERS

**-v**
> 启用详细输出，在每一行显示 DNSSEC 验证状态（secure、insecure 或 bogus）。

**-d**
> 启用到 stderr 的调试输出。重复该标志（-d -d）可获得更高详细度，包括完整的数据包细节。

**-t** _type_
> 查询特定记录类型（A、AAAA、MX、TXT、NS、SOA 等）。正向查询默认为 A、AAAA 和 MX，反向查询默认为 PTR。

**-c** _class_
> 查询特定的 DNS 类别。默认为 IN（互联网）。其他值：CH（chaos）、HS（hesiod）。

**-r**
> 读取 /etc/resolv.conf 并使用其中列出的转发 DNS 服务器。注意：如果这些服务器不支持 DNSSEC，可能会破坏验证。

**-f** _keyfile_
> 从区域文件格式的文件中读取 DS 或 DNSKEY 信任锚记录（每行一条记录）。用于为 DNSSEC 验证提供信任锚。

**-F** _namedkeyfile_
> 从 BIND 风格的 named.conf 文件中读取信任锚密钥。只读取 trusted-key {} 条目。

**-y** _key_
> 直接在命令行上以 DS 或 DNSKEY 记录格式指定单个信任锚。

**-D**
> 使用默认位置（依系统而定，/usr/share/dns/root.key 或 /etc/trusted-key.key）的根信任锚启用 DNSSEC 验证。

**-C** _file_
> 使用指定的 unbound.conf 配置文件来配置解析器。

**-4**
> 仅使用 IPv4 发送数据包。

**-6**
> 仅使用 IPv6 发送数据包。

**-h**
> 显示版本和帮助信息。

# DESCRIPTION

**unbound-host** 使用 Unbound 解析器库（libunbound）执行 DNS 查询。它提供 DNSSEC 验证能力，报告响应是 secure（经过加密验证）、insecure（该域名没有 DNSSEC 信任链）还是 bogus（验证失败，可能被篡改）。

如果 _hostname_ 是 IPv4 或 IPv6 地址，则自动执行反向查询（PTR 记录）。

默认情况下，该工具不读取任何配置文件，而是直接尝试连接互联网根服务器。**-r** 选项使用 /etc/resolv.conf 中的解析器，**-C** 加载完整的 unbound 配置。

DNSSEC 验证需要信任锚。使用 **-D** 自动加载根信任锚，或通过 **-y**、**-f**、**-F** 手动提供信任锚。

# EXIT STATUS

**0**
> 成功（尽管所查询的数据可能不存在）。

**1**
> 查询期间发生致命错误。

# CAVEATS

直接查询根服务器可能很慢或被防火墙阻止。将 **-r** 与不支持 DNSSEC 的服务器一起使用会破坏验证。信任锚必须是最新的，DNSSEC 才能正常工作。

# HISTORY

**unbound-host** 是 NLnet Labs 的 Unbound 项目的一部分，提供对 Unbound 验证型解析器能力的命令行访问。它被设计为传统 host 和 dig 命令的 DNSSEC 感知替代品。

# INSTALL

```apt: sudo apt install unbound-host```

```dnf: sudo dnf install unbound```

```pacman: sudo pacman -S unbound```

```apk: sudo apk add unbound```

```zypper: sudo zypper install unbound```

```brew: brew install unbound```

```nix: nix profile install nixpkgs#unbound```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unbound](/man/unbound)(8), [unbound-control](/man/unbound-control)(8), [dig](/man/dig)(1), [host](/man/host)(1), [drill](/man/drill)(1), [nslookup](/man/nslookup)(1)
