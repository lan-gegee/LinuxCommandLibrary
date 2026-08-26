# TAGLINE

基于 DNS 的 SSL 证书验证

# TLDR

使用 Cloudflare DNS **签发**证书

```export CF_Token="[token]" && acme.sh --issue -d [example.com] --dns dns_cf```

使用 **AWS Route53** 签发

```export AWS_ACCESS_KEY_ID="[key]" && export AWS_SECRET_ACCESS_KEY="[secret]" && acme.sh --issue -d [example.com] --dns dns_aws```

使用 **DigitalOcean** DNS 签发

```export DO_API_KEY="[token]" && acme.sh --issue -d [example.com] --dns dns_dgon```

通过 DNS 签发**泛域名（wildcard）**证书

```acme.sh --issue -d [example.com] -d [*.example.com] --dns dns_cf```

# SYNOPSIS

**acme.sh** --issue -d _domain_ --dns _dns_provider_ [_options_]

# DESCRIPTION

**acme.sh** 的 DNS 模式通过 DNS-01 验证实现证书自动签发。这种方式通过在域名的 DNS 区域中创建特定的 TXT 记录来证明域名所有权。泛域名证书必须使用此方法；当 HTTP 验证不可行时它也很有用。

该工具通过 API 集成支持超过 100 家 DNS 提供商。凭据通常通过环境变量提供，acme.sh 会自动创建和删除验证记录。

# PARAMETERS

**--dns** _provider_
> DNS 提供商插件名称（dns_cf、dns_aws、dns_gd、dns_ali 等）

**--dnssleep** _seconds_
> 等待 DNS 传播的秒数（默认：自动判断）

**--dns-alias** _domain_
> 使用别名词域进行 DNS 验证（CNAME 委派）

**-d** _domain_
> 域名（泛域名需重复使用：-d example.com -d *.example.com）

# COMMON DNS PROVIDERS

**dns_cf**
> Cloudflare（CF_Token 或 CF_Key + CF_Email）

**dns_aws**
> AWS Route53（AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY）

**dns_gd**
> GoDaddy（GD_Key + GD_Secret）

**dns_dgon**
> DigitalOcean（DO_API_KEY）

**dns_ali**
> 阿里云（Ali_Key + Ali_Secret）

**dns_gcloud**
> Google Cloud DNS（CLOUDSDK_ACTIVE_CONFIG_NAME）

**dns_linode**
> Linode（LINODE_V4_API_KEY）

**dns_ovh**
> OVH（OVH_AK + OVH_AS + OVH_CK）

# CONFIGURATION

**~/.acme.sh/account.conf**
> 首次使用后存储 DNS 提供商 API 凭据（token、密钥、secret）。续期证书时会自动复用这些凭据。

# CAVEATS

API 凭据保存在 account.conf 中以供自动续期。DNS 传播可能需要时间；如果验证失败，可增大 --dnssleep。部分提供商对 API 调用有速率限制。API token 的权限应仅限于 DNS 管理。

# HISTORY

**2016** 年，按照 ACME 协议规范，DNS 验证支持被加入 **acme.sh**。支持的 DNS 提供商数量大幅增长，社区贡献不断添加新的提供商。

# INSTALL

```pacman: sudo pacman -S acme.sh```

```apk: sudo apk add acme.sh```

```brew: brew install acme.sh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[acme.sh](/man/acme.sh)(1), [certbot](/man/certbot)(1), [dig](/man/dig)(1), [nslookup](/man/nslookup)(1)

# RESOURCES

```[Source code](https://github.com/acmesh-official/acme.sh)```

```[Documentation](https://github.com/acmesh-official/acme.sh/wiki/dnsapi)```

<!-- verified: 2026-06-10 -->
