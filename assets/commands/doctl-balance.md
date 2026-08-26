# TAGLINE

查询 DigitalOcean 账户的账单余额

# TLDR

**获取当前账户余额**

```doctl balance get```

**以 JSON 格式获取余额**

```doctl balance get --output json```

**只显示本月至今的用量**

```doctl balance get --format MonthToDateUsage```

# SYNOPSIS

**doctl balance** _command_ [_options_]

# PARAMETERS

**get**
> 获取当前账户余额、本月至今用量以及截至上次账单的余额。

**--format** _COLUMNS_
> 显示指定列（例如 MonthToDateUsage、AccountBalance、MonthToDateBalance、GeneratedAt）。

**--output** _FORMAT_
> 输出格式：text 或 json。

**--help**
> 显示帮助信息。

# DESCRIPTION

**doctl balance** 查询你的 DigitalOcean 账户的账单余额信息，显示当前余额、本月至今用量以及截至上次账单的账户余额。

该命令无需访问网页控制台即可快速查看支出和剩余额度，适合在自动化工作流或脚本中监控成本。

**get** 子命令（别名 **g**）是唯一可用的子命令。

# CAVEATS

余额更新与实际用量之间可能略有延迟。不显示按资源细分的详细费用。需要通过 **doctl auth init** 配置具有账单访问权限的有效 API 令牌。

# HISTORY

**doctl balance** 是 **DigitalOcean** 开发和维护的 **doctl** CLI 工具的一部分，用于以编程方式访问其云平台服务。

# SEE ALSO

[doctl](/man/doctl)(1), [doctl-account](/man/doctl-account)(1), [doctl-auth](/man/doctl-auth)(1)
