# TAGLINE

显示 DNS 域名

# TLDR

打印 FQDN 中的 **DNS 域名**部分

```dnsdomainname```

# SYNOPSIS

**dnsdomainname**

# DESCRIPTION

**dnsdomainname** 显示系统完全限定域名（FQDN）中的 DNS 域名部分。它先用 gethostname() 取得主机名，再通过 getaddrinfo() 经 DNS 查询解析为规范名称。

域名提取规则是取 FQDN 中第一个点之后的所有内容。例如 FQDN 为 "server.example.com" 时，dnsdomainname 返回 "example.com"。这与显示 NIS/YP 域的 domainname 等工具不同。在大多数发行版上，dnsdomainname 是指向同一个 **hostname** 多功能二进制文件的链接（等价于 `hostname --domain`）。该命令需要正确的 DNS 配置和名称解析才能正常工作。如果系统主机名不包含域部分或 DNS 解析失败，它会返回空结果。

# CAVEATS

如果系统主机名不含域名或 DNS 解析失败，则返回空结果。需要正确的 DNS 配置。

# INSTALL

```apt: sudo apt install hostname```

```dnf: sudo dnf install hostname```

```pacman: sudo pacman -S net-tools```

```apk: sudo apk add net-tools```

```zypper: sudo zypper install hostname```

```brew: brew install net-tools```

```nix: nix profile install nixpkgs#hostname```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hostname](/man/hostname)(1), [domainname](/man/domainname)(1), [hostnamectl](/man/hostnamectl)(1)
