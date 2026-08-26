# TAGLINE

验证型递归缓存 DNS 解析器

# TLDR

**启动 unbound DNS 服务器**

```sudo unbound```

**以指定配置文件启动**

```sudo unbound -c [path/to/unbound.conf]```

**在前台启动**（不守护进程化）

```sudo unbound -d```

**以详细输出启动**

```sudo unbound -v```

**检查配置文件**是否有错误

```unbound-checkconf [path/to/unbound.conf]```

**显示版本**

```unbound -V```

# SYNOPSIS

**unbound** [**-c** _configfile_] [**-d**] [**-p**] [**-v**] [**-V**] [**-h**]

# PARAMETERS

**-c** _configfile_
> 使用指定的配置文件而不是 /etc/unbound/unbound.conf。

**-d**
> 调试模式。不派生到后台，保持在前台运行。

**-p**
> 不使用 chroot，也不放弃特权。

**-v**
> 提高详细程度级别。可以多次指定以获得更多输出。

**-V**
> 显示版本信息。

**-h**
> 显示帮助信息。

# DESCRIPTION

**Unbound** 是一个验证型递归缓存 DNS 解析器，专为安全性和性能而设计。它代表客户端执行 DNS 查询，使用 DNSSEC 验证响应，并缓存结果以提高后续查询的响应时间。

与转发解析器不同，Unbound 是完整的递归解析器，可以直接查询根 DNS 服务器，从而消除对上游 DNS 提供商的依赖。它默认支持 DNSSEC 验证，通过验证 DNS 响应的真实性来防范缓存污染和其他 DNS 攻击。

配置通过 /etc/unbound/unbound.conf 完成，该文件控制监听接口、访问控制、DNSSEC 设置、缓存大小和性能调优。Unbound 既可作为单机的本地解析器运行，也可作为全网范围的 DNS 服务器运行。

相关工具包括用于运行时管理的 **unbound-control**、用于配置校验的 **unbound-checkconf**、用于 DNSSEC 根密钥管理的 **unbound-anchor**，以及用于 DNS 查询的 **unbound-host**。

# CONFIGURATION

**/etc/unbound/unbound.conf**
> 主配置文件，控制监听接口、访问控制、DNSSEC 设置、缓存大小和转发规则。

**/etc/unbound/unbound.conf.d/**
> 存放额外配置片段的目录，由主配置文件包含。

**/var/lib/unbound/root.key**
> 由 unbound-anchor 管理的 DNSSEC 根信任锚文件。

# CAVEATS

作为公共 DNS 解析器运行时，需要仔细配置访问控制以防滥用。DNSSEC 验证可能导致配置不当的域名解析失败。缓存大小应根据预期查询量和可用内存进行调优。确保定期用 unbound-anchor 更新根信任锚。

# HISTORY

**Unbound** 由荷兰的 **NLnet Labs** 开发，首个版本于 **2008 年 5 月**发布。它被设计为 BIND 的现代安全替代品，注重代码整洁和安全。Unbound 已成为多个 BSD 操作系统的默认 DNS 解析器，并广泛与 Pi-hole 及其他 DNS 过滤方案配合使用。

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

[unbound-control](/man/unbound-control)(8), [unbound-checkconf](/man/unbound-checkconf)(8), [unbound-host](/man/unbound-host)(1), [dig](/man/dig)(1), [nslookup](/man/nslookup)(1)
