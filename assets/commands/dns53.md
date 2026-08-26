# TAGLINE

Amazon Route53 动态 DNS 客户端

# TLDR

用当前 IP 地址**更新** DNS 记录

```dns53 update [domain] [record_name]```

以守护进程模式**运行**，自动更新

```dns53 daemon --domain [domain] --record [name]```

**检查**当前 IP 和配置

```dns53 status```

# SYNOPSIS

**dns53** [_command_] [_options_]

# PARAMETERS

**-d, --domain** _DOMAIN_
> 托管在 Route53 的域名

**-r, --record** _RECORD_
> 要更新的 DNS 记录名

**-i, --interval** _SECONDS_
> 更新间隔（秒）（守护进程模式）

**-t, --ttl** _SECONDS_
> DNS 记录的 TTL（默认：300）

**--access-key** _KEY_
> AWS access key ID

**--secret-key** _KEY_
> AWS secret access key

**--region** _REGION_
> AWS 区域（默认：us-east-1）

**-c, --config** _FILE_
> 配置文件路径

**-v, --verbose**
> 启用详细输出

**-h, --help**
> 显示帮助并退出

**--version**
> 显示版本并退出

# DESCRIPTION

**dns53** 是专为 Amazon Route53 设计的动态 DNS 客户端。它自动将 DNS A 记录更新为其所在主机的当前公网 IP 地址，非常适合家庭服务器或动态 IP 环境。

该工具可以单次运行更新记录，也可以以守护进程模式持续监控。它使用 AWS 凭证通过 Route53 API 完成身份验证并修改 DNS 记录。

# CONFIGURATION

配置文件格式（JSON）：

```json
{
  "domain": "example.com",
  "record": "home.example.com",
  "ttl": 300,
  "access_key": "AKIA...",
  "secret_key": "..."
}
```

# CAVEATS

需要具有 Route53 权限的有效 AWS 凭证。API 调用可能产生 AWS 费用。IP 检测依赖必须可达的外部服务。守护进程模式持续运行，占用系统资源。

# HISTORY

**dns53** 的出现填补了 Amazon Route53 在动态 DNS 支持方面的空白——Route53 本身不像传统 DNS 服务器那样支持动态更新。它为想在动态 IP 上借助 AWS DNS 运行服务的用户提供了一个轻量级方案。

# SEE ALSO

[aws](/man/aws)(1), [curl](/man/curl)(1), [dig](/man/dig)(1)
