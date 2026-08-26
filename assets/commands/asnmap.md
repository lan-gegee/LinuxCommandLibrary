# TAGLINE

映射自治系统编号与 IP 网段

# TLDR

查询 IP 对应的 **ASN**

```asnmap -ip [8.8.8.8]```

查询**域名**

```asnmap -d [google.com]```

按 **ASN 编号**查询

```asnmap -a [AS15169]```

按**组织**查询

```asnmap -org "[Google LLC]"```

从**文件**读取目标进行查询

```asnmap -f [targets.txt]```

以 JSON 输出 **CIDR 网段**

```asnmap -a [AS15169] -json```

# SYNOPSIS

**asnmap** [_-ip ip_] [_-d domain_] [_-a asn_] [_-org name_] [_options_]

# DESCRIPTION

**asnmap** 可快速映射 ASN（自治系统编号）信息。它能从 IP 地址、域名或组织名称查询 ASN，并返回关联的 IP 网段。

这对侦察、网络测绘以及了解组织的 IP 分配情况非常有用。

# PARAMETERS

**-ip** _address_
> 查询 IP 地址对应的 ASN

**-d** _domain_
> 查询域名对应的 ASN

**-a** _asn_
> 获取 ASN 的 IP 网段

**-org** _name_
> 按组织名称搜索

**-f**, **-file** _file_
> 从文件读取要查询的目标

**-j**, **-json**
> 以 JSON 格式显示输出

**-c**, **-csv**
> 以 CSV 格式显示输出

**-v6**
> 在 CLI 输出中显示 IPv6 CIDR 网段

**-silent**
> 静默输出（只显示结果）

**-o**, **-output** _file_
> 将输出写入文件

**-up**, **-update**
> 更新 asnmap 到最新版本

# CAVEATS

数据来自公开来源，可能不是最新的。有些组织拥有多个 ASN。用于安全工作时应对结果加以验证。

# HISTORY

**asnmap** 由 ProjectDiscovery 开发，是其安全侦察工具集的一部分。

# INSTALL

```dnf: sudo dnf install asnmap```

```aur: yay -S asnmap```

```brew: brew install asnmap```

```nix: nix profile install nixpkgs#asnmap```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[whois](/man/whois)(1), [dig](/man/dig)(1), [nmap](/man/nmap)(1), [subfinder](/man/subfinder)(1)

# RESOURCES

```[Source code](https://github.com/projectdiscovery/asnmap)```

<!-- verified: 2026-06-17 -->
