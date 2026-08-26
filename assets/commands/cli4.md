# TAGLINE

Cloudflare API v4 命令行客户端

# TLDR

**列出 Cloudflare 账户中所有区域**（域名）

```cli4 /zones```

**按 ID 获取特定区域的详细信息**

```cli4 /zones/[zone_id]```

**清除某个区域的全部分析缓存**

```cli4 --post /zones/[zone_id]/purge_cache purge_everything:=true```

**列出某个区域的 DNS 记录**

```cli4 /zones/[zone_id]/dns_records```

**创建一条 DNS 记录**

```cli4 --post /zones/[zone_id]/dns_records type:='"A"' name:='"www"' content:='"192.0.2.1"'```

**删除一条 DNS 记录**

```cli4 --delete /zones/[zone_id]/dns_records/[record_id]```

**更新一条页面规则**

```cli4 --put /zones/[zone_id]/pagerules/[rule_id] status:='"active"'```

# SYNOPSIS

**cli4** [_options_] _/endpoint_ [_data_...]

# PARAMETERS

**--get**
> HTTP GET 请求（默认）。

**--post**
> HTTP POST 请求。

**--put**
> HTTP PUT 请求。

**--patch**
> HTTP PATCH 请求。

**--delete**
> HTTP DELETE 请求。

**-q**, **--quiet**
> 不产生输出。

**-v**, **--verbose**
> 详细输出，包括 HTTP 头。

**-r**, **--raw**
> 输出未经格式化的原始 JSON。

**-d**, **--dump**
> 导出请求而不执行它。

# DESCRIPTION

**cli4** 是一个与 Cloudflare API v4 交互的命令行工具。它提供对所有 Cloudflare API 端点的直接访问，可以从终端管理区域、DNS 记录、防火墙规则、页面规则及其他 Cloudflare 功能。

该工具采用简单语法：API 端点以路径形式指定，数据以键值对形式传递。JSON 值使用 **:=** 运算符以保证类型正确，而字符串赋值使用 **=**。身份验证通过环境变量或配置文件处理。

cli4 对自动化和脚本化 Cloudflare 操作特别有用。它可以集成到 CI/CD 流水线中，用于缓存清除、DNS 更新或防火墙规则管理。

# CONFIGURATION

**~/.cloudflare/cloudflare.cfg**
> 存储 API 凭证（email、key 或 token），可作为环境变量的替代方案。

# CAVEATS

需要通过 **CF_API_EMAIL** 和 **CF_API_KEY** 环境变量进行身份验证，使用 API token 时则用 **CF_API_TOKEN**。区域 ID 必须单独获取；它们不是域名。速率限制遵循 Cloudflare API 文档的规定。

# HISTORY

cli4 是一个基于 Python 的非官方 CLI，为 Cloudflare 于 **2014 年**发布的 API v4 而创建。它是 Cloudflare 官方工具的轻量替代品，专注于直接访问 API 而非高层抽象。

# SEE ALSO

[wrangler](/man/wrangler)(1), [curl](/man/curl)(1), [flarectl](/man/flarectl)(1), [jq](/man/jq)(1)
